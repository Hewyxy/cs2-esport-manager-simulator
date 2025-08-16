from players import players, teamsList
import random, time, os
from save import load_game

data = {
    "Teams" : teamsList,
    "Players": players,
    "Tournament": 0,
}


player0 = {"Nickname" : players[43]["Nickname"],"Rating": players[43]["Rating"], "Kills" : 25, "Deaths": 24}
player1 = {"Nickname" : players[52]["Nickname"],"Rating": players[52]["Rating"], "Kills" : 0, "Deaths": 0}
player2 = {"Nickname" : players[70]["Nickname"],"Rating": players[70]["Rating"], "Kills" :0, "Deaths": 0}
player3 = {"Nickname" : players[35]["Nickname"],"Rating": players[35]["Rating"], "Kills" : 0, "Deaths": 0}
player4 = {"Nickname" : players[25]["Nickname"],"Rating": players[25]["Rating"], "Kills" : 0, "Deaths": 0}
player5 = {"Nickname" : players[16]["Nickname"],"Rating": players[16]["Rating"], "Kills" : 0, "Deaths": 0}
player6 = {"Nickname" : players[48]["Nickname"],"Rating": players[48]["Rating"], "Kills" : 0, "Deaths": 0}
player7 = {"Nickname" : players[72]["Nickname"],"Rating": players[72]["Rating"], "Kills" : 0, "Deaths": 0}
player8 = {"Nickname" : players[50]["Nickname"],"Rating": players[50]["Rating"], "Kills" : 0, "Deaths": 0}
player9 = {"Nickname" : players[12]["Nickname"],"Rating": players[12]["Rating"], "Kills" : 0, "Deaths": 0}

team1 = {"Name": "Team 1", "Points": 0, "Earing": 0, "Players": [player0,player1,player3,player4,player2], "Wins": 0, "Losses": 0, "Trophys": ["Major Winner"], "Score": 4}
team2 = {"Name": "Team 2", "Points": 0, "Earing": 0, "Players": [player5,player6,player7,player8,player9], "Wins": 0, "Losses": 0, "Trophys": [], "Score": 13}

teams = [team1, team2]

def grid(team1, team2):
    team1["Players"].sort(key=lambda x: x["Kills"], reverse=True)
    team2["Players"].sort(key=lambda x: x["Kills"], reverse=True)

    print(team1["Name"])
    for player in team1["Players"]:
        print(player["Nickname"], end=" ")
        nicklen = len(player["Nickname"])
        while nicklen < 10:
            print(" ", end="")
            nicklen += 1
        deaths = player["Deaths"]
        kd = player["Kills"] / deaths if deaths != 0 else player["Kills"]
        print(f'{player["Kills"]} / {player["Deaths"]} / {kd:.2f}')

    print(f"\n{team2["Name"]}")
    for player in team2["Players"]:
        print(player["Nickname"], end=" ")
        nicklen = len(player["Nickname"])
        while nicklen < 10:
            print(" ", end="")
            nicklen += 1
        deaths = player["Deaths"]
        kd = player["Kills"] / deaths if deaths != 0 else player["Kills"]
        print(f'{player["Kills"]} / {player["Deaths"]} / {kd:.2f}')


def roster(team):
    time.sleep(1)
    avg_rating = sum(p["Rating"] for p in team["Players"]) / len(team["Players"])
    if team['Losses'] == 0:
        winrate = "N/A"
    else:
        winrate = f"{(team['Wins'] / (team['Wins'] + team['Losses'])) * 100:.1f}%"

    print(f"[{team['Points']}] {team['Name']} ({avg_rating:.2f})\t${team['Earing']}\t  Winrate:{winrate}")

    if team["Trophys"]:
        print("Trophies:", ", ".join(f"{key} {value}" for key, value in team["Trophys"].items()))
    else:
        print("Trophies: None")

    print("Roster:", end=" ")
    for p in team["Players"]:
        print(f"{p['Nickname']}({p['Rating']:.2f})", end="\t")
    print("\n")

def ranking(teamList):
    teamList.sort(key=lambda x: x["Points"], reverse=True)
    place = 1
    for team in teamList:
        print(f"\n\n{place}", end=". ")
        roster(team)
        place+=1

def player_ranking(teamList):
    all_players = []
    for team in teamList:
        for player in team["Players"]:
            player["Team"] = team["Name"]  # Ensure player's current team is known
            all_players.append(player)

    all_players.sort(key=lambda x: x["Rating"], reverse=True)

    print("\n\n--- Player Rankings ---\n")
    for i, player in enumerate(all_players, start=1):
        name = player["Nickname"]
        rating = player.get("Rating", 0)
        team = player.get("Team", "Free Agent")
        print(f"{i}. {name} | Rating: {rating} | Team: {team}")


