class pixel:
    def __init__(self, r = 0, g = 0, b = 0):
        self.red = r
        self.green = g
        self.blue = b
    def getColor(self):
        return "{} {} {}".format(self.red, self.green, self.blue)
class image:
    def __init__(self, h, w = h):
        self.pixels = [[pixel() for i in range(n)] for i in range[n]]
        self.height = h
        self.width = w
    def fileInput(file):
        enter = "p3\n {} {} \n".format(self.height, self.width)
        for i in self.pixels:
            row = ""
            for p in i:
                row += p.getColor()
            enter += row + "\n"
        with open(file+".ppm", "r+") as f:
            f.write(enter)


    
