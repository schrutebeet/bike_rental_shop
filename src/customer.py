from dataclasses import dataclass
import datetime

@dataclass
class Customer:
    """
    Our constructor method which instantiates various customer objects.
    """
    rentalBasis: str = ''
    rentalTime: datetime.datetime = datetime.datetime.now()
    bikes: int = 0

    def requestBike(self) -> int:
        """
        Takes a request from the customer for the number of bikes.
        """
        bikes = input('How many bikes would you like to rent?: ')
        if (bikes.isdigit()) and (float(bikes) % 1 == 0) and (int(bikes) >= 1):
            self.bikes = int(bikes)
            return self.bikes
        else:
            print('Please, enter correct number of bikes to be rented.')
            return None

    def returnBike(self) -> tuple[str, datetime.datetime, int]:
        """
        Allows customer to return their bikes to the rental shop.
        """
        if self.rentalTime and self.rentalBasis and self.bikes:
            return (self.rentalBasis, self.rentalTime, self.bikes)
        else:
            return (0, 0, 0)
