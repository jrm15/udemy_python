travel_list = [
    {
    'country' : 'France',
    'cities' : ['París', 'Lille', 'Dijon'],
    'visits' : 4
    },
    {
    'country' : 'Berlin',
    'cities' : ['Berlin', 'Hamburg'],
    'visits' : 2
    },
]

def add_new_country(country: str, cities: str, visits: int) -> str:
    new_country = {}
    new_country['country'] = country
    new_country['cities'] = cities
    new_country['visits'] = visits
    travel_list.append(new_country)


add_new_country('Rusia', ['Moscow', 'Saint Petersburg'], 2)
print(travel_list)