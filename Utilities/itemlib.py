#   From: https://github.com/MartinDbx/RDO-CollectorsBagToMap
#   File: Utilities/itemlib.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

AntiqueAlcoholBottles = [
    "Antique Alcohol Bottles", "Caribbean Rum", "Irish Whiskey",
    "Scotch Whisky", "Tennessee Whiskey", "London Dry Gin", "Cognac",
    "Old Tom Gin", "Absinthe", "Gran Corazon Madeira"
]

FamilyHeirlooms = [
    "FamilyHeirlooms", "Ebony Hairbrush", "New Guinea Rosewood Hairbrush",
    "Jade Hairpin", "Ivory Hairpin", "Carved Wooden Hairpin",
    "Horse Hair Brush", "Goat Hair Brush", "Cherrywood Comb", "Ebony Hairpin",
    "Boar Bristle Brush", "Boxwood Comb", "Tortoiseshell Comb",
    "Metal Hairpin", "Rosewood Hairbrush", "Ivory Comb"
]

SuitOfCupsTarotCards = [
    "Suit of Cups Tarot Cards", "Ace of Cups Tarot Card",
    "Two of Cups Tarot Card", "Three of Cups Tarot Card",
    "Four of Cups Tarot Card", "Five of Cups Tarot Card",
    "Six of Cups Tarot Card", "Seven of Cups Tarot Card",
    "Eight of Cups Tarot Card", "Nine of Cups Tarot Card",
    "Ten of Cups Tarot Card", "Page of Cups Tarot Card",
    "Knight of Cups Tarot Card", "Queen of Cups Tarot Card",
    "King of Cups Tarot Card"
]

SuitOfPentaclesTarotCards = [
    "Suit of Pentacles Tarot Cards", "Ace of Pentacles Tarot Card",
    "Two of Pentacles Tarot Card", "Three of Pentacles Tarot Card",
    "Four of Pentacles Tarot Card", "Five of Pentacles Tarot Card",
    "Six of Pentacles Tarot Card", "Seven of Pentacles Tarot Card",
    "Eight of Pentacles Tarot Card", "Nine of Pentacles Tarot Card",
    "Ten of Pentacles Tarot Card", "Page of Pentacles Tarot Card",
    "Knight of Pentacles Tarot Card", "Queen of Pentacles Tarot Card",
    "King of Pentacles Tarot Card"
]

SuitOfSwordsTarotCards = [
    "Suit of Swords Tarot Cards", "Ace of Swords Tarot Card",
    "Two of Swords Tarot Card", "Three of Swords Tarot Card",
    "Four of Swords Tarot Card", "Five of Swords Tarot Card",
    "Six of Swords Tarot Card", "Seven of Swords Tarot Card",
    "Eight of Swords Tarot Card", "Nine of Swords Tarot Card",
    "Ten of Swords Tarot Card", "Page of Swords Tarot Card",
    "Knight of Swords Tarot Card", "Queen of Swords Tarot Card",
    "King of Swords Tarot Card"
]

SuitOfWandsTarotCards = [
    "Suit of Wands Tarot Cards", "Ace of Wands Tarot Card",
    "Two of Wands Tarot Card", "Three of Wands Tarot Card",
    "Four of Wands Tarot Card", "Five of Wands Tarot Card",
    "Six of Wands Tarot Card", "Seven of Wands Tarot Card",
    "Eight of Wands Tarot Card", "Nine of Wands Tarot Card",
    "Ten of Wands Tarot Card", "Page of Wands Tarot Card",
    "Knight of Wands Tarot Card", "Queen of Wands Tarot Card",
    "King of Wands Tarot Card"
]

COLLECTIONS = [
    AntiqueAlcoholBottles,
    FamilyHeirlooms,
    SuitOfCupsTarotCards,
    SuitOfPentaclesTarotCards,
    SuitOfSwordsTarotCards,
    SuitOfWandsTarotCards
]


# Translation according to jeanropke's naming convention.
collectionsJR = {
    "Antique Alcohol Bottles" : "bottle\\",
    "FamilyHeirlooms" : "heirlooms\\",
    "Suit of Cups Tarot Cards" : "cups\\",
    "Suit of Pentacles Tarot Cards" : "pentacles\\",
    "Suit of Swords Tarot Cards" : "swords\\",
    "Suit of Wands Tarot Cards" : "wands\\"
}

