'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Ray import Ray


class Corpus(object):
    
    def __init__(self, material):
        self.surface = material
        
    def colourAt(self, ray, hitdist, light, corpusList):
        """
        calculates the colour of a corpus at one given point
        the given point is where 'ray' intersects the corpus
        """
        d = ray.direction
        s = ray.pointAtParameter(hitdist)
        n = self.normalAt(s)
        l = (light.getPosition()-s).normalized()
        lr = (-l - (n.scale(n.dot(-l)*2))).normalized()
        
        a = self.calcAmbient(s)
        shadow = self.shade(l, s, corpusList, d, ray.direction, light)
        if shadow:
            colour = a * self.surface.shadowPower
        else:
            b = self.calcDiffuse(light, l, n)
            c = self.calcSpecular(light, lr, d)
            colour = a+b+c
        return colour
        
    def calcAmbient(self, s):
        """
        returns ambient proportion of its own colour
        """
        return self.surface.baseColourAt(s) * self.surface.ka
        
    def calcDiffuse(self, light, l, n):
        """
        returns diffuse proportion of global light
        """        
        return light.getColour() * self.surface.kd * l.dot(n)
    
    def calcSpecular(self, light, lr, d):
        """
        returns specular proportion of global light
        """
        x = max(lr.dot(-d), 0)
        return light.getColour() * self.surface.ks * (x**self.surface.shininess)
    
    def shade(self, l, s, corpusList, d, rd, light):
        """
        returns True if there is at least one object between the source of light and itself
        """
        s = s+rd.scale(-0.000001) # direction to camera
        #s = s+l.scale(0.0000001) # direction to light
        r = Ray(s, l)
        for corpus in corpusList:
                hitdist = corpus.intersectionParameter(r)
                if hitdist > 0 and hitdist < (light.getPosition() - s).length() :
                    return True
