from bdb import set_trace
from calendar import c
import pdb
from models import city

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country ("Scotland")
country_repository.save(country1)

country2 = Country ("Italy")
country2 =country_repository.save(country2)

city1 = City("Glasgow", country1)
city_repository.save(city1)

city2 = City("Edinburgh", country1)
city_repository.save(city2)

city3 = City("Rome", country2)
city_repository.save(city3)

city4= City("Bologna", country2)
city_repository.save(city4)

country2.mark_country_visited


list_of_cities = country_repository.cities(country1)

print(country2.id)

country_repository.select_all()

pdb.set_trace()