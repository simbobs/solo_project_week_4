from flask import Flask, render_template, request, redirect, Blueprint

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository 
from models.city import City

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities = cities)

# this is a get because we jsut want to get the page with the form on it
@cities_blueprint.route("/cities/new")
def new_city():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_cities = cities, all_countries = countries)

@cities_blueprint.route("/cities", methods =["POST"])
def add_city():
    city_name = request.form['name']
    country_id = request.form['country_id']
    visited = bool(int(request.form['visited']))
    
    country = country_repository.select(country_id)
    city = City(city_name, country.name, visited)
    
    city_repository.save(city)
    return redirect("/cities")
    
    