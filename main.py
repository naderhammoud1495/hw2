import requests
from flask import Flask
import json


app = Flask(__name__)

@app.route('/<country_name>')
def countrey(country_name):


    url1 = "https://restcountries.eu/rest/v2/name/" +country_name+"?fullText=true"
    r = requests.get(url1)
    if r.status_code != 200:
        return ""+country_name +" not found in countrey list!"
    countries= ''
    json_pa = (r.json())
    countries+= "<b>Country’s Full Name:" +json_pa[0]['name']+ '<br/>'
   # print("Country’s Full Name:", json_pa[0]['name'])

    countries +="Country’s Capital :"+ json_pa[0]['capital']+'<br/>'
    countries +="Country’s Common Language:" + json_pa[0]["languages"][0]["name"] + '<br/>'

   # print("Country’s Common Language:", json_pa[0]['languages'][0]['name'])
    countries+="Country’s Currency Name:"+ json_pa[0]["currencies"][0]["name"]+ '<br/>'

   # print("Country’s Currency Name:", json_pa[0]['currencies'][0]['name'])

    cur = json_pa[0]['currencies'][0]["code"]

    url2 = "http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=" + cur
    r1 = requests.get(url2)
    json_pa2 = (r1.json())
    countries+="Country’s Currency rate (Base currency is EURO)  :"+str(json_pa2['rates'][cur])+'<br/>'

    #print("Country’s Currency rate (Base currency is EURO)  :", json_pa2['rates'][curcode])

    return (countries)

    if _name_ == "_main_":
        app.run(host='0.0.0.0' , debug=True)

