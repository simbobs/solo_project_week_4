from flask import Flask, render_template, request, redirect, Blueprint
from models import country

from models.city import City
from models.sight import Sight

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sights", methods = ["GET"])
def sights():
    sights = sight_repository.select_all()
    
   
    return render_template("sights/index.html", all_sights = sights)

# @sights_blueprint.route("/sights/<city_id>", methods = ["GET"])
# def sights(city_id):
#     sights = sight_repository.select_all()
#     city = city_repository.select(city_id)
#     all_sights = city_repository.sights(city)
    
#     return render_template("sights/index.html", sights = sights, all_sights = all_sights, city = city)

# # @sights_blueprint.route()



@sights_blueprint.route("/sights/new", methods = ["GET"])
def new_sight():
    
    cities = city_repository.select_all()
    sights = sight_repository.select_all()
    countries = country_repository.select_all()
    
    
    return render_template("sights/new.html", cities = cities, sights = sights, countries = countries)

@sights_blueprint.route("/sights/<id>", methods = ["GET"])
def show_sight(id):
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    sight = sight_repository.select(id)
    
    return render_template("cities/show.html", sight = sight, countries = countries, cities = cities)

@sights_blueprint.route("/sights", methods = ["POST"])
def add_sight():
    sight_name = request.form['name']
    sight_comment = request.form['comment']
    city_id = request.form ['city_id']
    country_id = request.form['country_id']
    
    city = city_repository.select(city_id)
    country = country_repository.select(country_id)
    
    new_sight = Sight(sight_name, sight_comment, city, country)
    
    sight_repository.save(new_sight)
    
    return redirect(f"/cities/{city_id}")

@sights_blueprint.route("/sights/<id>/edit", methods =["GET"])
def edit_sight(id):
    sight = sight_repository.select(id)
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    
    return render_template("sights/edit.html", sight = sight, cities = cities, countries = countries)

@sights_blueprint.route("/sights/<id>", methods = ["POST"])
def update_sight(id):
    sight_name = request.form['name']
    sight_comment = request.form['comment']
    city_id = request.form['city_id']
    country_id = request.form['country_id']
    
    city = city_repository.select(city_id)
    country = country_repository.select(country_id)
    
    updated_sight = Sight(sight_name, sight_comment, city, country, id)
    sight_repository.update(updated_sight)
    
    return redirect(f"/cities/{city_id}")
    
    ## this last route had you stumped for ages ^^
    
    ##THIS IS AN EXTENSION TOO BUT IT WORKS
@sights_blueprint.route("/sights/<id>/delete", methods = ["POST"])
def delete_sight(id):
    
    sight= sight_repository.select(id)
    sight_repository.delete(id)

    return redirect(f"/cities/{sight.city.id}")
    
    


