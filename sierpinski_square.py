from drawingpanel import *
import math

panel = DrawingPanel(1000,1000)
canvas = panel.canvas


def sierpinski(x,y,side_length,n):
	if n <= 0:
		return None
	else:
		side_length = side_length / 3
		canvas.create_rectangle(x-side_length/2,y-side_length/2,x+side_length/2,y+side_length/2,fill="white")
		x1 = x-side_length
		x2 = x
		x3 = x+side_length
		y1 = y-side_length
		y2 = y
		y3 = y+side_length
		sierpinski(x1,y1,side_length,n-1)
		sierpinski(x1,y2,side_length,n-1)
		sierpinski(x1,y3,side_length,n-1)
		sierpinski(x2,y1,side_length,n-1)
		sierpinski(x2,y3,side_length,n-1)
		sierpinski(x3,y1,side_length,n-1)
		sierpinski(x3,y2,side_length,n-1)
		sierpinski(x3,y3,side_length,n-1)

def main():
	n = int(input("input n"))
	panel.set_background("white")
	
	canvas.create_rectangle(50,50,950,950,fill = "red")
	
	sierpinski(500,500,900,n)

main()