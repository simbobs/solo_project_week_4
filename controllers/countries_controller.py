from flask import Flask, render_template, request, redirect, Blueprint

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository 

countries_blueprint = Blueprint("countries", __name__)