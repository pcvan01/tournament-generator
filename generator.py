class Generator:
    def __init__(self):
        self.number_teams = 0
        self.name_teams = []
        self.games_played = 0
        self.final_teams = []

    def get_number_teams(self):
        while True:
            resp = input(f"Enter the number of teams in the tournament: ")
            if resp.isdigit() and int(resp) >= 2 and int(resp) <= 50:
                self.number_teams = resp
                break
            elif resp.isdigit() and int(resp) >= 2 and int(resp) > 50:
                print("Sorry, this game can only process 50 teams or less")
            else:
                print("Sorry, please enter a digit between 2 and 50")

    def get_name_teams(self):
        for i in range(1, int(self.number_teams) + 1):
            while True:
                resp = input(f"Enter the name for team #{i}: ")
                if len(resp) >= 50:
                    print(f"Sorry, please enter a team name with less than 50 characters")
                else:
                    self.name_teams.append(resp)
                    break

    def get_number_games(self):
        while True:
            resp = input(f"Enter the number of games played by each team: ")
            if resp.isdigit() and int(resp) >= int(self.number_teams) - 1:
                self.games_played = resp
                break
            elif resp.isdigit() and int(resp) < int(self.number_teams) - 1:
                print(f"Sorry, in this league every team would have played each other team at least once. \n" +
                      f"Please enter a valid number of games")
            else:
                print("Sorry, please enter a valid digit")

    def get_number_wins(self):
        for item in self.name_teams:
            while True:
                resp = input(f"Enter the number of wins team {item} had: ")
                if resp.isdigit() and int(resp) <= int(self.games_played) and int(resp) >= 0:
                    self.final_teams.append((item, int(resp)))
                    break
                else:
                    print(f"Sorry, please enter a valid integer number.\n" +
                          f"The number of wins can range from 0 - {self.games_played}")

    def get_schedule(self):
        self.final_teams.sort(key=lambda x: x[1])
        print("\nThe first round tournament pairings are:")
        if len(self.final_teams) % 2 == 1:
            print(f"    {self.final_teams[-1][0]} has a buy")
            self.final_teams.pop()
        ii = 1
        for jj in range(0, len(self.final_teams)//2):
            print(f"    {self.final_teams[ii*-1][0]} plays {self.final_teams[ii-1][0]}")
            ii += 1

