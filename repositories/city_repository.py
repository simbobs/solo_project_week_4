
import pdb

from db.run_sql import run_sql

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, visited, country_id) VALUES (?, ?, ?) RETURNING ID"
    values = [city.name, city.visited, city.country.id]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    
    for row in results:
        visited = True if results['visited'] == 1 else False
        country = country_repository.select(row['country_id']).name
        city = City(row['name'],country, visited, row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities where id = ?"
    values = [id]
    result = run_sql(sql, values)
    
    if city is not None:
        visited = True if result['visited'] == 1 else False
        country = country_repository.select(result['country_id']).name
        city = City (result['name'], country, visited, result ['id'])
    return city

def update(city):
    sql = "UPDATE cities SET ( name, visited, country_id) = ( ?, ?, ?) WHERE id = ?"
    values = [city.name, city.visited, city.country.id, city.id]
    run_sql(sql, values)
    

def delete(id):
    sql = "DELETE FROM cities WHERE id = ?"
    values = [id]
    run_sql(sql, values)



def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)
        
        
        
        
        
        
    

