# StockOrderExecution - Coding Assignment

### Problem statement: 

A stock order is an order to buy or sell a given quantity of stocks of a specified company.
Person willing to buy or sell a stock will submit an order to a stock exchange where it is
executed against the opposite side order of the same company i.e., buy order is executed
against a sell order and vice-versa. The criteria for execution of stock orders is - they should
belong to the same company, they are opposite sides ( Buy vs Sell), and an stock order is
executed against the first available stock order. The left-over quantity, after execution, is called
remaining quantity. For example, if a buy order of quantity 10 is executed against a sell order of
quantity 4, the remaining quantity of buy and sell orders are 6 and 0, respectively. The status of
an order is OPEN if the remaining quantity is greater than zero, otherwise it is CLOSED (i.e.
remaining quantity = 0).
Your task is to implement stock order execution system which takes stock orders as input from a
CSV file, processes them and prints, as output, the status, remaining quantity of all the
executed orders.


