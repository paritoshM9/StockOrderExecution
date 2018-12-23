import unittest
import pandas as pd
from stock import StockOrder
from init import main
from main_func import executeStock, createOutput, readStock, order_to_tuple


class TestStock(unittest.TestCase):

    def setUp(self):
        self.order_1 = StockOrder(1,"Buy", "ABC", 10)
        self.order_2 = StockOrder(2,"Sell", "XYZ", 15)
        self.order_3 = StockOrder(3,"Sell", "ABC", 13)
        self.order_4 = StockOrder(4,"Buy", "XYZ", 10)
        self.order_5 = StockOrder(5,"Buy", "XYZ", 8)

    def tearDown(self):
        pass


    def test_execute(self):

        orders = [self.order_1, self.order_2, self.order_3, self.order_4, self.order_5 ]
        output_orders = executeStock(orders)

        self.assertEqual(self.order_1.rem_qty, 0)
        self.assertEqual(self.order_1.status, "CLOSED")
        self.assertEqual(self.order_3.rem_qty, 3)
        self.assertEqual(self.order_3.status, "OPEN")

        self.assertEqual(self.order_2.rem_qty, 0)
        self.assertEqual(self.order_2.status, "CLOSED")
        self.assertEqual(self.order_4.rem_qty, 0)
        self.assertEqual(self.order_4.status, "CLOSED")
        self.assertEqual(self.order_5.rem_qty, 3)
        self.assertEqual(self.order_5.status, "OPEN")       


    def test_readStock(self):
        filename = "stock.csv"
        orders = readStock(filename)
        self.assertGreater(len(orders), 0)
    
    def test_order_to_tuple(self):

        self.order_2.processOrder(self.order_4)
        self.order_2.processOrder(self.order_5)

        tup = order_to_tuple(self.order_2)
        self.assertTrue(isinstance(tup, tuple))
        actual_tup = (2,"Sell", "XYZ", '15,0',"CLOSED")
        self.assertTupleEqual(tup, actual_tup)

    def test_isBuy(self):
        self.assertEqual(self.order_1.isBuy(), True)
        self.assertEqual(self.order_2.isBuy(), False)

        
    def test_isSell(self):
        self.assertEqual(self.order_1.isSell(), False)
        self.assertEqual(self.order_2.isSell(), True)        
        

    def test_processOrder(self):
        self.order_2.processOrder(self.order_1)
        self.order_2.processOrder(self.order_3)
        self.order_2.processOrder(self.order_4)
        self.order_2.processOrder(self.order_5)

        self.assertEqual(self.order_2.rem_qty, 0)
        self.assertEqual(self.order_2.status, "CLOSED")
        self.assertEqual(self.order_4.rem_qty, 0)
        self.assertEqual(self.order_4.status, "CLOSED")
        self.assertEqual(self.order_5.rem_qty, 3)
        self.assertEqual(self.order_5.status, "OPEN")




        

if __name__ == '__main__':

    unittest.main()