'''
Created on 22.04.2014

@author: Dominik
'''
class Material(object):
    """
    super class to all classes that simulate different materials on the surface of a corpus
    """
    
    def __init__(self, ka, kd, ks, shininess, reflection, shadowPower):
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.shininess = shininess
        self.reflection = reflection
        self.shadowPower = shadowPower