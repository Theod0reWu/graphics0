class pixel:
    def __init__(self, r = 0, g = 0, b = 0):
        self.red = r 
        self.green = g
        self.blue = b
    def setColor(self, r = -1, g = -1, b = -1):
    	self.red = self.red if r = -1 else r
    	self.green = self.green if g = -1 else g
    	self.blue = self.blue if b = -1 else b
    def getColor(self):
        return "{} {} {}".format(self.red, self.green, self.blue)
class image:
    def __init__(self, h, w):
        self.pixels = [[pixel() for i in range(w)] for i in range(h)]
        self.height = h
        self.width = w
    def toFile(self,file):
        enter = "P3\n{} {}\n255\n".format(self.height, self.width)
        for i in self.pixels:
            row = ""
            for p in i:
                row += p.getColor() + " "
            enter += row + "\n"
        with open(file+".ppm", "w+") as f:
            f.write(enter)
    def printIt(self):
        enter = "P3\n{} {}\n255\n".format(self.height, self.width)
        for i in self.pixels:
            row = ""
            for p in i:
                row += p.getColor() + " "
            enter += row + "\n"
        print(enter)
    def allPix(self, funct): #funct is a function that takes in a pixel and modifies it
        for r in self.pixels:
            for c in r:
                funct(c)
    def allPixCoord(self, funct):
        for h in range(self.height):
            for w in range(self.width):
                funct(w,h,self.pixels[w][h])
    def plot(self,w, h, r = 0, g = 0, b = 0):
        self.pixels[h][w].setColor(r,g,b)
    
nothing = image(500,500)
from random import randint
def rando(pixel):
    pixel.red = randint(0,255)
    pixel.green = randint(0,255)
    pixel.blue = randint(0,255)
#nothing.allPix(rando)
#nothing.printIt()
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 80:
        z = z*z + c
        n += 1
    return n

def man(w,h,pixel):
    c = complex(-2 + (w / 500) * (1 - -2),-1 + (h / 500) * (1 - -1))
    m = mandelbrot(c)
    pixel.red = 255 - int(m * 255 / 80)
nothing.allPixCoord(man)
nothing.toFile("image")

