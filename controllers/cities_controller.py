from flask import flask, render_template, request, redirect, Blueprint

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository 

cities_blueprint = Blueprint("cities", __name__)