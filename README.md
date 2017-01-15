# Anki Airtable

This is an Anki plugin that can synchronize an Airtable to Anki. At the end of
the day, Anki is just a flash-card frontend to a database. Why not use Airtable as
that database? Airtable is much nicer to use as a database, and makes the data
searchable outside of Anki.

I use this to organize and memorize things like the trees and flowers of
Ontario, cheeses from around the world, macronutrients of various foods, how to
make cocktails and learning new words.

Let's say you're dying to learn when all produce is in season to impress your
friends and own the local farmer's market. While you're at it, why not learn the
origin of all these vegetables too? :tomato: :corn: :eggplant: :apple:

Having all that information is great. But you really want to have a full
overview of all produce by season, and not just have it in your head. Airtable
is fantastic for this!

Okay, so you spent the entire afternoon [typing in all the produce that grows
near you](https://airtable.com/shrvVrHDN6idKdAZN):

[![](http://g.recordit.co/fTzu3HjP3l.gif)](https://airtable.com/shrvVrHDN6idKdAZN)

This is awesome. You've created some super complicated views in Airtable where
you filter your recipes by seasonality, so it won't show you asparagus recipes
in the winter, or butternut squash in the spring. Sick.

But back to learning this by heart. You want this table in your head.
Unfortunately, Airtable doesn't have a brain interface and this is [likely not
happening anytime
soon](https://en.wikipedia.org/wiki/Superintelligence:_Paths,_Dangers,_Strategies).
Your best bet to learn this by heart so you can spot the seasonal restaurants
and impress your local chefs are flash cards. Basically, you want to learn this
table by heart.

This is where Airtable Anki wins. You **install the extension** by throwing
`airtable.py` in your Anki `addon` directory, located in
`~/Documents/Anki/addons`. Put `settings.json` in that directory as well. A
quick command that'll work for most (you may have to adjust the username, but
default is `User 1`):

```bash
curl https://raw.githubusercontent.com/Sirupsen/anki-airtable/master/airtable.py \
  -o ~/Library/Application\ Support/Anki/User\ 1/addons/airtable.py
curl https://raw.githubusercontent.com/Sirupsen/anki-airtable/master/settings.example.json \
  -o ~/Library/Application\ Support/Anki/User\ 1/addons/settings.json
```

Then open `settings.json` with an editor and configure it:

```json
{
  "key": "your api key from api.airtable.com",
  "media_path": "/Users/your_username/Library/Application Support/Anki2/User 1/collection.media/{}",
  "tables": [
    {
      "anki_deck": "NerdCooking",
      "anki_model": "Produce",
      "airtable_table": "Produce",
      "airtable_view": "All",
      "airtable_key": "base key from api.airtable.com"
    }
  ]
```

This extension will automatically create a "Produce" model if it doesn't exist,
but there will be no cards. You can also create the model yourself beforehand
with all the fields you'd like to include from the Airtable records. 

Note that Anki will NOT import Airtable records that don't generate any cards,
so you'll have to restart Anki after creating cards for your new model, whether
or not it was created manually or with Airtable Anki.

Once you've created some cards for the new model, you'll see some brand new cards:

![](http://g.recordit.co/o4srVtFVRD.gif)
![](http://g.recordit.co/hJQa8Hlqu3.gif)

## Bugs

There's bound to be many.. this doesn't use any proper Airtable client for
Python because dependencies are hard in Anki and I don't know anything about
Anki. To my knowledge no-one but me is using this. If you use it or have trouble
getting it running, let me know!

## License

MIT