def match(team1, team2, list):
    os.system("cls")
    roster(team1)
    print("\n\n\t\t\t\tVS\n")
    roster(team2)
    input("\nPress Enter to continue")
    os.system("cls")
    teamA = team1
     
    teamB = team2
       
    mapA = 0
    mapB = 0
    while mapA < 2 and mapB < 2:
        scoreA = 0
        scoreB = 0
        round_num = 1
        tempA = [{"Nickname": p["Nickname"], "Rating": p["Rating"], "Kills": 0, "Deaths": 0} for p in teamA["Players"]]
        tempB = [{"Nickname": p["Nickname"], "Rating": p["Rating"], "Kills": 0, "Deaths": 0} for p in teamB["Players"]]
        #print(f"Maps Score {mapA}:{mapB}")
        max_score = 13
        while scoreA < max_score and scoreB < max_score:
            gameRosterA = tempA.copy()
            gameRosterB = tempB.copy()
            random.shuffle(gameRosterA)
            random.shuffle(gameRosterB)
            while gameRosterA and gameRosterB:
                if random.randint(0, int(gameRosterA[0]["Rating"]*100)) > random.randint(0, int(gameRosterB[0]["Rating"]*100)):
                    gameRosterA[0]["Kills"] += 1
                    gameRosterB[0]["Deaths"] += 1
                    gameRosterB.pop(0)
                else:
                    gameRosterB[0]["Kills"] += 1
                    gameRosterA[0]["Deaths"] += 1
                    gameRosterA.pop(0)
            if gameRosterA:
                scoreA += 1
            else:
                scoreB += 1
            round_num +=1
            if (scoreA == max_score - 1) and (scoreB == max_score - 1):
                max_score += 4
        print(f"\t\t\t{scoreA}:{scoreB}")
        grid({"Name": teamA["Name"], "Players": tempA},{"Name": teamB["Name"], "Players": tempB})

        for temp_player in tempA:
            for main_player in teamA["Players"]:
                if main_player["Nickname"] == temp_player["Nickname"]:
                    main_player["Kills"] += temp_player["Kills"]
                    main_player["Deaths"] += temp_player["Deaths"]
                    break

        for temp_player in tempB:
            for main_player in teamB["Players"]:
                if main_player["Nickname"] == temp_player["Nickname"]:
                    main_player["Kills"] += temp_player["Kills"]
                    main_player["Deaths"] += temp_player["Deaths"]
                    break
        input("\nPress Enter to Continue")
        if scoreA > scoreB:
            mapA += 1
            team1["Wins"] += 1
            team2["Losses"] +=1
        else:
            team2["Wins"] += 1
            team1["Losses"] +=1
            mapB += 1
    if mapA > mapB:
        os.system("cls")
        print(f'{teamA["Name"]} wins against {teamB["Name"]} with the score {mapA}:{mapB}!')
        team1["Points"] += 10
        if team2["Points"] == 0:
            team2["Points"] = 0
        else:
            team2["Points"] -= 5
        list.remove(team2)
        input("\nPress Enter to Continue")
        os.system("cls")
    else:
        print(f'{teamB["Name"]} wins against {teamA["Name"]} with the score {mapB}:{mapA}!')
        team2["Points"] += 10
        if team1["Points"] == 0:
            team1["Points"] = 0
        else:
            team1["Points"] -= 5
        list.remove(team1)
        input("\nPress Enter to Continue")
        os.system("cls")
    

def rating_upd(teams):
    for team in teams:
        for player in team["Players"]:
            if player["Kills"] == 0:
                player["Rating"] = player["Rating"]
            else:
                player["Rating"] = (player["Kills"] / player["Deaths"])
                player["Rating"] = round(player["Rating"],2)
            if player["Rating"] > 2:
                player["Rating"] = 2


def reshafl(teams, players):
    for team in teams:
        if random.randint(1, 2) == 1:
            print(f"\n\n{team['Name']} is going to have some reshuffles")
            roll = random.randint(1, 100)
            if roll <= 40:
                num = 1
            elif roll <= 70:
                num = 2
            elif roll <= 85:
                num = 3
                team["Points"] = 0
            elif roll <= 95:
                num = 4
                team["Points"] = 0
            else:
                num = 5
                team["Points"] = 0
            while num > 0 and team["Players"]:
                time.sleep(1)
                reshaflPlayer = random.choice(team["Players"])
                reasons = [
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} as his contract expired.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} due to lack of competitive results.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} following internal disagreements.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} due to recent underperformance.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} due to personal reasons.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} as part of a major roster overhaul.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} to make space for new talent.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} following disciplinary issues.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} after role conflicts with teammates.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} due to poor team synergy.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} after missing too many practices.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} at the coach’s request.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} due to player burnout.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} after failing to qualify for playoffs.",
                f"{reshaflPlayer['Nickname']} is kicked from {team['Name']} because of financial restructuring."
                ]
                print(random.choice(reasons))
                time.sleep(1)
                players.append(reshaflPlayer)
                team["Players"].remove(reshaflPlayer)
                num -= 1
        else:
            print(f"\n\nNo reshuffles for {team['Name']}")
            time.sleep(1)

def balance(teams):
    for team in teams:
        team["Wins"] = 0
        team["Losses"] = 0
        for player in team["Players"]:
            # Случайное изменение рейтинга 
            if player["Rating"] >= 1.5:
                delta = round(random.uniform(-0.50, 0.15), 2)
            elif player["Rating"] <= 0.75:
                delta = round(random.uniform(0.25, 0.45), 2)
            else:
                delta = round(random.uniform(-0.25, 0.25), 2)
            player["Rating"] += delta
            # Ограничим рейтинг в пределах 0.50 - 2.00
            player["Rating"] = round(min(max(player["Rating"], 0.50), 2.00), 2)
            # Обновим статистику
            player["Kills"] = int(player["Rating"] * 100)
            player["Deaths"] = 100
    print("New season Begins!")
    time.sleep(2)
    os.system("cls")