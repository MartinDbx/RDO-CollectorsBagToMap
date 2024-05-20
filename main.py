#   From: https://github.com/MartinDbx/RDO-CollectorsBagToMap
#   File: main.py
#   Author: Martin Debaisieux
#   Date: 13 May 2024

import sys
sys.path.append("Utilities")
import scraper, mapfinder


if __name__ == "__main__":

    SELECTEDCOLL = scraper.readSelectedCollections()
    UNCOLLITEMS = scraper.scrapShoppingCart(SELECTEDCOLL)

    mapfinder.makeFileJR(SELECTEDCOLL, UNCOLLITEMS)

    if len(sys.argv) == 2 and sys.argv[1] in ["-r", "-reset"]:
        scraper.resetShoppingCart()