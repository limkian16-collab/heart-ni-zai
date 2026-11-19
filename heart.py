
from turtle import *
import math

speed(0)
bgcolor("#1E2B20") 
color("#B7D99A")
pensize(2)
hideturtle()

for i in range(600):
    t = i / 20

    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    penup()
    goto(x * 15, y * 15)
    pendown()

    if i % 10 == 0:
        write("Zai Calmada", align="center",
              font=("Arial", 8, "bold"))

done()
