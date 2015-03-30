'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Colour import Colour
from RayTracer.Homogen import Homogen
from RayTracer.Material import Material


class Checkerboard(Material):
    """
    a material class that simulates the properties of a checkerboard surface
    """
    
    def __init__(self, baseColour = Colour(0,0,0), otherColour = Colour(255,255,255), ka=1.0, kd=0.1, ks=0.2, checkSize=1, shininess=17, reflection=0.0, shadowPower=0.7):
        """
        manages checkerboard settings and transfers potential material coefficients to super class 'Material'
        """
        Material.__init__(self, ka, kd, ks, shininess, reflection, shadowPower)
        self.baseColour = baseColour
        self.otherColour = otherColour
        self.checkSize = checkSize
        
    def baseColourAt(self, p):
        """
        returns the checkerboards material colour at a given point p
        """
        v = Homogen(p.x, p.y, p.z, 0)
        v = v.scale(1.0 / self.checkSize)
        if (int(abs(v.x)+0.5) + int(abs(v.y)+0.5) + int(abs(v.z)+0.5)) %2:
            return self.otherColour
        else:
            return self.baseColour