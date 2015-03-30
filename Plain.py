'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Material import Material


class Plain(Material):
    """
    a material class that simulates the properties of a plain surface
    """
    
    def __init__(self, baseColour, ka=0.7, kd=0.3, ks=0.4, shininess=21, reflection=0.5, shadowPower=0.7):
        """
        manages plain settings and transfers potential material coefficients to super class 'Material'
        """
        Material.__init__(self, ka, kd, ks, shininess, reflection, shadowPower)
        self.baseColour = baseColour
        
    def baseColourAt(self, p=None):
        """
        returns the checkerboards material colour at a given point p
        in this case it is always the baseColour no matter at which p
        """
        return self.baseColour