import time, os, random, subprocess
from save import save_game, load_game
from players import teamsList, allPlayers, teamNames, teamP
from teams import teams_fill, player_fill
from utils import roster, ranking, match, rating_upd, reshafl, player_ranking, balance
from tournament import tournament




def main():
    os.system("Cls")
    print("Welcome to CS2 manager simulator")
    time.sleep(3)
    os.system("cls")
    #loading data or creatating new one if needed
    try:
        data = load_game("saves/savegame.json")
        teams = data["Teams"]
        players = data["Players"]
        current_tournament = data["Tournament"]
        teamP = next(team for team in teams if team.get("is_user"))
        ai_teams = [team for team in teams if not team.get("is_user")]
    except FileNotFoundError:
        ai_teams = teamsList[:-1]      # Exclude player team
        teamP = teamsList[-1]          # The last team is the player team

        random.shuffle(teamNames)
        random.shuffle(allPlayers)

        teams_fill(ai_teams, allPlayers)  # Fill AI teams
        player_fill(teamP, allPlayers)           # Fill player team (teamP)

        data = {
            "Teams": teamsList,        # Save full list with filled teamP
            "Players": allPlayers,
            "Tournament": 1,
        }
        save_game(data)
        teams = teamsList
        players = allPlayers
        current_tournament = 0

    
    if teamP["Name"] == None:
        user = input("Create a name for your team: ")
        teamP["Name"] = user
        os.system('cls')
    while True:
        print("\t\tMENU")
        print("\t\t[1]Play\n\t\t[2]Team Ranking\n\t\t[3]Roster\n\t\t[4]Player Ranking\n\t\t[E]Exit")
        user = input()
        if user == "1":
            tournament(teams, current_tournament)
            current_tournament += 1
            if current_tournament == 6:
                current_tournament = 0
                balance(teams)
                save_game(data)
            data["Tournament"] = current_tournament
            rating_upd(teams)
            reshafl(teams, players)
            teams_fill(ai_teams, players) 
            player_fill(teamP, players)   
            save_game(data)
        elif user == "2":
            os.system("cls")
            ranking(teams)
            input("\n\nPress Enter to continue")
            os.system("cls")
        elif user == "3":
            os.system("cls")
            roster(teamP)
            input("\n\nPress Enter to continue")
            os.system("cls")
        elif user == "4":
            os.system("cls")
            player_ranking(teams)
            input("\n\nPress Enter to continue")
            os.system("cls")
        elif user == "e" or user == "E":
            save_game(data)
            break
        

main()