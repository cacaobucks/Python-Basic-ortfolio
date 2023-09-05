class Baseball_Team:
    def __init__(self, name, win, lose, draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw
    
    def calc_win_rate(self):
        return self.win / (self.win + self.lose)
        
    
    def show_team_result(self):
        print(f"{self.name:12s} {self.win:4d}{self.lose:4d}{self.draw:6d} {self.calc_win_rate():.3f}")
         
         
Giants = Baseball_Team("Giants", 77, 64, 2)
BayStars = Baseball_Team("BayStars", 71, 69, 3)
Tigers  =Baseball_Team("Tigers ", 69, 68, 6)
Carp = Baseball_Team("Carp", 70, 70, 3)
Dragons = Baseball_Team("Dragons", 68, 73, 2)
Swallows = Baseball_Team("Swallows", 59, 82, 2)


teams = [Giants,BayStars,Tigers,Carp,Dragons,Swallows]
print("team","        ","win","lose","draw","rate")



for team in teams:
    team.show_team_result()
