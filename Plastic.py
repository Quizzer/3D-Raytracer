'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Material import Material


class Plastic(Material):
    """
    a material class that simulates the properties of a plastic surface
    """
    def __init__(self, baseColour):
        Material.__init__(self, 0.5, 0.01, 0.5, 32)#.8974)
        #super(Plain, self).__init__(0.7, 0.4, 0.4, 18)
        self.baseColour = baseColour
        
    def baseColourAt(self, p=None):
        return self.baseColour