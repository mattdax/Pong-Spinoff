
#Import statement
import pyglet

#Dimensions
width = 1280
height = 720
#Starting POS of the player
xs = 32
ys = 32
speedofplayer = 10
curscore = 0


#Creates the window
window = pyglet.window.Window(width,height,"Matt's Pong")

#Setting up keys
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

#Loading in the sprites
image = pyglet.image.load("C:\\Users\Matthew\\Documents\\ooo.png")
sprite= pyglet.sprite.Sprite(image,x=xs,y=ys)


#Scale the sprites down to preffered size
sprite.update(scale_x=0.125,scale_y=0.5)

#First pixel location

#Middle of screen
x = width//2
y = height//2
#Direction 1 = pos -1=neg
xx = 1
yy = 1


score = pyglet.text.Label(str(curscore),font_size=36,
                         x=window.width//2, y=650,
                        anchor_x='center', anchor_y='top')


#Updates the location of the pixels
def update(dt):
	#global variables
	global x,y,xx,yy, speedofplayer,curscore
	
	#Checks if ball is bouncing off walls, if it is, direction is changed.
	if x>=width:
		xx=-(xx*1.25)
		speedofplayer = speedofplayer*1.25
	if y>=height:
		yy=-1
	if x<=0:
		exit()
	if y<=0:
		yy=1
	#Check for ball colliding with paddle=
	if (y>=sprite.y and y<=(sprite.y+int((255*0.5)))) and x<=(64):
		if xx <= 0:
			xx= xx*-1
		elif yy == 1:
			yy=-1
		elif yy == -1:
			yy = 1
		curscore+=1
		score.text=(str(curscore))
	x=x+xx
	y=y+yy
	#print(sprite.y)
	#print(y)




#Draws the pixel onto the gui
@window.event
def on_draw():
	#(x,y) gives the location of the pixel
	window.clear()
	score.draw()
	sprite.draw()
	pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,('v2i',(x,y)))
	
@window.event
def on_key_press(symbol,modifiers):
	if(symbol == pyglet.window.key.P):
		pyglet.clock.schedule_interval(update,1/120)
	if(symbol == pyglet.window.key.O):
		pyglet.clock.unschedule(update)
@window.event
def on_text_motion(motion):
	if(motion == pyglet.window.key.MOTION_UP):
		if ((sprite.y+int(255*0.5))+speedofplayer)>=height:
			sprite.y=height-int(256*0.5)
		else:
			sprite.y+=speedofplayer
	if(motion == pyglet.window.key.MOTION_DOWN):
		if sprite.y-speedofplayer<0:
			sprite.y=0
		else:
			sprite.y-=speedofplayer
		

#Runs the GUI
pyglet.app.run()
