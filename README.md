# RDO - Collector Bag to Map

The jeanropke's [Collectors Map](https://jeanropke.github.io/RDR2CollectorsMap/) is an efficient way to complete your Red Dead Online collections. Compare your collections and hide the items you've collected is quite tedious. This repository automates this process, by extracting uncollected items from the Rockstar Games HTML files and generating a settings file that can be imported into the map.

## Supported collections

For some collections, it is not possible to determine the location of a given item. This tool is therefore only designed for deterministic collections.

- [ ] American Wild Flowers	(soon)
- [x] Antique Alcohol Bottles
- [ ] Bird Eggs (soon)
- [x] Family Heirlooms
- [x] Suit of Cups Tarot Cards
- [x] Suit of Pentacles Tarot Cards
- [x] Suit of Swords Tarot Cards
- [x] Suit of Wands Tarot Cards


## Usage

1. Sign in to Social Club (in English) and go to your [collector's bag](https://socialclub.rockstargames.com/games/rdo/roles/collector/bag). For each collection you want, copy the HTML code (inspect the page) and paste it into the appropriate file of `Collections/`. See an [example](Utilities/template-collection.txt) of what this looks like. 
2. For each collection you want to appear in the list, set the corresponding bit to 1 in `shopping-cart.txt`.
3. Run `main.py` in your shell. This builds the file `collector-list.json`.
4. Import `collector-list.json` as settings into jeanropke's [Collectors Map](https://jeanropke.github.io/RDR2CollectorsMap/).


## Options

When running the script, you can add the option `-r` or `-reset` to reset the `shopping-cart.txt` file.
