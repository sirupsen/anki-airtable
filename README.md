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
origin of all these vegetables too? :tomato: :corn :eggplant: :apple:

Having all that information is great. But you really want to have a full
overview of all produce by season, and not just have it in your head. Airtable
is fantastic for this!

Okay, so you spent the entire afternoon typing in all the produce that grows
near you:

![](https://cloud.githubusercontent.com/assets/97400/19216985/80027fd8-8da0-11e6-9308-8a45bdb063aa.png)

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

This is where Airtable Anki wins. You install the extension by throwing
`airtable.py` in your Anki `addon` directory, located in
`~/Documents/Anki/addons`. Put `settings.json` in that directory as well, and
configure it to use your glowing new Airtable:

```json
{
  "key": "your api key from api.airtable.com",
  "media_path": "/Users/YOUR NAME/Documents/Anki/YOUR ANKI NAME/collection.media/{}",
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

You'll need to create a new "Produce" model in Anki first. The extension
*should* automatically create the fields, but it's not smart enough to create
models yet (you should add that).

Finally, open Anki, and you'll see some brand new cards.

![](https://cloud.githubusercontent.com/assets/97400/19217043/ba883ae2-8da2-11e6-9faf-02b856fb5c58.gif)

## Bugs

There's bound to be many.. this doesn't use any proper Airtable client for
Python because dependencies are hard in Anki and I don't know anything about
Anki. To my knowledge no-one but me is using this. If you use it or have trouble
getting it running, let me know!

## License

MIT
