# by Antoni Gual Via 4/2015

from tkinter import Tk, Canvas, PhotoImage,NW,mainloop 
from time import time

def mandel_pixel(x0,y0):   #c is a complex
  """ calculates the color index of the mandelbrot plane point passed in the arguments """
  maxIt = 256
  x=x0
  y=y0
  
  for i in range(maxIt):
      x2=x*x
      y2=y*y
      xt=x2-y2+x0
      y=2*x*y+y0
      x=xt
      if (x2+y2)  > 4.:
         return i
      
  return maxIt

def mandelbrot(xa,xb,ya,yb,x,y):
    """ returns a mandelbrot in a string for Tk PhotoImage"""
    #color string table in Photoimage format #RRGGBB 
    clr=[ ' #%02x%02x%02x' % (int(255*(((i+1)/255)**.25)),0,0) for i in range(256)]
    clr.append(' #000000')  #append the color of the centre as index 256
    #calculate mandelbrot x,y coordinates for each screen pixel
    xm=list([xa + (xb - xa) * kx /x  for kx in range(x)])
    ym=list([ya + (yb - ya) * ky /y  for ky in range(y)])
    #build the Photoimage string by calling mandel_pixel to index in the color table
    return " ".join((("{"+"".join(clr[mandel_pixel(i,j)] for i in xm))+"}" for j in ym))



#window size
x=640
y=480
#corners of  the complex plane to display  
xa = -2.0; xb = 1.0
ya = -1.27; yb = 1.27

#Tkinter window
window = Tk()
canvas = Canvas(window, width = x, height = y, bg = "#000000");canvas.pack()
img = PhotoImage(width = x, height = y)
canvas.create_image((0, 0), image = img, state = "normal", anchor = NW)

#do the mandelbrot
print('Starting Mandelbrot')
t1=time()
img.put(mandelbrot(xa,xb,ya,yb,x,y))
print(time()-t1, ' seconds')

mainloop()
