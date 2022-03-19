from estate import Purchasable, Rental, Apartment, House


class ApartmentPurchasable(Purchasable, Apartment):

    @classmethod
    def prompt(cls):
        result = Apartment.prompt()
        result.update(Purchasable.prompt())
        return result


class ApartmentRental(Rental, Apartment):
    @classmethod
    def prompt(cls):
        result = Apartment.prompt()
        result.update(Rental.prompt())
        return result


class HousePurchasable(Purchasable, House):
    @classmethod
    def prompt(cls):
        result = House.prompt()
        result.update(Purchasable.prompt())
        return result


class HouseRental(Rental, House):
    @classmethod
    def prompt(cls):
        result = House.prompt()
        result.update(Rental.prompt())
        return result
