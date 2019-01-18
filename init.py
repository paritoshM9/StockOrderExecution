import pandas as pd
from main_func import executeStock, createOutput, readStock
from stock import StockOrder


def main(filename):

    orders_input = readStock(filename)
    orders_output = executeStock(orders_input)
    #print(orders_output)
    createOutput(orders_output)

if __name__ == '__main__':
    filename = "stock.csv"
    main(filename)
