#   From: https://github.com/MartinDbx/RDO-CollectorBagToMap
#   File: main.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

import sys
sys.path.append("Utilities")
import scraper, lister


if __name__ == "__main__" :

    SHOPCART = scraper.readShoppingCart()
    UNCOLLITEMS = scraper.scrapShoppingCart(SHOPCART)

    lister.makeFileJR(SHOPCART, UNCOLLITEMS)

    # scraper.resetShoppingCart()