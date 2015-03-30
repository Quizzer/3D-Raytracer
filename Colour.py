'''
Created on 22.04.2014

@author: Dominik
'''
class Colour(object):
    
    def __init__ (self, r=0, g=0, b=0):
        """
        saves coefficients r = red, g = green, b = blue of a colour
        """
        self.r = float(min(max(0, r), 255))
        self.g = float(min(max(0, g), 255))
        self.b = float(min(max(0, b), 255))
        
    def getRGB(self):
        """
        returns r,g,b as a tuple
        """
        return int(self.r),int(self.g),int(self.b)
    
    def __add__(self, other):
        """
        simulates additive color mixing
        """
        assert(type(other) == type(Colour()))
        return Colour((self.r+other.r), (self.g+other.g), (self.b+other.b))
    
    def compound(self, other):
        """
        simulates subtractive color mixing
        """
        return Colour((self.r+other.r)/2, (self.g+other.g)/2, (self.b+other.b)/2)
    
    def __mul__(self, t):
        """
        gives the possibility to multiply colours with an scalar factor 't'
        't' can also be a tuple containing three coefficients for each r,g and b
        """
        if type(t) == type(tuple()) and len(t) == 3:
            return Colour(self.r*float(t[0]), self.g*float(t[1]), self.b *float(t[2]))
        elif type(t) == type(float()) or type(t) == type(int()):
            return Colour(self.r*float(t), self.g*float(t), self.b *float(t))
        else:
            raise Exception ("forbidden multiplication")
    
    def __rmul__(self, t):
        return self.__mul__(t)
        
    def __repr__(self):
        return "Colour(%s, %s, %s)" %(self.r, self.g, self.b)
