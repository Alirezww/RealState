class BaseProperty:
    def __init__(self, area, room_numbers, parking, address, **kwargs):
        super().__init__(**kwargs)
        self.area = area
        self.room_numbers = room_numbers
        self.parking = parking
        self.address = address

    @classmethod
    def prompt(cls):
        area = input('PLease enter area : ')
        room_numbers = input('PLease enter room_numbers : ')
        parking = input('PLease enter parking : ')
        address = input('PLease enter address : ')
        result = {
            'area': area, 'room_numbers': room_numbers, 'parking': parking, 'address': address
        }
        return result


class House(BaseProperty):
    def __init__(self, pool, yard, **kwargs):
        super().__init__(**kwargs)
        self.pool = pool
        self.yard = yard

    @classmethod
    def prompt(cls):
        pool = input('Has a pool?')
        yard = input('Has a yard?')
        result = {
            'pool': pool, 'yard': yard
        }
        result.update(BaseProperty.prompt())
        return result


class Apartment(BaseProperty):
    def __init__(self, floor, elevator, balcony, **kwargs):
        super().__init__(**kwargs)
        self.floor = floor
        self.elevator = elevator
        self.balcony = balcony

    @classmethod
    def prompt(cls):
        floor = input('Has a floor? ')
        elevator = input('Has a elevator? ')
        balcony = input('Has a balcony? ')
        result = {
            'floor': floor, 'elevator': elevator, 'balcony': balcony
        }
        result.update(BaseProperty.prompt())
        return result


class Rental:
    def __init__(self, pre_paid, monthly_cost, **kwargs):
        super().__init__(**kwargs)
        self.pre_paid = pre_paid
        self.monthly_cost = monthly_cost

    @classmethod
    def prompt(cls):
        pre_paid = input('Please enter pre paid amount ')
        monthly_cost = input('Please enter monthly amount ')
        result = {
            'pre_paid': pre_paid, 'monthly_cost': monthly_cost
        }
        return result


class Purchasable:
    def __init__(self, cost, **kwargs):
        super().__init__(**kwargs)
        self.cost = cost

    @classmethod
    def prompt(cls):
        cost = input('Please enter cost ')
        result = {
            'cost': cost
        }
        return result
