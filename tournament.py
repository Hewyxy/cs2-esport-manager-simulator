import os, time, random
from players import players, teamsList
from utils import match
tournaments = [
    {
        "Name": "IEM Katowice",
        "PrizePool": 1000000,
        "title": "IEM x",
        "Prizes": {
            1: 500000,
            2: 200000,
            3: 100000,
            4: 70000,
            5: 40000,
            6: 30000,
            7: 20000,
            8: 10000
        }
    },
    {
        "Name": "FISSURE Playgorund",
        "PrizePool": 1250000,
        "title": "FISSURE x",
        "Prizes": {
            1: 200000,
            2: 100000,
            3: 40000,
            4: 40000,
            5: 17500,
            6: 17500,
            7: 17500,
            8: 17500
        }
    },
    {
        "Name": "ESL One Cologne",
        "PrizePool": 1000000,
        "title": "ESL One x",
        "Prizes": {
            1: 500000,
            2: 200000,
            3: 100000,
            4: 70000,
            5: 40000,
            6: 30000,
            7: 20000,
            8: 10000
        }
    },
    {
        "Name": "BLAST Premier Global Final",
        "PrizePool": 1000000,
        "title": "BLAST x",
        "Prizes": {
            1: 600000,
            2: 250000,
            3: 100000,
            4: 50000,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }
    },
    {
        "Name": "DreamHack Masters",
        "PrizePool": 500000,
        "title": "DreamHack x",
        "Prizes": {
            1: 250000,
            2: 100000,
            3: 50000,
            4: 30000,
            5: 20000,
            6: 20000,
            7: 20000,
            8: 20000
        }
    },
    {
        "Name": "ESL Pro League Finals",
        "PrizePool": 750000,
        "title": "ESL Pro x",
        "Prizes": {
            1: 375000,
            2: 150000,
            3: 75000,
            4: 50000,
            5: 25000,
            6: 25000,
            7: 25000,
            8: 25000
        }
    },
    {
        "Name": "ESports World Cup",
        "PrizePool": 2000000,
        "title": "EWC x",
        "Prizes": {
            1: 1000000,
            2: 500000,
            3: 150000,
            4: 100000,
            5: 50000,
            6: 30000,
            7: 20000,
            8: 10000
        }
    },
    {
        "Name": "PGL Major",
        "PrizePool": 1500000,
        "title": "Major x",
        "Prizes": {
            1: 750000,
            2: 350000,
            3: 150000,
            4: 100000,
            5: 50000,
            6: 30000,
            7: 20000,
            8: 10000
        }
    }
]

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

def tournament(teams, tournament):
    os.system("cls")
    teams.sort(key=lambda x: x["Points"], reverse=True)
    print(tournaments[tournament]["Name"])
    input("Press Enter to continue")
    os.system("cls")
    low_qual = teams[10:]
    random.shuffle(low_qual)
    qual = teams[7:10]
    random.shuffle(qual)
    playoff = teams[:7]
    random.shuffle(playoff)

    print("Low Qualification Matches")
    print(f"\n{low_qual[0]['Name']} vs {low_qual[1]['Name']}")
    print(f"\n{low_qual[2]['Name']} vs {low_qual[3]['Name']}")
    input("\nPress Enter to continue")
    match(low_qual[0], low_qual[1], low_qual)
    match(low_qual[1], low_qual[2], low_qual)

    print("Low Qualification Matches")
    print(f"\n{low_qual[0]['Name']} vs {low_qual[1]['Name']}")
    input("\nPress Enter to continue")
    match(low_qual[0], low_qual[1], low_qual)

    transfer = low_qual.pop(0)
    qual.append(transfer)
    print("Qualification matches")
    print(f"\n{qual[0]['Name']} vs {qual[1]['Name']}")
    print(f"\n{qual[2]['Name']} vs {qual[3]['Name']}") 
    input("\nPress Enter to continue")  
    match(qual[0], qual[1], qual)
    match(qual[1], qual[2], qual)
    print("Qualification matches")
    print(f"\n{qual[0]['Name']} vs {qual[1]['Name']}")
    input("\nPress Enter to continue")
    match(qual[0], qual[1], qual)
    transfer = qual.pop(0)
    playoff.append(transfer)

    print("Play-off Matches 1/4")
    for teams in playoff:
        teams["Earing"] += tournaments[tournament]["Prizes"][8]
    print(f"\n{playoff[0]['Name']} vs {playoff[1]['Name']}")
    print(f"\n{playoff[2]['Name']} vs {playoff[3]['Name']}")
    print(f"\n{playoff[4]['Name']} vs {playoff[5]['Name']}")
    print(f"\n{playoff[6]['Name']} vs {playoff[7]['Name']}")
    input("\nPress Enter to continue")
    match(playoff[0], playoff[1], playoff)
    match(playoff[1], playoff[2], playoff)
    match(playoff[2], playoff[3], playoff)
    match(playoff[3], playoff[4], playoff)
    print("Play-off Matches Semi-final")
    for teams in playoff:
        teams["Earing"] -= tournaments[tournament]["Prizes"][8]
        teams["Earing"] += tournaments[tournament]["Prizes"][4]
    print(f"\n{playoff[0]['Name']} vs {playoff[1]['Name']}")
    print(f"\n{playoff[2]['Name']} vs {playoff[3]['Name']}")
    input("\nPress Enter to continue")
    match(playoff[0], playoff[1], playoff)
    match(playoff[1], playoff[2], playoff)
    print("Play-off Final")
    for teams in playoff:
        teams["Earing"] -= tournaments[tournament]["Prizes"][4]
        teams["Earing"] += tournaments[tournament]["Prizes"][2]
    print(f"\n{playoff[0]['Name']} vs {playoff[1]['Name']}")
    input("\nPress Enter to continue")
    match(playoff[0], playoff[1], playoff)
    for teams in playoff:
        teams["Earing"] -= tournaments[tournament]["Prizes"][2]
        teams["Earing"] += tournaments[tournament]["Prizes"][1]
        title = tournaments[tournament]["title"]
        teams["Trophys"][title] = teams["Trophys"].get(title, 0) + 1

    input("\nPress Enter to continue")
    os.system("cls")
    print(f"{playoff[0]["Name"]} is the winner of the {tournaments[tournament]["Name"]}")
    input("\nPress Enter to continue")
    os.system("cls")
