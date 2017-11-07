from drawingpanel import *

panel = DrawingPanel(500,500)
canvas = panel.canvas

def draw_ehrenstein_circles(x1,x2,y1,y2,num):
	step = (x2-x1) / (num*2) 	
	for i in range(num):
			x = x1 + i* step
			y = y1 + i* step
			canvas.create_oval(x,y,x2-i*step,y2-i*step,outline="black",fill="yellow")
		

def draw_diamond(x1,y1,x2,y2):
	canvas.create_line(x1,(y1+y2)/2,(x1+x2)/2,y1, fill="black")
	canvas.create_line(x1,(y1+y2)/2,(x1+x2)/2,y2, fill="black")
	canvas.create_line(x2,(y1+y2)/2,(x1+x2)/2,y2, fill="black")
	canvas.create_line(x2,(y1+y2)/2,(x1+x2)/2,y1, fill="black")


def draw_grid(x1,y1,sizex,sizey,size,num,not_cirles_only):
	for i in range(sizex):
		for j in range(sizey):
			x = x1 + i* size
			y = y1 + j* size
			if not_cirles_only:
				canvas.create_rectangle(x,y,x+size,y+size,fill="cyan",outline="black")
			draw_ehrenstein_circles(x,x+size,y,y+size,num)
			if not_cirles_only:
				draw_diamond(x,y,x+size,y+size)

def drawing():
	panel.set_background("forest green")
	draw_grid(0,0,1,1,75,6,True)
	draw_grid(105,15,7,1,50,10,True)
	draw_grid(175,115,3,3,100,8,True)
	draw_grid(10,100,2,5,70,3,True)
	draw_grid(200,430,10,2,25,4,False)



def main():	
	drawing()

main()