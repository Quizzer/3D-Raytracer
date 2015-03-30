'''
Created on 22.04.2014

@author: Dominik
'''
import math

from RayTracer.Corpus import Corpus


class Sphere(Corpus):
    """
    a lower class to Corpus representing a algebraic Sphere
    """
    
    def __init__(self, center, radius, material):
        Corpus.__init__(self, material)
        self.center = center
        self.radius = radius
        
    def __repr__(self):
        return 'Sphere(%s, %s)' % (repr(self.center), self.radius)
    
    def intersectionParameter(self, ray):
        """
        returns the distance where the sphere is intersected by the given 'ray' 
        """
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v * v - co.dot(co) + self.radius * self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)
            
    def normalAt(self, p):
        """
        returns a normal vector of the sphere at the given point 'p'
        """
        return (p - self.center).normalized()
