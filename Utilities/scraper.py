#   From: https://github.com/MartinDbx/RDO-CollectorBagToMap
#   File: Utilities/scraper.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

import sys, shutil
sys.path.append("../Collections")
sys.path.append("../Utilities")
import items


def readShoppingCart() -> list:
    """Construct from the shopping cart the list of the selected collections
    (all items)."""

    cart = []

    with open("shopping-cart.txt") as file:
        for i, line in enumerate(file):
            if "1" in line:
                cart.append(items.COLLECTIONS[i])

    return cart


def resetShoppingCart():
    """Reset shopping-cart.txt file."""

    shutil.copyfile("Utilities/template-shopping-cart.txt", "shopping-cart.txt")


def __scraper(collection: list) -> list:
    """Given a collection, returns the uncollected items of this collection via
    the HTML of the R* page."""

    uncollectedItems = []
    associatedFile = "Collections/" + collection[0] + ".txt"

    with open(associatedFile) as file:
        contents = file.read()
        for item in collection[1:]:
            if item + "</span><div class" not in contents:
                uncollectedItems.append(item)

    return uncollectedItems


def scrapShoppingCart(cart: list) -> list:
    """Given a list of collections (cart), returns the uncollected items of
    these collections."""

    allUncollectedItems = []

    for collection in cart:
        allUncollectedItems += __scraper(collection)

    return allUncollectedItems