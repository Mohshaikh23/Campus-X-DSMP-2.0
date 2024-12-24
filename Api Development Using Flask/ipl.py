import numpy as np
import pandas as pd

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"

df= pd.read_csv(ipl_matches)

def teamsAPI():
    teams = list(set(list(df["Team1"]) + list(df["Team2"])))
    teams_dict = {
        "Teams":teams
    }
    return teams_dict


def team_vs_team(team1, team2):
    teams = list(set(list(df["Team1"]) + list(df["Team2"])))
    if team1 in teams and team2 in teams:
        mask = df[(df["Team1"] == team1) & (df["Team2"]== team2) | (df["Team1"]== team2) & (df["Team2"]== team1)]
    
        matches_won_team1 = mask["WinningTeam"].value_counts()[team1]
        matches_won_team2 = mask["WinningTeam"].value_counts()[team2]
        Total_matches = mask["WinningTeam"].shape[0]
        draw_matches = Total_matches - (matches_won_team1 + matches_won_team2)

        response = {"Team1":team1,
                    "Team2":team2,
                    "Total_matches":str(Total_matches),
                    team1:str(matches_won_team1),
                    team2:str(matches_won_team2),
                    "Matches Drawn":str(draw_matches)
                }
        
        return response
    
    else:
        return {"message":"Invalid Teams"}

