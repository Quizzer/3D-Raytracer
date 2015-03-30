'''
Created on 22.04.2014

@author: Dominik Neu (873483)
'''
import sys
from PIL import Image

from RayTracer.Camera import Camera
from RayTracer.Checkerboard import Checkerboard
from RayTracer.Colour import Colour
from RayTracer.Homogen import Homogen
from RayTracer.Lighting import Lighting
from RayTracer.Plain import Plain
from RayTracer.Plane import Plane
from RayTracer.Sphere import Sphere
from RayTracer.Tracer import Tracer
from RayTracer.Triangle import Triangle


def main():
    """
    general settings
    initialisation of objects (corpus)
    computing and saving image
    """

    # parse parameters
    print sys.argv
    aufgabe = 3
    size = (400, 400)
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ['1','2','3']:
            aufgabe = int(sys.argv[1])
            if len(sys.argv) > 2:
                if len(sys.argv) > 3:
                    size = (int(sys.argv[2]), int(sys.argv[3]))
                else:
                    size = (int(sys.argv[2]), int(sys.argv[2]))
        else:
            if len(sys.argv) > 2:
                size = (int(sys.argv[1]), int(sys.argv[2]))
            else:
                size = (int(sys.argv[1]), int(sys.argv[1]))
        
                
    # image size
    imageWidth = size[0]
    imageHeight = size[1]
    
    # colours
    black = Colour(0,0,0)
    white = Colour(255,255,255)
    grey = black.compound(white)
    red = Colour(255,0,0)
    green = Colour(0,255,0)
    blue = Colour(0,0,255)
    yellow = red + green
    
    # points
    origin = Homogen(0,0,0,1)
    p1 = Homogen(0,5,0,1)
    p2 = Homogen(1.5,2.5,0,1)
    p3 = Homogen(-1.5,2.5,0,1)
    
    # vector
    e2 = Homogen(0,1,0.02,0)

    # corpus objects
    greyBottom = Plane(origin, e2, Plain(grey, reflection=0))
    if aufgabe == 3:
        greyBottom = Plane(origin, e2, Checkerboard(black, white))
        
    yellowTriangle = Triangle(p1, p2, p3, Plain(yellow, shadowPower=0.9)) 
    radius = 1.2
    redSphere = Sphere(p2, radius, Plain(red, shadowPower=0.9))
    greenSphere = Sphere(p3, radius, Plain(green, shadowPower=0.9))
    blueSphere = Sphere(p1, radius, Plain(blue, shadowPower=0.9))
    
    #list corpus objects
    corpusList = []
    corpusList.append(greyBottom)
    corpusList.append(yellowTriangle)
    corpusList.append(redSphere)
    corpusList.append(greenSphere)
    corpusList.append(blueSphere)
    
    # lighting settings
    sunPoint = Homogen(30, 30, 10,1)
    light = Lighting(sunPoint, white)

    # camera settings    
    e = Homogen(0,1.8,10,1)
    c = Homogen(0,3,0,1)
    up = Homogen(0,1,0,0)
    cam = Camera(e, c, up, 45, imageWidth, imageHeight)

    # calculate,display and save image
    img = Image.new("RGB", (imageWidth,imageHeight))    
    
    maxlevel = 3
    if aufgabe == 1:
        maxlevel = 1
    
    print "creating image..."
    for x in range(imageWidth):
        for y in range(imageHeight):
            ray = cam.calcRay(x, y)
            rayTracer = Tracer(light, corpusList, black, maxlevel)
            colour = rayTracer.traceRay(0, ray)
            img.putpixel((x,(imageHeight-y-1)), colour.getRGB())
    
    print "completed."        
    img.show()
    print "saving image..."
    img.save('RayTracer.bmp')
    print "saved as 'RayTracer.bmp'."

if __name__ == '__main__':
    main()