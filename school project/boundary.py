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
    #amc_price = yf.download(tickers='AMC', period='1m', interval='1m')
    #gme_price = yf.download(tickers='GME', period='1m', interval='1m')
    #clov_price = yf.download(tickers='CLOV', period='1m', interval='1m')
    #wish_price = yf.download(tickers='WISH', period='1m', interval='1m')
    #wkhs_price = yf.download(tickers='WKHS', period='1m', interval='1m')
    #bbby_price = yf.download(tickers='BBBY', period='1m', interval='1m')
    #bb_price = yf.download(tickers='BB', period='1m', interval='1m')

    #print(amc_price, gme_price, clov_price)

#exception to prevent value errors
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
    if age >= 122 or age <= 0:
        print("thats not possible, tell us your real age!")
        ammount()
        break
    else: 
        continue
    

    if age == 16 or age > 16:
        while stocks != "done":
            stocks = input("\nWhat stocks would you like to buy?\nAMC $53.27\nGME $220.40\nCLOV $12.63\nWISH $13.50\nWKHS $14.54\nBBBY $28.66\nBB$13.42 \nInput ""done"" when Finished selecting\n")
            has_stock  = stocks.upper() in stocklist

            if stocks.upper() in stocklist:
                if stocks.upper() == "DONE":
                    print("\nThe stocks you picked are:", *picked_stocks, sep="\n" "\n")
                    if any("AMC" in s for s in picked_stocks):
                        promt = "\nHow much AMC would you like? ($58.27 per stock) "
                        ammount()
                        amc = n * 58.27
                        bought_stocks.append(f"AMC: {n} stocks for {amc}")
                    if any("GME" in s for s in picked_stocks):
                        promt = "\nHow much GME would you like? ($220.40 per stock) "
                        ammount()
                        gme = n * 220.40
                        bought_stocks.append(f"GME: {n} stocks for {gme}")
                    if any("CLOV" in s for s in picked_stocks):
                        promt = "\nHow much CLOV would you like? ($12.63 per stock) "
                        ammount()
                        clov = n * 12.63
                        bought_stocks.append(f"CLOV: {n} stocks for {clov}")
                    if any("WISH" in s for s in picked_stocks):
                        promt = "\nHow much WISH would you like? ($13.50 per stock) "
                        ammount()
                        wish = n * 13.50
                        bought_stocks.append(f"WISH: {n} stocks for {wish}")
                    if any("WKHS" in s for s in picked_stocks):
                        promt = "\nHow much WKHS would you like? ($14.54 per stock) "
                        ammount()
                        wkhs = n * 14.54
                        bought_stocks.append(f"WKHS: {n} stocks for {wkhs}")
                    if any("BBBY" in s for s in picked_stocks):
                        promt = "\nHow much BBBY would you like? ($28.66 per stock) "
                        ammount()
                        bbby = n * 28.66
                        bought_stocks.append(f"BBBY: {n} stocks for {bbby}")
                    if any("BB" in s for s in picked_stocks):
                        promt = "\nHow much BB would you like? ($13.42 per stock) "
                        ammount()
                        bb = n * 13.42
                        bought_stocks.append(f"BB: {n} stocks for {bb}")
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