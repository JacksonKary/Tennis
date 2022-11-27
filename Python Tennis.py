import turtle, random

print("Controls:\n'q' - lob (high, deep, looping shot with topspin)\n'e' - winner (fast, low, flat shot)\n'f' - slice (short, slow ball, low bounce with backspin)\n'space' - groundstroke (moderate speed and depth)\n'x' - exit game")

'''
Purpose: objects represents tennis balls and their position and velocity coordinates
Instance variables: self.vx - x velocity, self.vy - y velocity, self.px - x pposition, self.py - y position, self.bouncTracker - tracks number of bounces,
self.shotselection - alters path of shot
'''
class Ball(turtle.Turtle):
    def __init__(self, xpi, ypi, xvi, yvi):
        turtle.Turtle.__init__(self)
        self.vx = xvi # velocity x
        self.vy = yvi # velocity y
        self.px = xpi # position x
        self.py = ypi # position y
        self.bounceTracker = 0
        self.shape('circle')
        self.pencolor("yellow")
        self.turtlesize(0.3)
        self.shotselection = "hit"
        self.penup()
        self.setpos(self.px, self.py)
    def move(self):
        if self.shotselection == "hit":
            self.vy -= 0.981
            if self.px >= 0:
                positionTracker = "Right Side"
            if self.px < 0:
                positionTracker = "Left Side"
            self.px += self.vx
            self.py += self.vy

            if self.px >= 0 and positionTracker == "Left Side":
                self.bounceTracker = 0
            if self.px < 0 and positionTracker == "Right Side":
                self.bounceTracker = 0

            if self.py >= 0:
                self.setpos(self.px, self.py)

            if self.py < 0:
                self.setpos(self.px, (0.75 * abs(self.py)))
                self.vy = ((-self.vy) * 0.75)
                self.bounceTracker += 1
                if self.bounceTracker > 1: # ball dead - point is over
                    # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    Game.gameloop(self)
                elif self.px > 390:
                    # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    Game().gameloop(self)
                elif self.px < -390:
                    # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    Game().gameloop(self)
                    
        if self.shotselection == "lob":
            self.vy -= 1
            if self.px >= 0:
                positionTracker = "Right Side"
            if self.px < 0:
                positionTracker = "Left Side"
            self.px += self.vx
            self.py += self.vy

            if self.px >= 0 and positionTracker == "Left Side":
                self.bounceTracker = 0
            if self.px < 0 and positionTracker == "Right Side":
                self.bounceTracker = 0

            if self.py >= 0:
                self.setpos(self.px, self.py)

            if self.py < 0:
                self.setpos(self.px, (0.85 * abs(self.py)))
                self.vy = ((-self.vy) * 0.85)
                self.bounceTracker += 1
                if self.bounceTracker > 1:
                    # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    Game().gameloop(self)
                if self.px > 390:
                    # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    Game().gameloop(self)
                if self.px < -390:
                    # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    Game().gameloop(self)
        if self.shotselection == "slice":
            self.vy -= 1
            if self.px >= 0:
                positionTracker = "Right Side"
            if self.px < 0:
                positionTracker = "Left Side"
            self.px += self.vx
            self.py += self.vy

            if self.px >= 0 and positionTracker == "Left Side":
                self.bounceTracker = 0
            if self.px < 0 and positionTracker == "Right Side":
                self.bounceTracker = 0

            if self.py >= 0:
                self.setpos(self.px, self.py)

            if self.py < 0:
                self.setpos(self.px, (0.4 * abs(self.py)))
                self.vy = ((-self.vy) * 0.4)
                self.bounceTracker += 1
                if self.bounceTracker > 1:
                    self.bounceTracker = 0
                    self.px = 600
                    self.setpos(self.px, self.py)
                    Game()
                if self.px > 390:
                    self.bounceTracker = 0
                    self.px = 600
                    self.setpos(self.px, self.py)
                    Game()
                if self.px < -390:
                    self.bounceTracker = 0
                    self.px = 600
                    self.setpos(self.px, self.py)
                    Game()

    def hit(self):
        self.shotselection = "hit"
        if abs(self.vx) != self.vx:
            self.vx = 16
        else:
            self.vx = -16
        self.vy = 16

    def lob(self):
        self.shotselection = "lob"
        if abs(self.vx) != self.vx:
            self.vx = 13
        else:
            self.vx = -13
        self.vy = 25

    def winner(self):
        self.shotselection = "hit"
        if abs(self.vx) != self.vx:
            self.vx = 23
        else:
            self.vx = -23
        self.vy = 12

    def slice(self):
        self.shotselection = "slice"
        self.vx = -self.vx * .9
        self.vy = 15

    def end(self): #ends game
        turtle.clear()
        turtle.write("End of Game")
        turtle.bye()
        turtle.mainloop()



