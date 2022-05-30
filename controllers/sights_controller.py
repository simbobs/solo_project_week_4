from flask import Flask, render_template, request, redirect, Blueprint

from models.city import City
from models.sight import Sight

import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

sights_blueprint = Blueprint("sights", __name__)

@sights_blueprint.route("/sight/new", methods = ["GET"])
def new_sight():
    
    cities = city_repository.select_all()
    sights = sight_repository.select_all()
    countries = country_repository.select_all()
    
    
    return render_template("sights/new.html", cities = cities, sights = sights, countries = countries)

@sights_blueprint.route("/sight/new/<id>", methods = ["POST"])
def add_sight():
    sight_name = request.form['name']
    sight_comment = request.form['comment']
    city_id = request.form ['city_id']
    
    city = city_repository.select(city_id)
    
    new_sight = Sight(sight_name, sight_comment, city.name)
    
    sight_repository.save(new_sight)
    
    return redirect(f"/cities/{city_id}")