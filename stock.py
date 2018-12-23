class StockOrder:

    def __init__(self, stockId, side, company, qty):

        self.side = side
        self.init_qty = qty
        self.rem_qty = qty 
        self.company = company
        self.id = stockId
        self.status = "OPEN"

    def isBuy(self):
        return self.side == "Buy"

    def isSell(self):
        return self.side == "Sell"


    def processOrder(self, order2):

        if(self.rem_qty == 0):
            self.status = "CLOSED"
            return

        if(self.company != order2.company):
            return

        if((self.isBuy() and order2.isSell()) or (self.isSell() and order2.isBuy())):

            if(self.rem_qty > order2.rem_qty):
                self.rem_qty = self.rem_qty - order2.rem_qty
                order2.rem_qty = 0
                order2.status = "CLOSED"

            else:
                order2.rem_qty =  order2.rem_qty - self.rem_qty
                self.rem_qty = 0
                self.status = "CLOSED"
                
""" The below function is used to convert StockOrder object into 
    a tuple containing output values, which will be further
    converted into dataframe """

def order_to_tuple(stock_order):

    tup = (stock_order.id, stock_order.side, stock_order.company)
    temp_tup = (','.join(map(str,(stock_order.init_qty, stock_order.rem_qty))), stock_order.status)
    tup3 = tup + temp_tup

    return tup3

import pandas as pd 


df = pd.read_csv('D://OneDrive//Desktop//stock.csv')
#print(df.head())

orders = [] # This list will contain all the stockorders
for i in range(len(df)):
    #print(df['Side'][i])
    
    stockO = StockOrder(df['Stock Id'][i], df['Side'][i], df['Company'][i], df['Quantity'][i])
    orders.append(stockO)

for i in range(len(df)-1):
    for j in range(i+1, len(df)):
        orders[i].processOrder(orders[j])



#for j in range(len(df)):
data = df.iloc[0,0:4].values
#print(data, len(data))

data = []
#print(order_to_tuple(orders[0]))
for i in range(len(orders)):
    temp_tup = order_to_tuple(orders[i])
    data.append(temp_tup)

labels = ["StockId", "Side", "Company", "Quantity", "Status"]
output_df = pd.DataFrame.from_records(data, columns = labels)

#print(output_df.head())
output_df.to_csv('output.csv')




        
