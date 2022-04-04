import random
import turtle
import time
import tkinter as tk
from tkinter import *


def play():
    delay = 0.15
    main.destroy()
    pencere = turtle.Screen()

    pencere.title('Yılan Oyunu')
    pencere.bgcolor('#6C757D')
    pencere.setup(width=600, height=620,startx=500,starty=200)
    pencere.tracer(0)
    pencere.bgpic("back.png")
    kafa = turtle.Turtle()
    kafa.speed(0)
    kafa.shape("square")
    kafa.color("#FFC107")
    kafa.penup()
    kafa.goto(0, 100)
    kafa.direction = "stop"

    yemek = turtle.Turtle()
    yemek.speed(0)
    yemek.shape("circle")
    yemek.color("#71F488")
    yemek.penup()
    yemek.shapesize(0.80, 0.80)
    yemek.goto(0, 0)

    kuyruklar = []
    puan = 0

    yaz = turtle.Turtle()
    yaz.speed(0)
    yaz.shape("square")
    yaz.color("#FFC107")
    yaz.penup()
    yaz.hideturtle()
    yaz.goto(0, 260)
    yaz.write("Skor: {}".format(puan), align="center", font=("Courier", 24, "bold"))

    def move():
        if kafa.direction == "up":
            y = kafa.ycor()
            kafa.sety(y + 20)
        if kafa.direction == "down":
            y = kafa.ycor()
            kafa.sety(y - 20)
        if kafa.direction == "right":
            x = kafa.xcor()
            kafa.setx(x + 20)
        if kafa.direction == "left":
            x = kafa.xcor()
            kafa.setx(x - 20)

    def go_up():
        if kafa.direction != "down":
            kafa.direction = "up"

    def go_down():
        if kafa.direction != "up":
            kafa.direction = "down"

    def go_right():
        if kafa.direction != "left":
            kafa.direction = "right"

    def go_left():
        if kafa.direction != "right":
            kafa.direction = "left"

    pencere.listen()
    pencere.onkey(go_up, "Up")
    pencere.onkey(go_down, "Down")
    pencere.onkey(go_right, "Right")
    pencere.onkey(go_left, "Left")

    while True:
        pencere.update()

        if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
            time.sleep(1)
            kafa.goto(0, 0)
            kafa.direction = "stop"

            for kuyruk in kuyruklar:
                kuyruk.goto(1000, 1000)
                kuyruklar = []

            
            yaz.clear()
            yaz.color("#DC3545")
            yaz.write("Oyun bitti. Skorun: {}".format(puan), align="center", font=("Courier", 26, "bold"))
            time.sleep(1)
            puan = 0
            yaz.clear()
            yaz.color("#FFC107")
            yaz.write("Skor: {}".format(puan), align="center", font=("Courier", 24, "bold"))
            
        if kafa.distance(yemek) < 20:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            yemek.goto(x, y)

            yeni_kuyruk = turtle.Turtle()
            yeni_kuyruk.speed(0)
            yeni_kuyruk.shape("square")
            yeni_kuyruk.color("#71F488")
            yeni_kuyruk.penup()
            kuyruklar.append(yeni_kuyruk)

            delay -= 0.001

            puan = puan + 1
            yaz.clear()
            yaz.write("Skor: {}".format(puan), align="center", font=("Courier", 24, "bold"))

        for index in range(len(kuyruklar) - 1, 0, -1):
            x = kuyruklar[index - 1].xcor()
            y = kuyruklar[index - 1].ycor()
            kuyruklar[index].goto(x, y)

        if len(kuyruklar) > 0:
            x = kafa.xcor()
            y = kafa.ycor()
            kuyruklar[0].goto(x, y)

        move()

        for segment in kuyruklar:
            if segment.distance(kafa) < 20:
                time.sleep(1)
                kafa.goto(0, 0)
                kafa.direction = "stop"
                for segment in kuyruklar:
                    segment.goto(1000, 1000)
                kuyruklar = []
                puan = 0
                yaz.clear()
                yaz.write('Skor: {}'.format(puan), align='center', font=('Courier', 24, 'bold'))
                hiz = 0.15

        time.sleep(delay)


main = tk.Tk()
main.geometry("600x620+500+200")
main.config(bg="#6C757D")
main.title("Snake Game")

from PIL import ImageTk, Image
img = ImageTk.PhotoImage(Image.open("back2.png"))  
Label(image=img).pack()

btn = Button(text="Oyna", bg="#71F488",fg="#343A40",font=("Courier", 12, "bold"),borderwidth=15,command=play)
btn.place(x=261, y=160)
Label(text="Created by Yusuf Emir CAN ",width="40",fg="#343A40", font=("Courier", 10, "bold")).place(x=180,y=600)

main.mainloop()