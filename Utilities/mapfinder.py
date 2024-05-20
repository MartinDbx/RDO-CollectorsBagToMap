#   From: https://github.com/MartinDbx/RDO-CollectorsBagToMap
#   File: Utilities/mapfinder.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

import datetime, shutil, itemlib


def __dateOfToday(formattedDate) -> str:
    """Creates the .json line for the date of today."""

    return "    \"rdr2collector.date\": \"" + formattedDate + "\",\n"


def __collectionsToShow(selectedCollections: list) -> str:
    """Creates the .json line to show only the selected collections."""

    txt = ""

    for collection in selectedCollections[:-1]:
        txt += "\\\"" + itemlib.collectionsJR[collection[0]] + "\","

    txt += "\\\"" + itemlib.collectionsJR[selectedCollections[-1][0]] + "\""

    return "    \"rdr2collector.enabled-categories\": \"[" + txt + "]\","


def makeFileJR(collectionsToShow: list, uncollectedItems: list):
    """Generate 'collector-list.json' where only uncollectedItems of
    collectionsToShow are visible. This file can be uploaded into
    https://jeanropke.github.io/RDR2CollectorsMap/."""

    idx = 0
    today = datetime.date.today()
    formattedDate = today.strftime("%Y-%m-%d")
    fileName = "rdo-collector-map-list-" + formattedDate + ".json"

    shutil.copyfile("Utilities/template-collector-list.json", fileName)

    for item in uncollectedItems:

        with open(fileName, "r") as file:
            lines = file.readlines()

        with open(fileName, "w") as file:
            for line in lines:
                if idx == 0 and len(line) == 1:
                    file.write(__dateOfToday(formattedDate))
                    file.write(__collectionsToShow(collectionsToShow))
                    idx = 1
                if "collected" not in line or  itemlib.itemsJR[item] not in line:
                    file.write(line)
