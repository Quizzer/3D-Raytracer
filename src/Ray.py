'''
Created on 22.04.2014

@author: Dominik
'''
class Ray(object):
    """
    represents an algebraic ray
    """
    
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalized()
    
    def __repr__(self):
        return 'Ray(%s, %s)' %(repr(self.origin),repr(self.direction))
    
    def pointAtParameter(self, t):
        """
        returns a point on the ray at a given distance parameter t
        """
        return self.origin + self.direction.scale(t)