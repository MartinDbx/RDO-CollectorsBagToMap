#   From: https://github.com/MartinDbx/RDO-CollectorBagToMap
#   File: Utilities/lister.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

import sys, shutil, items
sys.path.append("..")


def __collectionsToShow(cart: list):
    """Creates the .json line to show only the selected collections."""

    txt = ""

    for collection in cart[:-1]:
        txt += "\\\"" + items.collectionsJR[collection[0]] + "\","

    txt += "\\\"" + items.collectionsJR[cart[-1][0]] + "\""

    return "    \"rdr2collector.enabled-categories\": \"[" + txt + "]\","


def makeFileJR(collectionsToShow: list, uncollectedItems: list):
    """"Generate 'collector-list.json' where only uncollectedItems of
    collectionsToShow are visible. This file can be uploaded into
    https://jeanropke.github.io/RDR2CollectorsMap/."""

    shutil.copyfile("Utilities/template-collector-list.json", "collector-list.json")
    idx = 0

    for item in uncollectedItems:
        with open("collector-list.json", "r") as file:
            lines = file.readlines()
        with open("collector-list.json", "w") as file:
            for line in lines:
                if idx == 0 and len(line) == 1:
                    file.write(__collectionsToShow(collectionsToShow))
                    idx = 1
                if "collected" not in line or  items.itemsJR[item] not in line:
                    file.write(line)