import sys, shutil
sys.path.append("Others")
import dictionariesJR


# Supported collections
AntiqueAlcoholBottles = ["Antique Alcohol Bottles",
                         "Caribbean Rum",
                         "Irish Whiskey",
                         "Scotch Whisky",
                         "Tennessee Whiskey",
                         "London Dry Gin",
                         "Cognac",
                         "Old Tom Gin",
                         "Absinthe",
                         "Gran Corazon Madeira"]
FamilyHeirlooms = ["FamilyHeirlooms",
                   "Ebony Hairbrush",
                   "New Guinea Rosewood Hairbrush",
                   "Jade Hairpin",
                   "Ivory Hairpin",
                   "Carved Wooden Hairpin",
                   "Horse Hair Brush",
                   "Goat Hair Brush",
                   "Cherrywood Comb",
                   "Ebony Hairpin",
                   "Boar Bristle Brush",
                   "Boxwood Comb",
                   "Tortoiseshell Comb",
                   "Metal Hairpin",
                   "Rosewood Hairbrush",
                   "Ivory Comb"]
SuitOfCupsTarotCards = ["Suit of Cups Tarot Cards",
                        "Ace of Cups Tarot Card",
                        "Two of Cups Tarot Card",
                        "Three of Cups Tarot Card",
                        "Four of Cups Tarot Card",
                        "Five of Cups Tarot Card",
                        "Six of Cups Tarot Card",
                        "Seven of Cups Tarot Card",
                        "Eight of Cups Tarot Card",
                        "Nine of Cups Tarot Card",
                        "Ten of Cups Tarot Card",
                        "Page of Cups Tarot Card",
                        "Knight of Cups Tarot Card",
                        "Queen of Cups Tarot Card",
                        "King of Cups Tarot Card"]
SuitOfPentaclesTarotCards = ["Suit of Pentacles Tarot Cards",
                             "Ace of Pentacles Tarot Card",
                             "Two of Pentacles Tarot Card",
                             "Three of Pentacles Tarot Card",
                             "Four of Pentacles Tarot Card",
                             "Five of Pentacles Tarot Card",
                             "Six of Pentacles Tarot Card",
                             "Seven of Pentacles Tarot Card",
                             "Eight of Pentacles Tarot Card",
                             "Nine of Pentacles Tarot Card",
                             "Ten of Pentacles Tarot Card",
                             "Page of Pentacles Tarot Card",
                             "Knight of Pentacles Tarot Card",
                             "Queen of Pentacles Tarot Card",
                             "King of Pentacles Tarot Card"]
SuitOfSwordsTarotCards = ["Suit of Swords Tarot Cards",
                          "Ace of Swords Tarot Card",
                          "Two of Swords Tarot Card",
                          "Three of Swords Tarot Card",
                          "Four of Swords Tarot Card",
                          "Five of Swords Tarot Card",
                          "Six of Swords Tarot Card",
                          "Seven of Swords Tarot Card",
                          "Eight of Swords Tarot Card",
                          "Nine of Swords Tarot Card",
                          "Ten of Swords Tarot Card",
                          "Page of Swords Tarot Card",
                          "Knight of Swords Tarot Card",
                          "Queen of Swords Tarot Card",
                          "King of Swords Tarot Card"]
SuitOfWandsTarotCards = ["Suit of Wands Tarot Cards",
                         "Ace of Wands Tarot Card",
                         "Two of Wands Tarot Card",
                         "Three of Wands Tarot Card",
                         "Four of Wands Tarot Card",
                         "Five of Wands Tarot Card",
                         "Six of Wands Tarot Card",
                         "Seven of Wands Tarot Card",
                         "Eight of Wands Tarot Card",
                         "Nine of Wands Tarot Card",
                         "Ten of Wands Tarot Card",
                         "Page of Wands Tarot Card",
                         "Knight of Wands Tarot Card",
                         "Queen of Wands Tarot Card",
                         "King of Wands Tarot Card"]

# List of all supported collections
COLLECTIONS = [AntiqueAlcoholBottles,
               FamilyHeirlooms,
               SuitOfCupsTarotCards,
               SuitOfPentaclesTarotCards,
               SuitOfSwordsTarotCards,
               SuitOfWandsTarotCards]


def __readShoppingCart():
    cart = []
    with open("Shopping Cart.txt") as file:
        for i, line in enumerate(file):
            if "1" in line:
                cart.append(COLLECTIONS[i])
    return cart

def __scraper(collection: list):
    uncollectedObjects = []
    associatedFile = "Collections/" + collection[0] + ".txt"

    with open(associatedFile) as file:
        contents = file.read()
        for ob in collection[1:]:
            if ob + "</span><div class" not in contents:
                uncollectedObjects.append(ob)

    return uncollectedObjects

def __scrapShoppingCart():
    cart = __readShoppingCart()
    objectsToShow = []
    for collection in cart:
        objectsToShow += __scraper(collection)
    return objectsToShow

def __collectionsToDisplay(cart: list):
    txt = ""
    for collection in __readShoppingCart()[:-1]:
        txt += "\\\"" + dictionariesJR.listsJR[collection[0]] + "\","
    txt += "\\\"" + dictionariesJR.listsJR[__readShoppingCart()[-1][0]] + "\""

    return "    \"rdr2collector.enabled-categories\": \"[" + txt + "]\","


def __deleteGoodLines(uncollected: list):
    shutil.copyfile("Others/template.json", "collector-list.json")
    cnt = 0

    for ob in uncollected :
        with open("collector-list.json", "r") as file:
            lines = file.readlines()
        with open("collector-list.json", "w") as file:
            for line in lines:
                if cnt == 0 and len(line) == 1:
                    file.write(__collectionsToDisplay(__readShoppingCart()))
                    cnt = 1
                if "collected" not in line or dictionariesJR.itemsJR[ob] not in line:
                    file.write(line)







    # with open("collector-list.json") as file:
    #     lines = file.readlines()
    # with open("collector-list.json") as file:
    #     for line in lines:
    #         if "categories" in line:
    #             file.write()

__deleteGoodLines(__scrapShoppingCart())

# print(__collectionsToDisplay(__scrapShoppingCart()))
