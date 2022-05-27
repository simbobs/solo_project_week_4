from flask import Flask, render_template

from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint

app = Flask(__name__)
 

# app.register_blueprint(books_blueprint)

@app.route('/')
def home():
    return "Simona's first solo project"

if __name__ == '__main__':
    app.run(debug=True)

