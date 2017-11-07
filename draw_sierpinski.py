from drawingpanel import *
import math

panel = DrawingPanel(1000,1000)
canvas = panel.canvas

def sierpinski(x,y,side_length,n):
	if n <= 0:
		return None
	else:
		canvas.create_polygon(x,y,x+side_length,y,x+0.5*side_length,y+math.sqrt(3)/2*side_length,fill = "cyan")
		side_length = side_length / 2
		x1 = x + side_length / 2
		y1 = y - side_length*math.sqrt(3)/2
		x2 = x - side_length /2
		y2 = y + side_length*math.sqrt(3)/2
		x3 = x + 1.5* side_length
		y3 = y2
		sierpinski(x1,y1,side_length,n-1)
		sierpinski(x2,y2,side_length,n-1)
		sierpinski(x3,y3,side_length,n-1)

def main():
	n = int(input("input n"))
	panel.set_background("white")
	side_length = 400
	canvas.create_polygon(400,800-400*math.sqrt(3),0,800,800,800,fill = "red")
	
	sierpinski(200,800-200 *math.sqrt(3),400,n)

main()