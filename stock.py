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

    """ Below function will match two StockOrder objects and update their remaining_qty
        if they follow few conditions 
        Input: StockOrder object
        O/p : The function doesn't return anything, it just updates the values of rem_qty 
                variable of the two objects if reqd """

    def processOrder(self, order2):

        if(self.rem_qty == 0):     # If the order is already complete
            self.status = "CLOSED"
            return

        if(self.company != order2.company): # If the companies for the two orders are different
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
                

