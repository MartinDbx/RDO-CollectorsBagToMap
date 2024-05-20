#   From: https://github.com/MartinDbx/RDO-CollectorsBagToMap
#   File: Utilities/scraper.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

import sys, shutil
sys.path.append("../Collections")
sys.path.append("../Utilities")
import itemlib


def readSelectedCollections() -> list:
    """Extract from the shopping cart the list of selected collections."""

    selectedCollections = []

    with open("shopping-cart.txt") as file:
        for i, line in enumerate(file):
            if "1" in line:
                selectedCollections.append(itemlib.COLLECTIONS[i])

    return selectedCollections


def resetShoppingCart():
    """Reset shopping-cart.txt file."""

    shutil.copyfile("Utilities/template-shopping-cart.txt", "shopping-cart.txt")


def __scraper(collection: list) -> list:
    """Given the HTML of the R* page of a collection, returns the uncollected
    items of this collection."""

    uncollectedItems = []
    associatedFile = "Collections/" + collection[0] + ".txt"

    with open(associatedFile) as file:
        contents = file.read()

        for item in collection[1:]:
            if item + "</span><div class" not in contents:
                uncollectedItems.append(item)

    return uncollectedItems


def scrapShoppingCart(collections: list) -> list:
    """Given a list of collections, returns all the uncollected items of these
    collections."""

    allUncollectedItems = []

    for collection in collections:
        allUncollectedItems += __scraper(collection)

    return allUncollectedItems