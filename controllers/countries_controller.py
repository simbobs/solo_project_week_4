from flask import Flask, render_template, request, redirect, Blueprint
from models import country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository 

from models.country import Country

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/<id>", methods = ['GET'])
def show_country(id):
    country = country_repository.select(id)
    all_cities = country_repository.cities(country)
    
    return render_template("countries/show.html", country = country, all_cities = all_cities)

@countries_blueprint.route("/countries/new", methods = ["GET"])
def new_country():
    countries = country_repository.select_all()
    return render_template ("countries/new.html", all_countries = countries)

@countries_blueprint.route("/countries", methods = ["POST"])
def add_country():
    country_name = request.form['name']
    country_visited = bool(int(request.form['visited']))
    
    new_country = Country(country_name, country_visited)
    country_repository.save(new_country)
    
    return redirect("/countries")
    
    