# Anki Airtable

This is an Anki plugin that can synchronize an Airtable to Anki. At the end of
the day, Anki is just a flash-card frontend to a database. Why not use Airtable as
that database? Airtable is much nicer to use as a database, and makes the data
searchable outside of Anki.

I use this to organize and memorize things like produce that's in season, the
trees and flowers of Ontario, cheeses from around the world, macronutrients of
various foods, how to make cocktails and learning new words.

For example, you might have an Airtable like this filled with words you want to
learn in a "To Learn" view:

![](https://cloud.githubusercontent.com/assets/97400/19216935/fe96cb94-8d9e-11e6-9f5d-4987c22f682f.png)

You fill out the word definition, and the new word migrates to a "Learning"
view. You add this view to `airtable-anki`:


```json
{
  "key": "your api key",
  "media_path": "/Users/sirup/Documents/Anki/Simon/collection.media/{}",
  "tables": [
    {
      "anki_deck": "English",
      "anki_model": "Word",
      "airtable_table": "Words",
      "airtable_view": "Learning",
      "airtable_key": "base key"
    }
  ]
```

You open Anki, and voila, you have a flash card with the new word!

![](https://cloud.githubusercontent.com/assets/97400/19216946/532d21da-8d9f-11e6-92b5-18f43b6ad762.gif)

## Installation

Place the `airtable.py` file in `~/Documents/Anki/addons` or wherever Anki is
installed.

Then put `settings.example.json` in `~/Documents/Anki/addons/settings.json` and
configure everything.

## Bugs

There's bound to be many.. this doesn't use any proper Airtable client for
Python because dependencies are hard in Anki and I don't know anything about
Anki. To my knowledge no-one but me is using this. If you use it or have trouble
getting it running, let me know!

## License

MIT
