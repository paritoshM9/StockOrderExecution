import pandas as pd
from stock import StockOrder

# --------------------------------------------------------------------------------------------------


""" The below function is used to convert StockOrder object into 
    a tuple containing output values, which will be further
    converted into dataframe """
def order_to_tuple(stock_order):

    tup = (stock_order.id, stock_order.side, stock_order.company)
    temp_tup = (','.join(map(str,(stock_order.init_qty, stock_order.rem_qty))), stock_order.status)
    tup3 = tup + temp_tup

    return tup3

# --------------------------------------------------------------------------------------------------
""" This function will read the input from file and create a list of StockOrder objects"""
def readStock(filename):

    df = pd.read_csv(filename)
    # This list will contain all the stockorders
    orders = [] 

    for i in range(len(df)):
        
        # Creating StockOrder objects using the df values
        stockO = StockOrder(df['Stock Id'][i], df['Side'][i], df['Company'][i], df['Quantity'][i])
        orders.append(stockO)

    return orders


# --------------------------------------------------------------------------------------------------


""" This function will take list of order objects as input and do the stock processing on all of them.
    The final output will be a list of StockOrder objects which have been executed 
    and have updated values of remaining_qty and status """ 
def executeStock(orders):

    for i in range(len(orders)-1):
        for j in range(i+1, len(orders)):

            # We will compare and execute ith order with jth order
            orders[i].processOrder(orders[j])

    return orders


# --------------------------------------------------------------------------------------------------

""" This function will take list of StockOrder objects which have been executed, and will generate the
    required output file """
def createOutput(orders):

    data = [] # This list will contain tuples containing the output values

    for i in range(len(orders)):

        # Conversion of StockOrder object into tuple of output values
        temp_tup = order_to_tuple(orders[i]) 
        data.append(temp_tup)

    labels = ["StockId", "Side", "Company", "Quantity", "Status"] 
    output_df = pd.DataFrame.from_records(data, columns = labels) 
    output_df.to_csv('output3.csv',index = False)


