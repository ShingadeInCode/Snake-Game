import turtle # to make game screen
import random #food randomly move on the screen 
import time   # counting,speed 
delay=0.1
sc=0 #scorecard
hs=0  # highest scorecard

#creating a body of snake
bodies=[]


#creating a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("white")
s.setup(width=600,height=600) #size of screen

#creating a head
head=turtle.Turtle() # small t is for library capital T is for class
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction=("stop")

#creating food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()#hide turtle
food.goto(150,250)
food.st()#show turtle 
food.direction=("stop")

#scoreboard
sb=turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-250,250)
sb.write("Score:0 | Highest Score:0")# to print message on screen

def moveup():
    if head.direction!="down":
       head.direction="up"

def movedown():
    if head.direction!="up":
       head.direction="down"
       
def moveleft():
    if head.direction!="right":
       head.direction="left"
       
def moveright():    
    if head.direction!="left":
       head.direction="right"
       
def movestop():
       head.direction="stop"
       
def move():
  if head.direction=="up":
       y=head.ycor()#y cordinate
       head.sety(y+20)


  if head.direction=="down":
       y=head.ycor()
       head.sety(y-20)


  if head.direction=="left":
       x=head.xcor()
       head.setx(x-20)


  if head.direction=="right":
       x=head.xcor()
       head.setx(x+20)
       
#event handlling (key mapping)
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

#mainloop
while True:
  s.update() # to update screen
    #check collision with border
  if head.xcor()>290:
     head.setx(-290)
  if head.xcor()<-290:
     head.setx(290)
  if head.ycor()>290:
     head.sety(-290)        
  if head.ycor()<-290:
     head.sety(290)
        
     # check collision with food    
  if head.distance(food)<20:
     x=random.randint(-290,290)
     y=random.randint(-290,290)
     food.goto(x,y)       
     #increase lenghth of snake
     body=turtle.Turtle()
     body.speed(0)
     body.penup()
     body.shape("square")
     body.color("green")
     bodies.append(body)

    # increase the score
     sc=sc+10
     if sc>hs:
        hs=sc
     sb.clear()
     sb.write("Score:{} | Highest Score:{}".format(sc,hs))
        # increase the speed
     delay=delay-0.001

  #move the snake body 
  for index in range(len(bodies)-1,0,-1):
     x= bodies[index-1].xcor()
     y= bodies[index-1].ycor()
     bodies[index].goto(x,y)
  if len(bodies)>0:
     x=head.xcor()
     y=head.ycor()
     bodies[0].goto(x,y)
  move()

  #check collision with snake body
  for body in bodies:
    if body.distance(head)<20:
       time.sleep(1)
       head.goto(0,0)
       head.direction="stop"
       for body in bodies:
           body.ht()
       bodies.clear()
       sc=0
       delay=0.1
       sb.clear()
       sb.write("Score:{} | Highest Score:{}".format(sc,hs))
  time.sleep(delay)
s.mainloop()
        
        












































        
