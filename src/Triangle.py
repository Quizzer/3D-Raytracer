'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Corpus import Corpus


class Triangle(Corpus):
    """
    a lower class to Corpus representing a algebraic Triangle
    """
    
    def __init__(self, a, b, c, material):
        Corpus.__init__(self, material)
        self.a = a
        self.b = b
        self.c = c
        self.u = self.b - self.a
        self.v = self.c - self.a
    
    def __repr__(self):
        return 'Triangle(%s, %s, %s)' %(repr(self.a), repr(self.b), repr(self.c))
    
    def intersectionParameter(self, ray):
        """
        returns the distance where the triangle is intersected by the given 'ray' 
        """
        w = ray.origin - self.a
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu
        if 0 <= r and r <= 1 and 0 <= s and s <= 1 and r+s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None
        
    def normalAt(self, p):
        """
        returns a normal vector of the triangle at the given point 'p'
        """
        return self.u.cross(self.v).normalized()