itemsJR = {
    "Caribbean Rum" : "carib_rum",
    "Irish Whiskey" : "irish_whiskey",
    "Scotch Whisky" : "scotch_whiskey",
    "Tennessee Whiskey" : "tenn_whiskey",
    "London Dry Gin" : "londry_gin",
    "Cognac" : "cognac",
    "Old Tom Gin" : "oldtom_gin",
    "Absinthe" : "cyprus_brandy",
    "Gran Corazon Madeira" : "plymouth_gin",

    "Ebony Hairbrush" : "brush_ebony",
    "New Guinea Rosewood Hairbrush" : "brush_rosewood_ng",
    "Jade Hairpin" : "hairpin_jade",
    "Ivory Hairpin" : "hairpin_ivory",
    "Carved Wooden Hairpin" : "hairpin_wooden",
    "Horse Hair Brush" : "brush_horsehair",
    "Goat Hair Brush" : "brush_goathair",
    "Cherrywood Comb" : "comb_cherrywood",
    "Ebony Hairpin" : "hairpin_ebony",
    "Boar Bristle Brush" : "brush_boar",
    "Boxwood Comb" : "comb_boxwood",
    "Tortoiseshell Comb" : "comb_tortoiseshell",
    "Metal Hairpin" : "hairpin_metal",
    "Rosewood Hairbrush" : "brush_rosewood",
    "Ivory Comb" : "comb_ivory",

    "Ace of Cups Tarot Card" : "ace_cups",
    "Two of Cups Tarot Card" : "two_cups",
    "Three of Cups Tarot Card" : "three_cups",
    "Four of Cups Tarot Card" : "four_cups",
    "Five of Cups Tarot Card" : "five_cups",
    "Six of Cups Tarot Card" : "six_cups",
    "Seven of Cups Tarot Card" : "seven_cups",
    "Eight of Cups Tarot Card" : "eight_cups",
    "Nine of Cups Tarot Card" : "nine_cups",
    "Ten of Cups Tarot Card" : "ten_cups",
    "Page of Cups Tarot Card" : "page_cups",
    "Knight of Cups Tarot Card" : "knight_cups",
    "Queen of Cups Tarot Card" : "queen_cups",
    "King of Cups Tarot Card" : "king_cups",

    "Ace of Pentacles Tarot Card" : "ace_pentacles",
    "Two of Pentacles Tarot Card" : "two_pentacles",
    "Three of Pentacles Tarot Card" : "three_pentacles",
    "Four of Pentacles Tarot Card" : "four_pentacles",
    "Five of Pentacles Tarot Card" : "five_pentacles",
    "Six of Pentacles Tarot Card" : "six_pentacles",
    "Seven of Pentacles Tarot Card" : "seven_pentacles",
    "Eight of Pentacles Tarot Card" : "eight_pentacles",
    "Nine of Pentacles Tarot Card" : "nine_pentacles",
    "Ten of Pentacles Tarot Card" : "ten_pentacles",
    "Page of Pentacles Tarot Card" : "page_pentacles",
    "Knight of Pentacles Tarot Card" : "knight_pentacles",
    "Queen of Pentacles Tarot Card" : "queen_pentacles",
    "King of Pentacles Tarot Card" : "king_pentacles",

    "Ace of Swords Tarot Card" : "ace_swords",
    "Two of Swords Tarot Card" : "two_swords",
    "Three of Swords Tarot Card" : "three_swords",
    "Four of Swords Tarot Card" : "four_swords",
    "Five of Swords Tarot Card" : "five_swords",
    "Six of Swords Tarot Card" : "six_swords",
    "Seven of Swords Tarot Card" : "seven_swords",
    "Eight of Swords Tarot Card" : "eight_swords",
    "Nine of Swords Tarot Card" : "nine_swords",
    "Ten of Swords Tarot Card" : "ten_swords",
    "Page of Swords Tarot Card" : "page_swords",
    "Knight of Swords Tarot Card" : "knight_swords",
    "Queen of Swords Tarot Card" : "queen_swords",
    "King of Swords Tarot Card" : "king_swords",

    "Ace of Wands Tarot Card" : "ace_wands",
    "Two of Wands Tarot Card" : "two_wands",
    "Three of Wands Tarot Card" : "three_wands",
    "Four of Wands Tarot Card" : "four_wands",
    "Five of Wands Tarot Card" : "five_wands",
    "Six of Wands Tarot Card" : "six_wands",
    "Seven of Wands Tarot Card" : "seven_wands",
    "Eight of Wands Tarot Card" : "eight_wands",
    "Nine of Wands Tarot Card" : "nine_wands",
    "Ten of Wands Tarot Card" : "ten_wands",
    "Page of Wands Tarot Card" : "page_wands",
    "Knight of Wands Tarot Card" : "knight_wands",
    "Queen of Wands Tarot Card" : "queen_wands",
    "King of Wands Tarot Card" : "king_wands"
}