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



for j in range(len(orders)):
    print(orders[j].status)







        
