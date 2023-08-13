import datetime

class BikeRental:

    HOURLY_DATE = 5
    DAILY_RATE = 20
    WEEKLY_RATE = 60

    def __init__(self, stock=0) -> None:
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock=stock

    def displaystock(self) -> int:
        """
        Displays the bikes currently available for rent in the shop.
        """
        print(f'We currently have {self.stock} bikes available to rent.')
        return self.stock

    def rentBikes(self, rentalBasis, n_bikes):
        rent_option = {
                        'hourly':self.rentBikeOnHourlyBasis,
                        'daily': self.rentBikeOnDailyBasis,
                        'weekly': self.rentBikeOnWeeklyBasis,
                      }
        return rent_option[rentalBasis](n_bikes)

    def rentBikeOnHourlyBasis(self, n_bikes) -> any:
        """
        Rents a bike on hourly basis to a customer.
        """
        self._check_stock_availability(n_bikes)
        # Run the action if no issues found
        now = datetime.datetime.now()
        print(f"You have rented {n_bikes} bike(s) on hourly basis today at {now.hour} hours.")
        print("You will be charged $5 for each hour per bike.")
        print("We hope that you enjoy our service")
        self.stock -= n_bikes
        return now
        
    def rentBikeOnDailyBasis(self, n_bikes) -> any:
        """
        Rents a bike on a daily basis to a customer.
        """
        self._check_stock_availability(n_bikes)
        # Run the action if no issues found
        now = datetime.datetime.now()                      
        print(f"You have rented {n_bikes} bike(s) on daily basis today at {now.hour} hours.")
        print("You will be charged $20 for each day per bike.")
        print("We hope that you enjoy our service.")
        self.stock -= n_bikes
        return now
    
    def rentBikeOnWeeklyBasis(self, n_bikes) -> any:
        self._check_stock_availability(n_bikes)
        # Run the action if no issues found
        now = datetime.datetime.now()                      
        print(f"You have rented {n_bikes} bike(s) on weekly basis today at {now.hour} hours.")
        print("You will be charged $60 for each week per bike.")
        print("We hope that you enjoy our service.")
        self.stock -= n_bikes
        return now

    def _check_stock_availability(self, n_bikes):
        """
        Internal checking used for stopping renting process in case of error.
        """
        # Halt process if number of bikes is zero or negative
        if n_bikes <= 0:
            print('Number of bikes should be positive!')
            return None
        # Halt process if number of bikes is lower than the amount 
        # available at the store
        if n_bikes > self.stock:
            print(f'Sorry! We have currently {self.stock} bikes available to rent.')
            return None
        
    def returnBike(self, request):
        """
        Takes as input a tuple with three elements:
            - rentalTime
            - rentalBasis
            - numOfBikes
        """
        # extract tuple
        rentalTime, rentalBasis, numOfBikes = request
        # Issue bill only if all alements in tuple are non-null
        # and comply with their data types
        if isinstance(rentalTime, datetime.datetime) and isinstance(numOfBikes, int) and numOfBikes > 0 and rentalBasis in ('hourly', 'daily', 'weekly'):
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            # compute bill depending on rental basis
            func_name = 'calc_bill_' + rentalBasis
            # Concatenate the function name with strings and call it
            bill = func_name(rentalPeriod, numOfBikes)
            print(f'The total amount to be paid is ${bill}')
        else:
            print('Input parameters must follow these rules:')
            print('    - rentalTime: datetime compliant with the "datetime" package')
            print('    - rentalBasis: needs to be "hourly", "daily" or "weekly"')
            print('    - numOfBikes: needs to be a positive integer number, i.e., 1, 2, 3, ..')
            return None
            
    def calc_bill_hourly(self, rentalPeriod, numOfBikes):
        bill = round((rentalPeriod.seconds / 3600) * self.HOUR_RATE * numOfBikes , 2)
        # check for family discount
        bill = self._family_discount(numOfBikes, bill)
        return bill
    
    def calc_bill_daily(self, rentalPeriod, numOfBikes):
        bill = round(rentalPeriod.days * self.DAILY_RATE * numOfBikes , 2)
        # check for family discount
        bill = self._family_discount(numOfBikes, bill)
        return bill

    def calc_bill_weekly(self, rentalPeriod, numOfBikes):
        bill = round((rentalPeriod.days / 3600) * self.WEEKLY_RATE * numOfBikes , 2)
        # check for family discount
        bill = self._family_discount(numOfBikes, bill)
        return bill
    
    def _family_discount(self, numOfBikes, bill):
        if numOfBikes >= 4:
            print('You are eligible for a family discount! 30% will be deducted from your bill')
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            return bill * 0.7
        else:
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            return bill
    