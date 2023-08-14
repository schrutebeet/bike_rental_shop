import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from src.customer import Customer

class CustomerTest(unittest.TestCase):

    @patch('builtins.input')
    def test_request_bike(self, mock_input):
        mock_input.return_value = '10'
        # create a customer
        customer = Customer()
        customer.requestBike()
        n_bikes = customer.bikes
        self.assertEqual(n_bikes, 10)

    @patch('builtins.input')
    def test_bug_request_bike(self, mock_input):
        mock_input.return_value = 'X'
        # create a customer
        customer = Customer()
        customer.requestBike()
        n_bikes = customer.bikes
        self.assertEqual(n_bikes, 0)

    def test_return_bike_tuple(self):
        artificial_datetime = datetime(2023, 8, 15, 10, 30, 0)
        # create a customer
        customer = Customer(rentalTime=artificial_datetime, rentalBasis='weekly', bikes=5)
        self.assertEqual(customer.returnBike(), ('weekly', artificial_datetime, 5))

    def test_bug_return_bike_tuple(self):
        artificial_datetime = datetime(2023, 8, 15, 10, 30, 0)
        # create a customer
        customer = Customer(rentalTime=artificial_datetime, rentalBasis='X', bikes=5)
        self.assertEqual(customer.returnBike(), (0, 0, 0))