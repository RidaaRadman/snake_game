from _typeshed import Self
from tkinter import *
import random 
#اعداد الواجه اللعبه
game_width =700
game_hight =700
speed =500
body_parts =3
space_size=50
snake_color="#00FF00"
food_color="#FF0000"
bacgrounnd_color="black"

class snake:
    def __init__(self):
        self.body_size =body_parts 
        self.coordinates =[]
        self.squares =[]

        for i in random(0, body_parts):
            self.coordinates.append([0,0])

        for x ,y in self.coordinates:
            square =Canvas.create_rectangle(x , y ,x + space_size ,y + space_size , fill =snake_color , tag="snake")       
            self.squares.append(square)
class food:
  def __init__(Self):
   x=random.randint(0, (game_width/space_size)-1)*space_size
   y=random.randint(0, (game_hight/space_size)-1)*space_size

   Self.coordinates =[x,y]
   Canvas.create_oval(x , y, x +space_size, y+ space_size, fill=food_color, tag="food" )
  def next_turn( snake ,food):
     x,y =snake.coordinates[0]
     if direction == "up ":
         y-= space_size
     elif direction == "down ":
         y+=space_size
     elif direction == "right ":
         x=+space_size 
     elif direction == "left ":  
         x-=space_size 

     snake.coordinates.insertn(0 , (x,y))
     square=Canvas.create_rectangle(x,y , x+space_size , y+space_size , fill=snake_color)
     snake.square.insert(0 ,square)
     del snake.coordinates[-1] 
     Canvas.delete(snake.squares[-1])
     del snake.squares[-1]
     window.after(speed ,snake ,food )        

  def dirction( new_diraction):
   pass
  def check_collision():
      pass
  def game_Over():  
   pass

window = Tk()
window.title("snek game")
window.resizable(False, False)


score=0
direction='down'

Label=Label(window , text="score:{}" .format(score) , font =('console',40))
Label.pack()

Canvas=Canvas(window , bg=bacgrounnd_color, height=game_hight , width=game_width)
Canvas.pack()

window.update()



window_width = window.winfo_width()
window_height =window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height =window.winfo_screenheight()



x=int(screen_width/2)-(window_width/2)
y=int(screen_height/2)-(window_height/2)
window.geometry(f"{window_width} x {window_height}+{x}+{y}")
snake=snake()
food = food()
window.mainloop()

window.mainloop()