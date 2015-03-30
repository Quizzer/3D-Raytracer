'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Corpus import Corpus


class Plane(Corpus):
    """
    a lower class to Corpus representing a algebraic Plane
    """
    
    def __init__(self, point, normal, material):
        Corpus.__init__(self, material)
        self.point = point
        self.normal = normal.normalized()
        
    def __repr__(self):
        return 'Plane(%s, %s)'%(repr(self.point), repr(self.normal))
    
    def intersectionParameter(self, ray):
        """
        returns the distance where the plane is intersected by the given 'ray' 
        """
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)
        if b:
            return -a/b
        else:
            return None
        
    def normalAt(self, p):
        """
        returns a normal vector of the plane at the given point 'p'
        """
        return self.normal
