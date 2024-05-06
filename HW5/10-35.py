from tkinter import *
import time
import random

width = 800
height = 600
ball_radius = 20

class Ball:
    def setColor(self):
        rd = random.randint(0,5)
        if rd == 0:
            return "black"
        if rd == 1:
            return "red"
        if rd == 2:
            return "green"
        if rd == 3:
            return "blue"
        if rd == 4:
            return "yellow"
        if rd == 5:
            return "white"

    def __init__(self, canvas, speed):
        self.canvas = canvas
        rx = random.randint(50, width - 50)
        ry = random.randint(50, height - 50)
        self.id = canvas.create_oval(rx - ball_radius, ry - ball_radius, rx + ball_radius, ry + ball_radius,
                                     fill=self.setColor())
        self.speed = speed
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.canvas_width = width
        self.canvas_height = height

    def move(self):
        self.canvas.move(self.id, self.dx * self.speed, self.dy * self.speed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.dy *= -1
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.dx *= -1

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("공 튕기기")
        self.canvas = Canvas(self.window, bg='white', width=width, height=height)
        self.canvas.pack()
        frame = Frame(self.window)
        frame.pack()
        Button(frame, text='정지', command=self.stop).pack(side=LEFT)
        Button(frame, text='재시작', command=self.resume).pack(side=LEFT)
        Button(frame, text='+', command=self.add_ball).pack(side=LEFT)
        Button(frame, text='-', command=self.remove_ball).pack(side=LEFT)
        Button(frame, text='빠르게', command=self.fast).pack(side=LEFT)
        Button(frame, text='느리게', command=self.slow).pack(side=LEFT)
        self.gamespeed = 1
        self.balls = []
        self.running = True
        self.move_balls()

    def move_balls(self):
        while self.running:
            for ball in self.balls:
                ball.move()
            self.window.update()
            time.sleep(0.01)
    def stop(self):
        self.running = False
    def resume(self):
        self.running = True
        self.move_balls()
    def add_ball(self):
        ball = Ball(self.canvas, self.gamespeed)
        self.balls.append(ball)
    def remove_ball(self):
        if self.balls:
            ball = self.balls.pop()
            self.canvas.delete(ball.id)
    def fast(self):
        self.gamespeed += 0.5
        for ball in self.balls:
            ball.speed = self.gamespeed
    def slow(self):
        self.gamespeed -= 0.5
        for ball in self.balls:
            ball.speed = self.gamespeed

ML = MainGUI()
ML.window.mainloop()
