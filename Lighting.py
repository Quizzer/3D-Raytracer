'''
Created on 22.04.2014

@author: Dominik
'''
class Lighting(object):
    """
    simulates the global illumination of a scene
    """
    
    def __init__(self, centre, colour):
        self.centre = centre
        self.colour = colour
    
    def getPosition(self):
        """
        returns the centre of a source of Light
        """
        return self.centre
    
    def getColour(self):
        """
        returns the clolour the source of Light has
        """
        return self.colour