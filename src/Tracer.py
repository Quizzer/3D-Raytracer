'''
Created on 22.04.2014

@author: Dominik
'''
from RayTracer.Ray import Ray


class Tracer(object):
    """
    this class is the processing unit of the RayTracer that computes recursive reflection
    """
    
    def __init__(self, light, corpusList, BG_COLOUR, maxlevel):
        self.light = light
        self.corpusList = corpusList
        self.BG_COLOUR = BG_COLOUR
        self.maxlevel = maxlevel
    
    def intersect(self, level, ray, maxlevel):
        """
        computes potential intersections with corpus objects
        """
        maxdist = float('inf')
        retCorpus = None
        for corpus in self.corpusList:
            hitdist = corpus.intersectionParameter(ray)
            if hitdist:
                if hitdist < maxdist and hitdist > 0:
                    maxdist = hitdist
                    retCorpus = corpus
        if retCorpus:
            return (retCorpus, maxdist)
        else:
            return None
    
    def traceRay(self, level, ray):
        """
        returns a colour to be represented at the given point, where 'ray' intersects the corpus
        """
        if level == self.maxlevel:
            return self.BG_COLOUR
        hitPointData = self.intersect(level, ray, self.maxlevel)
        if hitPointData:
            return self.shade(level, hitPointData, ray)
        return self.BG_COLOUR
    
    def shade (self, level, hitPointData, ray):
        """
        calculates the different components of reflected and direct light
        """
        directColour = self.computeDirectLight(hitPointData, ray)
        reflectedRay = self.computeReflectedRay(hitPointData, ray)
        reflectedColour = self.traceRay(level+1, reflectedRay)
        
        return directColour + reflectedColour * hitPointData[0].surface.reflection
        
    def computeDirectLight(self, hitPointData, ray):
        """
        returns the illuminated colour on a specific point on a certain corpus
        """
        return hitPointData[0].colourAt(ray, hitPointData[1], self.light, self.corpusList)
        
    def computeReflectedRay(self, hitPointData, ray):
        """
        returns the reflection of a ray on a certain corpus
        """        
        d = ray.direction
        s = ray.pointAtParameter(hitPointData[1])
        n = hitPointData[0].normalAt(s)
        lr = (d - (n.scale(n.dot(d)*2))).normalized()
        s = s+lr.scale(0.000001)
        retRay = Ray(s, lr)
        return retRay