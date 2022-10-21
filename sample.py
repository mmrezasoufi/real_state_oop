from random import choice
from user import User
from region import Region
from estate import Apartment
from advertisment import ApartmentSell, HouseSell, ApartmentRent, HouseRent

FIRST_NAME = ['Ali', 'Hosein', 'Reza', 'Mohammad']
LAST_NAME = ['Aliii', 'Hoseini', 'Rezai', 'Mohammadi']
MOBILES = ['0912', '0933', '0936', '0918']


def create_samples():
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)


    reg1 = Region('Tehpars')
    reg2 = Region('Ozgol')
    apt1 = Apartment(
        has_elevator=True, has_parking=False, floor=2, user=User.objects_list[0],
        built_year=1399, region=reg1, area=100, rooms_count=3, address='tehpars, parvin ...'
    )

    apartment_sell = ApartmentSell(
        has_elevator=True, has_parking=False, floor=2, user=User.objects_list[0],
        built_year=1399, region=reg1, area=100, rooms_count=3, address='tehpars, parvin ...',
        price_per_meter=10, discountable=False, convertable=False
    )

    house_sell = HouseSell(
        has_yard=True, floors_count=1, user=User.objects_list[2],
        area=150, rooms_count=3, built_year=1375, region=reg1, address='Some text ...',
        price_per_meter=1200, discountable=False, convertable=True
    )

    apartment_rent = ApartmentRent(
        has_elevator=True, has_parking=False, floor=2, user=User.objects_list[0],
        built_year=1399, region=reg1, area=100, rooms_count=3, address='tehpars, parvin ...',
        initial_price=100, monthly_price=3.5
    )

    house_rent= HouseRent(
        has_yard=True, floors_count=1, user=User.objects_list[2],
        area=150, rooms_count=3, built_year=1375, region=reg1,
        address='Some text ...', initial_price=100, monthly_price=3.5
    )

    print('#'*20, "\t sample created \t", "#"*20)