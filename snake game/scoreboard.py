from turtle import Turtle;


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score=0
    # self.highscore=0
    with open("/Users/manoh/OneDrive/Documents/Python Scripts/snake game/file.txt") as data:
      self.highscore= int(data.read())
    self.color("white")
    self.penup()
    self.goto(0,260)    
    self.hideturtle()
    self.score_update()
    # self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

  def score_update(self):
    self.clear()
    self.write(f"Score: {self.score} High Score : {self.highscore}", align="center", font=("Courier", 24, "normal"))

  def game_over(self):
    self.goto(0,0)
    self.write("Game Over", align= "center", font=("Courier", 24, "normal"))
  
  def reset(self):
    if self.score > self.highscore:
      self.highscore = self.score
      with open("/Users/manoh/OneDrive/Documents/Python Scripts/snake game/file.txt", mode="w") as data:
        data.write(str(self.score))
    self.score=0
    self.score_update()

  def score_count(self):
    self.score +=1    
    self.score_update()
    

