import pandas as pd
from stock import StockOrder


#------------------------------------------------------------------------------
""" Utility functions for implementing queue using list """

def deque(lis):
    return lis[1:]

def isEmpty(lis):
    return len(lis)==0

def front(lis):
    return lis[0]
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
""" This function will update the stock quantities of a particular company, by getting the sell and buy queues of the given company
    The stock orders which came first in the queue will be processed first and closed orders (order with 0 remaining quantity ) will
    be dequed from the queues . This process is repeated until both the queues are empty """

def processOrder(orders, buy_q, sell_q):

    while(not (isEmpty(buy_q) or isEmpty(sell_q))):

        """ We will simply compare the first items in the 'Buy' queue and 'Sell' queue and compare their quantities, the one with smaller
            quantity will be converted to 0 , and that order status is updated as CLOSED and that order is dequed from the list , whereas
            the one having larger quantity will be updated by subtracting the smaller quantity from it """
        
        if(buy_q[0][0] > sell_q[0][0]):

            
            buy_q[0][0] -= sell_q[0][0]
            sell_q[0][0] = 0
            ind_sell = sell_q[0][1]
            orders[ind_sell].rem_qty = 0
            orders[ind_sell].status = "CLOSED"

            sell_q = deque(sell_q)
            ind_buy = buy_q[0][1]
            orders[ind_buy].rem_qty = buy_q[0][0]
            
        elif( buy_q[0][0] < sell_q[0][0] ):
            
            sell_q[0][0] -= buy_q[0][0]
            buy_q[0][0] = 0
            ind_buy = buy_q[0][1]
            orders[ind_buy].rem_qty = 0
            orders[ind_buy].status = "CLOSED"

            buy_q = deque(buy_q)
            ind_sell = sell_q[0][1]
            orders[ind_sell].rem_qty = sell_q[0][0]
            

        else:

            sell_q[0][0] = 0
            buy_q[0][0] = 0
            ind_buy = buy_q[0][1]
            orders[ind_buy].rem_qty = 0
            orders[ind_buy].status = "CLOSED"

            buy_q = deque(buy_q)
            ind_sell = sell_q[0][1]
            orders[ind_sell].rem_qty = 0
            orders[ind_sell].status = "CLOSED"

            sell_q = deque(sell_q)

    while(isEmpty(buy_q) == False):
        frnt = front(buy_q)
        ind = frnt[1]
        qty = frnt[0]
        orders[ind].rem_qty = qty
        buy_q = deque(buy_q)
        
    while(isEmpty(sell_q) == False):
        frnt = front(sell_q)
        ind = frnt[1]
        qty = frnt[0]
        orders[ind].rem_qty = qty
        sell_q = deque(sell_q)

    return orders
    
        
            


            
            
        


# --------------------------------------------------------------------------------------------------


def executeStock(orders):

    """ This function generates a nested dictionary, with Company name as the keys and Their buy and sell stocks
    are stored in a QUEUE in this format [quantity, position_in_orders_list] . In the given question, dictionary
    generated will be as follows:
    {'ABC': {'Buy': [[10, 0]], 'Sell': [[13, 2]]}, 'XYZ': {'Buy': [[10, 3], [8, 4]], 'Sell': [[15, 1]]}}
    Finally we run processOrder function on each company with their buy and sell QUEUES and updated order list is generated
    """
    
    company_dict = {}
    for i in range(len(orders)):
        if(orders[i].company not in company_dict.keys()):
            company_dict[orders[i].company] = {"Buy":[],"Sell":[]}
        company_dict[orders[i].company][orders[i].side].append([orders[i].init_qty,i])
            
    for company in company_dict.keys():
        orders = processOrder(orders, company_dict[company]["Buy"], company_dict[company]["Sell"])

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


