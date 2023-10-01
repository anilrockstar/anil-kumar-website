from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

tech_skills =[
  "Python","SQL","HTML","CSS","JavaScript"
]
def weather_data():
  url = "https://api.weatherapi.com/v1/current.json?key=433cf5b0f8d74973ab3195705233009&q=Hyderabad"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data

@app.route("/")
def hello_world():
  json_data = weather_data()
  return render_template('home.html',skills=tech_skills,weather=json_data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)