import pdb

from db.run_sql import run_sql

from models.city import City
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name, visited) VALUES (?, ?) RETURNING id"
    values = [country.name, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    
    for row in results:
        visited = True if row['visited'] == 1 else False
        country = Country(row['name'], visited, row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if country is not None:
        visited = True if result['visited'] == 1 else False
        country = Country(result['name'], visited, result['id'])
    return country

def update(country):
    sql = "UPDATE countries SET (name, visited) = (?, ?) WHERE id = ?"
    values = [country.name, country.visited, country.id]
    run_sql(sql, values)

def cities(country):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = ?"
    values = [country.id]
    results = run_sql(sql, values)
    
    for row in results:
        visited = True if row['visited'] == 1 else False
        city = City(row['name'], country.name, visited, row['id'])
        cities.append(city)
    return cities

def delete(id):
    sql = "DELETE FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)
        