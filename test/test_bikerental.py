import unittest
import datetime
from unittest.mock import patch
from freezegun import freeze_time
from src.bikerental import BikeRental

class BikeRentalTest(unittest.TestCase):

    def setUp(self) -> None:
        self.shop = BikeRental(stock=1574)

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_constructor(self):
        self.assertEqual(self.shop.stock, 1574)

    def test_display_stock(self):
        stock = self.shop.displaystock()
        self.assertEqual(stock, 1574)

    @freeze_time("2023-08-15 10:30:00")
    def test_rent_bikes(self):
        return_date = datetime.datetime(2023, 8, 15, 10, 30, 0)
        test_cases = [
            ('hourly', -100, None),
            ('hourly', 183, return_date),
            ('daily', -100, None),
            ('daily', 183, return_date),
            ('weekly', -100, None),
            ('weekly', 183, return_date)
        ]
        for rentalBasis, n_bikes, expected_result in test_cases:
            with self.subTest(rentalBasis=rentalBasis, n_bikes=n_bikes, expected_result=expected_result):
                result = self.shop.rentBikes(rentalBasis, n_bikes)
                self.assertEqual(result, expected_result)

    @freeze_time("2023-08-15 10:30:00")
    def test_rent_bike_on_hourly_basis(self):
        #What the mocked function should return under normal circumstances
        date = datetime.datetime(2023, 8, 15, 10, 30, 0)
        test_cases = [
            (100, date),
            (-100, None),
            (0, None),
            (5000, None)
        ]
        for n_bikes, expected_output in test_cases:
            with self.subTest(n_bikes=n_bikes):
                result = self.shop.rentBikeOnHourlyBasis(n_bikes)
                print(result)
                self.assertEqual(result, expected_output)

    @freeze_time("2023-08-15 10:30:00")
    def test_rent_bike_on_daily_basis(self):
        #What the mocked function should return under normal circumstances
        date = datetime.datetime(2023, 8, 15, 10, 30, 0)
        test_cases = [
            (100, date),
            (-100, None),
            (0, None),
            (5000, None)
        ]
        for n_bikes, expected_output in test_cases:
            with self.subTest(n_bikes=n_bikes):
                result = self.shop.rentBikeOnDailyBasis(n_bikes)
                print(result)
                self.assertEqual(result, expected_output)

    @freeze_time("2023-08-15 10:30:00")
    def test_rent_bike_on_weekly_basis(self):
        #What the mocked function should return under normal circumstances
        date = datetime.datetime(2023, 8, 15, 10, 30, 0)
        test_cases = [
            (100, date),
            (-100, None),
            (0, None),
            (5000, None)
        ]
        for n_bikes, expected_output in test_cases:
            with self.subTest(n_bikes=n_bikes):
                time = self.shop.rentBikeOnWeeklyBasis(n_bikes)
                self.assertEqual(time, expected_output)

    @freeze_time("2023-08-15 10:30:00")
    def test_return_bike(self):
        start_date = datetime.datetime(2023, 8, 14, 8, 30, 0)
        self.HOURLY_RATE = 5
        self.DAILY_RATE = 20
        self.WEEKLY_RATE = 60
        test_cases = [
            ('hourly', start_date, 0, None),
            ('hourly', start_date, 3, 390.0),
            ('hourly', start_date, 100, 9100.0),
            ('X', start_date, 100, None),
            ('hourly', start_date, -100, None),
            ('hourly', 'X', 100, None),
            ('daily', start_date, 0, None),
            ('daily', start_date, 3, 65.0),
            ('daily', start_date, 100, 1516.67),
            ('daily', start_date, -100, None),
            ('X', start_date, 100, None),
            ('daily', 'X', 100, None),
            ('weekly', start_date, 0, None),
            ('weekly', start_date, 3, 27.86),
            ('weekly', start_date, 100, 650.0),
            ('weekly', start_date, -100, None),
            ('X', start_date, 100, None),
            ('weekly', 'X', 100, None),
        ]
        for rentalBasis, rentalTime, numOfBikes, expected_output in test_cases:
            with self.subTest(rentalBasis=rentalBasis, rentalTime=rentalTime, numOfBikes=numOfBikes, expected_output=expected_output):
                bill = self.shop.returnBike((rentalBasis, rentalTime, numOfBikes))
                self.assertEqual(bill, expected_output)
