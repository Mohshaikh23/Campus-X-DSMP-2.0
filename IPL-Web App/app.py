from flask import Flask,render_template,request
import requests

app  = Flask(__name__)

@app.route("/")
def index():

    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['Teams']
    
    return render_template('index.html',teams=sorted(teams))

@app.route("/teamvteam")
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response1 = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response1.json()['Teams']
    
    
    response= requests.get(f'http://127.0.0.1:5000/api/team-vs-team?team1={team1}&team2={team2}')

    response = response.json()
    return render_template('index.html',response=response,teams=sorted(teams))


app.run(debug=True,port=7000)