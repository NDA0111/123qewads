
# draw a bowtie

import turtle as t

t.penup()
t.goto (-350,200)
t.pendown ()
t.forward (150)
t.left (90)
t.forward (100)
t.left (90)
t.forward (150)
t.left (90)
t.forward (100)
t.penup ()
t.goto (200,200)
t.pendown ()
t.left (90)
t.forward (100)
t.left (90)
t.forward (100)
t.left (90)
t.forward (100)
t.left (90)
t.forward (100)
t.penup ()
t.goto (150,200)
t.pendown ()
t.left (180)
t.forward (100)
t.left (90)
t.forward (100)
t.left (90)
t.forward (100)
t.left (90)
t.forward (100)
t.penup ()
t.goto (-350,-200)
t.pendown ()
t.forward (100)
t.left (120)
t.forward (100)
t.left (120)
t.forward (100)
t.penup ()
t.goto (0,0)
t.pendown ()

t.fillcolor ("red")
t.begin_fill()
t.left (120)
t.forward (100)
t.left (120)
t.forward (100)
t.left (120)
t.forward (100)
t.end_fill()
t.fillcolor ("yellow")
t.begin_fill()
t.left (30)
t.forward (150)
t.left (90)
t.forward (100)
t.left (90)
t.forward (150)
t.end_fill()
t.penup ()
t.goto (200,-200)
t.pendown ()
t.pensize(7)
t.pencolor ("orange")
t.fillcolor ("green")
t.begin_fill()
t.right (90)
t.forward (100)
t.left (60)
t.forward (100)
t.left (60)
t.forward (100)
t.left (60)
t.forward (100)
t.left (60)
t.forward (100)
t.left (60)
t.forward (100)

t.end_fill ()

t.exitonclick()