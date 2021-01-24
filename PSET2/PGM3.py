# Initial variables surrounding stock
numStocks = 1000
buyPrice = 32.87
comm = 0.02
subBuyPrice = numStocks*buyPrice
commBuyPrice = subBuyPrice*comm
totalBuyPrice = subBuyPrice-commBuyPrice

# Variables after sell of stock
sellPrice = 33.92
numSold = 1000
subSellPrice = (numSold*sellPrice)
commSellPrice = subSellPrice*comm
totalSellPrice = subSellPrice-commSellPrice

# Calculate & display earnings or losses
totalProfit = totalSellPrice-totalBuyPrice
totalProfitPerc = totalSellPrice/totalBuyPrice

print(f"""
========================================
Buy Price (per share):  {buyPrice:.2f}
Amount Paid Total:      {totalBuyPrice:.2f}
Commission Paid:        {commBuyPrice:.2f}
----------------------------------------
Sell Price (per share): {sellPrice:.2f}
Amount Sold Total:      {totalSellPrice:.2f}
Commission Paid:        {commSellPrice:.2f}
----------------------------------------
Total Revenue:          {totalProfit:.2f}
Total Revenue (%):      {totalProfitPerc:.2f}
=========================================
""")
