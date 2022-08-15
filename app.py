import requests
from flask import Flask, render_template, request, redirect
from models import Countries

app = Flask(__name__)

@app.route('/')
def home():
    all_countries = Countries.select()
    return render_template("index.html", countries=all_countries)



res = requests.get('https://restcountries.com/v3.1/all')
a = 0
b = 0
# for i in range(20):
#     text = res.json()
#     name = text[a]['name']['common']
#     text = res.json()
#     name_offi = text[a]['name']['official']
#     text = res.json()
#     capital = text[a]["capital"][0]
#     text = res.json()
#     region = text[a]["region"]
#     text = res.json()
#     subregion = text[a]["subregion"]
#     text = res.json()
#     population = text[b]["population"]
#     text = res.json()
#     continents = text[b]["continents"][0]
#     text = res.json()
#     timezones = text[b]["timezones"][0]
#     text = res.json()
#     flag = text[b]["flags"]["png"]
#     a+=1
#     b+=1
#     Countries.create(
#         name = name,
#         official_name = name_offi,
#         capital = capital,
#         region = region,
#         subregion = subregion,
#         population = population,
#         continents = continents,
#         timezones = timezones,
#     )
    
if __name__=="__main__":
    app.run(debug=True)

