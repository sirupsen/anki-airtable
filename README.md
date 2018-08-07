# Anki Airtable

**Note: This plugin is only compatible with Anki 2.1.**

This is an Anki plugin that can synchronize an Airtable to Anki when Anki starts
up. At the end of the day, Anki is just a flash-card frontend to a database. Why
not use Airtable as that database? Airtable is much nicer to use as a database,
and makes the data searchable outside of Anki.

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

This is where Airtable Anki wins. 

Install by importing extension `1573217784`:

![](https://user-images.githubusercontent.com/97400/43768257-38da0a54-9a37-11e8-855d-4000e326c0ad.png)

Then highlight the plugin and click `Config`, and change the configuration file:

![](https://user-images.githubusercontent.com/97400/43768310-5b3883e6-9a37-11e8-8028-320ea356d464.png)

**This is very important, please make sure you understand this section.**

You will need to manually create the `Produce` model if it doesn't exist. You
will ALSO need to create cards for the model because `anki-airtable` will NOT
import records that don't generate any cards. So: (1) create the model, (2)
create cards, (3) restart Anki with this plugin.

Once you've created some cards for the new model, you'll see some brand new cards:

![](http://g.recordit.co/o4srVtFVRD.gif)
![](http://g.recordit.co/hJQa8Hlqu3.gif)

## Bugs

There's bound to be many.. this doesn't use any proper Airtable client for
Python because dependencies are hard in Anki and I don't know anything about
Python. To my knowledge no-one but me is using this. If you use it or have
trouble getting it running, let me know in an issue!

## License

MIT
