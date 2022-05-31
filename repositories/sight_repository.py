import pdb

from db.run_sql import run_sql

import repositories.city_repository as city_repository 
import repositories.country_repository as country_repository

from models.city import City
from models.sight import Sight


def save(sight):
    sql = "INSERT INTO sights (name, comment, city_id, country_id)  VALUES (?, ?, ?, ?) RETURNING *"
    values = [sight.name, sight.comment, sight.city.id, sight.country.id]
    
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight

def select_all():
    sights= []
    sql = "SELECT * FROM sights"
    results = run_sql(sql)
    
    for row in results:
        city = city_repository.select(row['city_id'])
        country = country_repository.select(row['country_id'])
        sight = Sight(row['name'], row['comment'], city, country, row['id'])
        sights.append(sight)
    return sights

def select(id):
    sight = None
    
    sql = "SELECT * FROM sights WHERE id = ?"
    values = [id]
    results = run_sql(sql,values)[0]
    
    if results is not None:
        city = city_repository.select(results['city_id'])
        country = country_repository.select(results['country_id'])
        sight = Sight(results['name'], results['comment'], city, country, results['id'])
    return sight

def update(sight):
    sql = "UPDATE sights SET (name, comment, city_id, country_id) = (?, ?, ?, ?) WHERE id = ?"
    values = [sight.name, sight.comment, sight.city.id, sight.country.id, sight.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM sights WHERE id = ?"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)