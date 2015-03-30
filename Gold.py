'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Colour import Colour
from RayTracer.Material import Material


class Gold(Material):
    """
    a material class that simulates the properties of a golden surface
    """
    
    def __init__(self, baseColour):
        Material.__init__(self, (0.329412, 0.223529, 0.027451), (0.780392, 0.568627, 0.113725), (0.992157, 0.941176, 0.807843), 27.8974, 0.5)
        #super(Plain, self).__init__(0.7, 0.4, 0.4, 18)
        self.baseColour = Colour(0,0,0)
        
    def baseColourAt(self, p=None):
        return self.baseColour