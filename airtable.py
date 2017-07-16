from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from anki.hooks import addHook
from anki.importing.noteimp import NoteImporter, ForeignNote
import httplib, urllib
from urlparse import urlparse
import md5
import ssl
import json
import pprint
import subprocess
import httplib2

Settings = {}

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/settings.json") as settings:
    Settings = json.load(settings)

class AirtableImporter(NoteImporter):
    importMode = 0
    allowHTML = True

    def __init__(self, col, table, view, api_key, app_key, linked_record_fields):
        NoteImporter.__init__(self, col, "")
        self.records = None
        self.table = table
        self.view = view
        self.api_key = api_key
        self.app_key = app_key
        self.linked_record_fields = linked_record_fields

    def outputLog(self):
        for statement in self.log:
            sys.stderr.write(statement + "\n")

    # TODO: This plugin should own the model completely. The document ID should
    # also be in there, so if the name changes or is removed, another card is
    # not created. Instead, old documents should be removed.
    def updateModel(self, model):
        models = mw.col.models
        fieldNames = models.fieldNames(model)

        for record in self.getRecords():
            for key in record["fields"].keys():
                if key not in fieldNames:
                    field = models.newField(key)
                    models.addField(model, field)
                    fieldNames = models.fieldNames(model)

    def fields(self):
        return len(self.model['flds'])

    def foreignNotes(self):
        notes = []

        for record in self.getRecords():
            note = ForeignNote()

            fields = record["fields"]
            modelFields = self.model["flds"]

            for field in modelFields:
                key = field['name']

                # sys.stderr.write(key + "\n")

                if key in fields:
                    if isinstance(fields[key], list):
                        if len(fields[key]) == 0:
                            note.fields.append("")
                        elif isinstance(fields[key][0], dict):
                            note.fields.append(self.downloadToCollection(fields[key]))
                        else:
                            strings = [str(e) for e in fields[key]]
                            note.fields.append(", ".join(strings))
                    else:
                        if not isinstance(fields[key], str) and not isinstance(fields[key], unicode):
                            fields[key] = unicode(fields[key])

                        asciiToHtml = fields[key].replace("\n", "<br/>")
                        note.fields.append(asciiToHtml)
                else:
                    note.fields.append("")

                # sys.stderr.write(key + " => " + note.fields[len(note.fields) - 1] + "\n")

            notes.append(note)

        return notes

    def sendAirtableRequest(self, url):
        headers = { "Authorization": "Bearer " + self.api_key }

        conn = httplib.HTTPSConnection("api.airtable.com")
        conn.request("GET", url, "", headers)

        response = conn.getresponse()
        raw_response = response.read()
        json_response = json.loads(raw_response)

        if "error" in json_response:
            sys.stderr.write(raw_response)
            return None

        return json_response

    def fetchRecord(self, table, record_id):
        return self.sendAirtableRequest("/v0/{}/{}/{}".format(self.app_key, table, record_id))

    def fetchLinkedRecord(self, table, record_id, primary_field):
        record = self.fetchRecord(table, record_id)
        return record["fields"][primary_field]

    def getRecords(self):
        if self.records:
            return self.records
        else:
            self.records = []

            offset = 0
            while True:
                json_response = self.sendAirtableRequest("/v0/{}/{}?view={}&offset={}".format(self.app_key, self.table, self.view, offset))

                if json_response:
                    for linked_record in self.linked_record_fields:
                        field = linked_record["field"]
                        table = linked_record["table"]
                        primary_field = linked_record["primary_field"]

                        for record in json_response["records"]:
                            # Sometimes a value hasn't been filled in for this field.
                            if field not in record["fields"]:
                                continue

                            linked_record_ids = record["fields"].get(field, None)

                            # Sometimes a linked record is a string, but it can be
                            # a list if linking to multiple records is allowed.  To
                            # keep the code simple, let's always make it a list.
                            if not isinstance(linked_record_ids, list):
                                linked_record_ids = [linked_record_ids]

                            linked_records = [self.fetchLinkedRecord(table, rid, primary_field) for rid in linked_record_ids]
                            record["fields"][field] = linked_records

                    self.records.extend(json_response["records"])

                    if "offset" in json_response:
                        offset = json_response["offset"]
                    else:
                        break

            return self.records

    def downloadToCollection(self, media):
        field = ""

        for medium in media:
            url = medium["url"]

            if "thumbnails" in medium: # spare some size if it's an image!
                url = medium["thumbnails"]["large"]["url"]

            _, extension = os.path.splitext(url)
            digest = md5.new(url).hexdigest()
            filename = u"{}{}".format(digest, extension)

            location = unicode(Settings["media_path"]).format(filename)

            command = u"curl {} -o '{}'".format(url, location)

            if not os.path.isfile(location):
                return_code = subprocess.call(command, shell=True)

            if extension == ".jpg" or extension == ".png" or extension == ".jpeg":
                field += u"<img src=\"{}\" />".format(filename)
            elif extension == ".ogg" or extension == ".mp3":
                field += u"[sound:{}]".format(filename)
            else:
                field += filename

        return field

def airtableImport(col, deck, modelName, table, view, app_key, linked_record_fields=[]):
    did = mw.col.decks.id(deck)
    mw.col.decks.select(did)

    model = mw.col.models.byName(modelName)

    if not model:
        model = mw.col.models.new(modelName)
        mw.col.models.add(model)

        template = mw.col.models.newTemplate("Default")
        mw.col.models.addTemplate(model, template)

    model['did'] = did

    deck = mw.col.decks.get(did)
    deck['mid'] = model['id']
    mw.col.decks.save(deck)

    airtable = AirtableImporter(mw.col, table, view, Settings["key"], app_key, linked_record_fields)
    airtable.updateModel(model)
    airtable.initMapping()
    airtable.run()

# TODO: Two-way sync would be dope, so fixing typos or changing content would be
# propegated to Airtable. E.g. when visiting a vocab card, it'd be great to add
# another sentence each time.
#
# TODO: Automatic cloze cards for English words.
def hook():
    for table in Settings["tables"]:
        airtableImport(mw.col, table["anki_deck"], table["anki_model"], table["airtable_table"], table["airtable_view"], table["airtable_key"], table.get("airtable_linked_record_fields", []))

addHook("profileLoaded", hook)
