import time
from src.bikerental import BikeRental
from src.customer import Customer
from datetime.datetime import now

def main():
    # Define variables
    TYPE_OF_RENTAL = 'weekly'
    INITIAL_SHOP_STOCK = 10
    SLEEPING_TIME = 10

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
    # Artificially sleep code for desired amount of seconds
    time.sleep(SLEEPING_TIME)
    # After waiting time, customer returns bike(s) to rental shop
    bike_shop.returnBike(customer.returnBike())
    
if __name__=="__main__":
    main()