'''
Purpose: represents the court and game functions
Instance variables: self.ball - references Ball() for ball shape and flight path
self.rand_velocity - chooses x direction for inital ball
Methods: (What methods does this class have, and what does each do in a few words?)
'''
class Game:
    def __init__(self):
        turtle.delay(0)
        turtle.tracer(0,0)
        turtle.setworldcoordinates(-500, -500, 500, 500)
        # Wimbledon
        turtle.penup()
        turtle.setpos(-90, -200)
        turtle.pencolor("green")
        turtle.write("WIMBLEDON")
        turtle.setpos(-160, -250)
        turtle.write("PRO WARMUP COURT")
        turtle.penup()
        turtle.setpos(0,0)
        # Net
        turtle.pencolor("black")
        turtle.pendown()
        turtle.left(90)
        turtle.forward(30)
        turtle.penup()
        # Court line
        turtle.setpos(390,0)
        turtle.pendown()
        turtle.pencolor("green")
        turtle.left(90)
        turtle.forward(780)
        turtle.right(180)
        turtle.penup()
        # Sun
        turtle.setpos(320, 320)
        turtle.pendown()
        turtle.color("yellow")
        turtle.circle(50)
        turtle.penup()
        # Hide arrow
        turtle.hideturtle()

        rand_velocity = random.randint(0, 1) # chooses postivie/negative range for initial ball
        if rand_velocity == 1: # ball moves right
            xvelocity = random.uniform(8, 12) #picks float from positive range
        if rand_velocity == 0: # ball moves left
            xvelocity = random.uniform(-12, -8) # picks float from negative range

        # randomize tennis ball's starting position and velocity components
        self.ball = Ball((random.randint(-100, 100)), (random.randint(60,100)), xvelocity, (random.uniform(6, 10)))

        turtle.update()
        self.gameloop()
        turtle.onkeypress(self.ball.hit, "space")
        turtle.onkeypress(self.ball.lob, "q")
        turtle.onkeypress(self.ball.winner, "e")
        turtle.onkeypress(self.ball.slice, "f")
        turtle.onkeypress(self.ball.end, "x")
        turtle.listen()
        turtle.mainloop()
        
    def gameloop(self):
        if self.ball.px < 0:
            positionTracker = "Left Side"
        if self.ball.px >= 0:
            positionTracker = "Right Side"

        

        self.ball.move()


        if positionTracker == "Left Side" and self.ball.px >= 0:
            if self.ball.py <= 30:
                # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    self.gameloop
        if positionTracker == "Right Side" and self.ball.px < 0:
            if self.ball.py <= 30:
                # reset ball {
                    self.bounceTracker = 0
                    # chooses a random direction (left or right) and generates a random horizontal velocity 
                    rand_velocity = random.randint(0, 1) 
                    if rand_velocity == 1: # ball moves right
                        xvelocity = random.uniform(8, 12) # picks float from positive range
                    if rand_velocity == 0: # ball moves left
                        xvelocity = random.uniform(-12, -8) # picks float from negative range
                    
                    self.vx = xvelocity
                    # generate y velocity
                    self.vy = random.uniform(6, 10)
                    # generate x and y positions
                    self.px = random.randint(-100, 100) 
                    self.py = random.randint(60,100)

                    # set the x and y positions
                    self.setpos(self.px, self.py)
                    # }
                    self.gam

        turtle.update()
        turtle.ontimer(self.gameloop, 30)

if __name__ == '__main__':
    Game()