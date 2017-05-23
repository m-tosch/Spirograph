import turtle
import math
from fraction import Fraction

class Spirograph():

    def __init__(self, R):
        """ Creates new Spirograph with outer radius R """
        self.R = R
        self.turtle = turtle.Turtle()


    def setSmallCircle(self, r):
        """ sets the radius of the small circle used to draw """
        self.r = r


    def setPen(self, l, color = 'black'):
        """ sets then pen color and its distance from C """
        self.l = l
        self.color = color


    def draw(self):
        """ draws a spirograph using the current small circle and pen settings """
        ###### CALC ######
        # use Fraction class to break down fraction
        k = Fraction(self.r, self.R)
        k.breakDown()
        l = self.l
        periods = k.num;
        print "k = %s\tl = %s\tperiods = %s" % (k, l, periods)

        xCoords = []
        yCoords = []
        k = float(k)

        # for small angle steps in the full range, calculate
        for angle in self.__drange(0, 2*math.pi*periods, 0.005):
            x = self.R*((1-k)*math.cos(angle) + l*k*math.cos(((1-k)/(k))*angle))
            y = self.R*((1-k)*math.sin(angle) - l*k*math.sin(((1-k)/(k))*angle))
            xCoords.append(x)
            yCoords.append(y)

        ###### INIT ######
        # turtle window and parameters
        screen = self.turtle.getscreen()
        # speed up drawing
        screen.tracer(15)
        self.turtle.speed(4)
        # set color
        self.turtle.color(self.color)

        ###### DRAW ###### 
        # move the pen to first point without drawing
        self.turtle.up()
        self.turtle.goto(xCoords[0], yCoords[0])
        self.turtle.down()
        # draw the points from the list
        for i in range(len(yCoords)):
            self.turtle.goto(xCoords[i], yCoords[i])

        
    def clear(self):
        """ reset the drawing surface """
        self.turtle.getscreen().reset()


    def __drange(self, start, end, step):
        """ decimal range to use for loop statements """
        curr = start
        while curr < end:
            yield curr
            curr += step