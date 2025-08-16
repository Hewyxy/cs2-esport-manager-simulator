import random, os, time
from save import save_game, load_game
from players import teamsList, players, teamNames, teamP

teams = teamsList[:-1]
random.shuffle(teamNames)
random.shuffle(players)

def teams_fill(teamList,players):
    teamNameIndex = 0
    for team in teamList:
        if team["Name"] == None:
            team["Name"] = teamNames[teamNameIndex]
            teamNameIndex += 1
        while len(team["Players"]) < 5:
            index = random.randint(0, len(players) - 1)
            player = players.pop(index)
            player["Team"] = team["Name"]
            team["Players"].append(player)

def player_fill(teamP, players):
    while len(teamP["Players"]) < 5:
        print("\nAvailable Players:\n")
        for i, player in enumerate(reversed(players)):
            print(f"[{i + 1}] {player['Nickname']}, Rating: {player['Rating']}")

        try:
            inp = int(input("Enter the number of the player you want to buy: ")) - 1
            if 0 <= inp < len(players):
                player_index = len(players) - 1 - inp  # Since printed in reverse
                player = players.pop(player_index)
                print(f"{player['Nickname']} transferred --> {teamP['Name']}")
                player["Team"] = teamP["Name"]
                teamP["Players"].append(player)
                time.sleep(2)
                os.system("cls")
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Please enter a valid number.")


                

