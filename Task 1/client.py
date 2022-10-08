################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request
from statistics import mean
import pandas as pd

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote: dict) -> tuple:
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = mean([bid_price, ask_price])
    return stock, bid_price, ask_price, price


def getRatio(price_a: float, price_b: float) -> float:
    """ Get ratio of price_a and price_b """
    try:
        return price_a / price_b
    except ZeroDivisionError:
        return 0


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    # for _ in iter(range(N)):
    quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

    """ ----------- Update to get the ratio --------------- """
    prices = {}
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        prices[stock] = price
        print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

    # Calculate the ratio for each stock pair
    ratios = {k: {} for k in prices.keys()}
    for stock_a, price_a in prices.items():
        # Get the ratio for all stock pairs
        ratios[stock_a] = {stock_b: getRatio(price_a, price_b) for stock_b, price_b in prices.items()}
    
    # Format the ratios into a neat ratio matrix Pandas dataframe
    ratio_matrix = pd.DataFrame(ratios)
    
    # Final output
    print(f"Ratio Matrix:\n\n{ratio_matrix.head()}")
