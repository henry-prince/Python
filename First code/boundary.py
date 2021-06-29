#imports libarys for live price updating
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

#Sets up initial variables and lists to allow code to run
start = True
while start == True:
    stocks = ""
    stocklist = ["AMC", "GME", "CLOV", "WISH", "WKHS", "BBBY", "BB", "DONE"]
    picked_stocks = []
    bought_stocks = []
    amc = 0
    gme = 0
    clov = 0
    wish = 0
    wkhs = 0
    bbby = 0
    bb = 0
    n = 0
    amc_price = yf.download(tickers='AMC', period='1m', interval='1m')
    gme_price = yf.download(tickers='GME', period='1m', interval='1m')
    clov_price = yf.download(tickers='CLOV', period='1m', interval='1m')
    wish_price = yf.download(tickers='WISH', period='1m', interval='1m')
    wkhs_price = yf.download(tickers='WKHS', period='1m', interval='1m')
    bbby_price = yf.download(tickers='BBBY', period='1m', interval='1m')
    bb_price = yf.download(tickers='BB', period='1m', interval='1m')

    print(amc_price, gme_price, clov_price)
#exception 
    def ammount():
        global n
        while True:
            try:
                n  = float(input(promt))
                if n <= 0:
                    print("number has to be positive")
                    ammount()
                break
            except ValueError  or TypeError:
                print("that is not a number, please try again")


    promt = "How old are you?\n"
    ammount()
    age = n

    if age == 16 or age > 16:
        while stocks != "done":
            stocks = input("\nWhat stocks would you like to buy? (AMC, GME, CLOV, WISH, WKHS, BBBY, BB) \nInput ""done"" when Finished selecting\n")
            has_stock  = stocks.upper() in stocklist

            if stocks.upper() in stocklist:
                if stocks.upper() == "DONE":
                    print("\nThe stocks you picked are:", *picked_stocks, sep="\n" "\n")
                    if any("AMC" in s for s in picked_stocks):
                        promt = "\nHow much AMC would you like? "
                        ammount()
                        amc = float(n) * 58.27
                        bought_stocks.append("AMC: ${}" .format(amc))
                    if any("GME" in s for s in picked_stocks):
                        promt = "\nHow much GME would you like? "
                        ammount()
                        gme = float(n) * 220.40
                        bought_stocks.append("GME: ${}" .format(gme))
                    if any("CLOV" in s for s in picked_stocks):
                        promt = "\nHow much CLOV would you like? "
                        ammount()
                        clov = float(n) * 12.63
                        bought_stocks.append("CLOV: ${}" .format(clov))
                    if any("WISH" in s for s in picked_stocks):
                        promt = "\nHow much WISH would you like? "
                        ammount()
                        wish = float(n) * 13.50
                        bought_stocks.append("WISH: ${}" .format(wish))
                    if any("WKHS" in s for s in picked_stocks):
                        promt = "\nHow much WKHS would you like? "
                        ammount()
                        wkhs = float(n) * 14.54
                        bought_stocks.append("WKHS: ${}" ,format(wkhs))
                    if any("BBBY" in s for s in picked_stocks):
                        promt = "\nHow much BBBY would you like? "
                        ammount()
                        bbby = float(n) * 28.66
                        bought_stocks.append("BBBY: ${}" .format(bbby))
                    if any("BB" in s for s in picked_stocks):
                        promt = "\nHow much BB would you like? "
                        ammount()
                        bb = float(n) * 13.42
                        bought_stocks.append("BB: ${}" .format(bb))
                else:
                    picked_stocks.append(stocks.upper())
                    picked_stocks = [ele for ele in stocklist if ele in picked_stocks]
                    print("\nThe stocks you picked are:", *picked_stocks, sep="\n")
            else:
                print("that is not an option, try again")
        print("Your totals are:")
        print(*bought_stocks, sep=",\n")
        print("Total: $" , amc + gme + clov + wish + wkhs + bbby + bb)
    else:
        print("You are not allowed to buy stocks, sorry\n")
    again = str(input("Would you like to try again? (y/n)\n"))
    if again in ['y', 'n']:
        break
    print("That is not a valid input")
    if again == 'y':
        continue
    elif again == 'n':
        print("Thank you for playing")
        start = False