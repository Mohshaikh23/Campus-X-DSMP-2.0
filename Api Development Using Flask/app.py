from flask import Flask,render_template,redirect,jsonify,request
import ipl
import ops
import json

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/teams")
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route("/api/team-vs-team")
def teamvteam():
    team1 = request.args.get("team1")
    team2 = request.args.get("team2")

    response = ipl.team_vs_team(team1,team2)
    print(response)
    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = ops.teamAPI(team_name)
    return response

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = ops.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = ops.bowlerAPI(bowler_name)
    return response

app.run(debug=True)