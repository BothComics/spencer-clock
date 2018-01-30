from graphics import *
from time import *
from math import *

def main():
#The window and background, calls the clock face
	win = GraphWin("Clock", 500,500)
	win.setBackground('red')
	clock_face(win)
#Main loop, calls hand drawing functions and undraws every second
	while True:
		time = localtime()
		hour = float(time[3])
		if hour > 12:
			hour -= 12
			minute = float(time[4])
		second = float(time[5])
		time = hour, minute, second

		hour_coord = hour_pos(hour)
		min_coord = min_pos(minute)
		sec_coord = sec_pos(second)

		display = Text(Point(250, 175), asctime())
		display.setSize(10)
		display.draw(win)

		hHand = hour_hand(hour_coord, win)
		mHand = min_hand(min_coord, win)
		sHand = second_hand(sec_coord, win)
		sleep(1)
		sHand.undraw()
		mHand.undraw()
		hHand.undraw()
		display.undraw()

#The clock face
def clock_face(win):
	face = Circle(Point(250,250), 239)
	face.setWidth(10)
	face.setFill("white")
	face.draw(win)

	displayBox = Rectangle(Point(170, 190), Point(330, 160))
	displayBox.setFill("light grey")
	displayBox.setWidth(3)
	displayBox.setOutline('grey')
	displayBox.draw(win)

	spencer = Text(Point(250, 300), "SPENCER")
	spencer.setStyle('italic')
	spencer.setFace('courier')
	spencer.setTextColor("gold")
	spencer.setSize(30)
	spencer.draw(win)

	clock_numbers = ['12','1','2','3','4','5','6','7','8','9','10','11']
#Draws the minute notches on the clock face
	for x in range(0, 360, 6):
		x = float(x)
		if x > 360:
			x -= 360
		innerX = 220*cos(radians(x)) + 250
		innerY = 220*sin(radians(x)) + 250
		outerX = 234*cos(radians(x)) + 250
		outerY = 234*sin(radians(x)) + 250
		notch = Line(Point(innerX, innerY), Point(outerX, outerY))
		notch.clone()
		notch.setWidth(2)
		notch.setFill('gold')
		notch.draw(win)

#Draws the hour notches on the clock face
	for i in range(0, 360, 30):
		i = float(i)
		if i > 360:
			i -= 360
		innerX = 220*cos(radians(i-90)) + 250
		innerY = 220*sin(radians(i-90)) + 250
		outerX = 234*cos(radians(i-90)) + 250
		outerY = 234*sin(radians(i-90)) + 250
		textX = 200*cos(radians(i-90)) + 250
		textY = 200*sin(radians(i-90)) + 250
		notch = Line(Point(innerX, innerY), Point(outerX, outerY))
		notch.clone()
		notch.setWidth(5)
		notch.draw(win)

#Draws the numbers on the clock face
		number = Text(Point(textX, textY), clock_numbers[int(i/30)])
		number.setSize(30)
		number.setStyle('bold')
		number.setFill('grey')
		number.draw(win)

#These functions take the time as input and returns the position for the hands
def hour_pos(hour):
	xpoint = 150*cos(radians((30*hour)-90))+250
	ypoint = 150*sin(radians((30*hour)-90))+250
	return xpoint, ypoint

def min_pos(minute):
	xpoint = 220*cos(radians((6*minute)-90))+250
	ypoint = 220*sin(radians((6*minute)-90))+250
	return xpoint, ypoint

def sec_pos(second):
	xpoint = 225*cos(radians((6*second)-90))+250
	ypoint = 225*sin(radians((6*second)-90))+250
	return xpoint, ypoint

#These functions draw the hands
def min_hand(min_coord, win):
	min = Line(Point(250,250), Point(min_coord[0], min_coord[1]))
	min.setWidth(10)
	min.draw(win)
	return min

def hour_hand(hour_coord, win):
	hour = Line(Point(250,250), Point(hour_coord[0], hour_coord[1]))
	hour.setWidth(20)
	hour.draw(win)
	return hour

def second_hand(sec_coord, win):
	sec = Line(Point(250,250), Point(sec_coord[0], sec_coord[1]))
	sec.setWidth(2)
	sec.setFill("red")
	sec.draw(win)
	return sec

main()