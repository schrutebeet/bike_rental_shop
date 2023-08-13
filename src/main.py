import sys
import time
from pathlib import Path

# Set PYTHONPATH to bike_rental_shop/
new_path = Path(__file__).resolve().parent.parent
sys.path.append(str(new_path))

from src.customer import Customer
from src.bikerental import BikeRental

def main():
    # Define variables
    TYPE_OF_RENTAL = 'hourly'
    INITIAL_SHOP_STOCK = 100
    SLEEPING_TIME = 5

    # Create a customer instance
    customer = Customer()
    # Define type of rental
    customer.rentalBasis = TYPE_OF_RENTAL
    # Create a rental bike shop instance
    bike_shop = BikeRental(stock=INITIAL_SHOP_STOCK)
    # print current stock for the rental shop
    bike_shop.displaystock()
    # Customer requests rental for X number of bikes (input parameter)
    bikes_requested = customer.requestBike()
    # Start rental period
    start_rental_period = bike_shop.rentBikes(customer.rentalBasis, bikes_requested)
    customer.rentalTime = start_rental_period
    if customer.rentalTime:
        # Artificially sleep code for desired amount of seconds
        time.sleep(SLEEPING_TIME)
        # After waiting time, customer returns bike(s) to rental shop
        bike_shop.returnBike(customer.returnBike())
    
if __name__=="__main__":
    main()