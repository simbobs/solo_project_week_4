from flask import Flask, render_template, request, redirect, Blueprint
from models import city

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository 
from models.city import City
from models.sight import Sight
import repositories.sight_repository as sight_repository

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
    new_city = City(city_name, country, visited)
    
    city_repository.save(new_city)
    return redirect(f"/countries/{country_id}")

@cities_blueprint.route("/cities/<id>", methods = ["GET"])
def show_city(id):
    cities = city_repository.select_all()
    city = city_repository.select(id)
    
    # extension, add sights
    
    sights = city_repository.sights(city)
    
    return render_template("cities/show.html", cities = cities, city = city, all_sights = sights)

@cities_blueprint.route("/cities/<id>/edit", methods = ["GET"])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    
    return render_template("cities/edit.html", city = city, all_countries = countries)

@cities_blueprint.route("/cities/<id>", methods =["POST"])
def update_city(id):
    city_name = request.form['name']
    country_id = request.form['country_id']
    visited = bool(int(request.form['visited']))
    
    country = country_repository.select(country_id)
    selected_city = City(city_name, country, visited, id)
    
    city_repository.update(selected_city)
    
    return redirect("/cities")


    

@cities_blueprint.route("/cities/<id>/delete", methods = ["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")
    