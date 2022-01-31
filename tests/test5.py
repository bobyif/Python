import turtle
turtle.setup(800,600)
board = turtle.Turtle()
 
 
circle_positions = [(-170,0,"red"),(-130,0,"green"),(-90,0,"red"),(-50,0,"green"),(-10,0,"red"), (30,0,"green"), (70,0,"red"), (110,0,"green"),(150,0,"red"), (190,0,"green")]
 
for pos in circle_positions:
  board.penup()
  board.setpos(pos[0],pos[1])
  board.pencolor(pos[2])
  board.pensize(5)
  board.pendown()
  board.circle(20)
 
turtle.done()