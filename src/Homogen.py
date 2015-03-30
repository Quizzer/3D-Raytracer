'''
Created on 22.04.2014

@author: Dominik
'''
import math


class Homogen(object):
    """
    represents a algebraic homogeneous vector that can either be a point or a vector 
    """
    
    def __init__(self, x, y, z, h):
        """
        saves a homogen vector and reduces the homogen component h to either 0 or 1
        homogen component h=0 represents a vector, h=1 represents a point
        """
        self.h = float(h)
        if h == 0:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        else:
            self.x = x/h
            self.y = y/h
            self.z = z/h
    
    def __neg__(self):
        """
        returns the negated homogen vector
        """
        return Homogen(-self.x, -self.y, -self.z, -self.h)
    
    def __add__(self, other): # x : point or vector
        """
        returns the addition of itself and another homogen vector
        """
        return Homogen(self.x+other.x, self.y+other.y, self.z+other.z, self.h+other.h)
    
    def __sub__(self, other): # x : point or vector
        """
        returns the difference of itself an another homogen vector
        """ 
        return Homogen(self.x-other.x, self.y-other.y, self.z-other.z, self.h-other.h)
        
    def scale(self, scaleFactor):
        """
        returns a homogen vector which is the vector itself scaled by given factor 
        """
        assert(self.h == 0) # only with vectors
        return Homogen(self.x*scaleFactor, self.y*scaleFactor, self.z*scaleFactor, self.h)
        
    def length(self):
        """
        returns the length of the homogen vector
        assumption: points are of length = 0
        """
        if self.h == 0:
            return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.h**2)
        else:
            return 0
    
    def normalized(self):
        """
        returns the normalized homogen vector
        """
        assert(self.h == 0) # only with vectors
        if self.length():
            return Homogen(self.x/self.length(), self.y/self.length(), self.z/self.length(), self.h)
    
    def dot(self, other):
        """
        generates the scalar product of two homogen vectors
        """
        assert(self.h == 0 and other.h == 0) # only with vectors
        return (self.x*other.x + self.y*other.y + self.z*other.z + self.h*other.h)
    
    def cross(self, other):
        """
        generates the vector product of two homogen vectors
        """
        assert(self.h == 0 and other.h == 0) # only with vectors
        return Homogen(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x, self.h)
            
    def __repr__(self):
        return 'Homogen(%s, %s, %s, %s)' %(self.x, self.y, self.z, self.h)
        #if self.h == 0:
        #    return 'Vector(%s, %s, %s)' %(self.x, self.y, self.z)
        #elif self.h == 1:
        #    return 'Point(%s, %s, %s)' %(self.x, self.y, self.z)
        #else:
        #    raise Exception ("undefined Homogen")