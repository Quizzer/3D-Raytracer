'''
Created on 22.04.2014

@author: Dominik
'''
import math

from RayTracer.Ray import Ray


class Camera(object):

    def __init__(self, e, c, up, fieldOfView, imageWidth, imageHeight):
        """
        manages camera settings
        and computes the height and width in dependence on the given 'fieldOfView'
        """
        self.e = e
        self.c = c
        self.up = up
        self.fieldOfView = fieldOfView # angular field
        self.wRes = imageWidth
        self.hRes = imageHeight
        self.calculateCoordinateSystem()
        
        alpha = (fieldOfView/(2*math.pi)) /2
        self.height = 2*math.tan(alpha)
        self.width = (self.wRes/float(self.hRes)) *self.height
        
        
    def calculateCoordinateSystem(self):
        """
        calculates a coordinate system with axes f,s,u out of the cameras perspective
        """
        self.f = (self.c-self.e).normalized()         #calculate f
        self.s = (self.f).cross(self.up).normalized()   #calculate s
        self.u = self.s.cross(self.f).normalized()    #calculate u
        
    def calcRay(self, x, y):
        """
        returns a object of type Ray from the cameras centre to the given point in x,y pixels
        """
        pixelWidth = self.width / (self.wRes-1)
        pixelHeight = self.height / (self.hRes-1)
        xcomp = self.s.scale(x*pixelWidth - self.width/2)
        ycomp = self.u.scale(y*pixelHeight - self.height/2)
        ray = Ray(self.e, self.f + xcomp + ycomp) # maybe several rays for one Pixel
        return ray
    
    