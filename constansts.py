from Profile import ApartmentRental, ApartmentPurchasable, HousePurchasable, HouseRental

SUPERVISOR_CREDENTIAL = [
    {'username': 'admin', 'password': '123'},
]
AGENTS_FILE_PATH = "C:\\Users\SALAM\PycharmProjects\Real State\\fixtures\\agents.json"

PROFILE_MAPPER = {
    ('house', 'rent'): HouseRental,
    ('house', 'purchase'): HousePurchasable,
    ('apartment', 'rent'): ApartmentRental,
    ('apartment', 'purchase'): ApartmentPurchasable,
}
