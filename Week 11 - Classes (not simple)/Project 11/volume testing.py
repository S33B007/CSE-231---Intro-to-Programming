UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude = 0, units = 'ml'):   # this line is incomplete: parameters needed
        '''This function is to initialize the parameters'''
        if magnitude > 0 and (units == "ml" or units == "oz"):
            self.magnitude = magnitude
            self.units = units
        elif magnitude < 0  and (units == "ml" or units == "oz") :
            self.magnitude = 0
            self.units = None
        else:
            self.magnitude = None
            self.units = None
        
        
    def __str__(self):    # this line is incomplete: parameters needed
        '''display the magnitude (rounded to three decimal places) and the 
            units, with one space between them'''
        # as long as neither magnitude or units equal to none, "not a volunme" will not be printed
        if self.magnitude != 0  and self.units != None:
            out_str1 = "{:.3f} {}".format(self.magnitude, self.units)
        elif self.magnitude == None and self.units != None:
            out_str1 = "{:.3f} {}".format(self.magnitude, self.units)
        else:
            out_str1 = "Not a Volume"
        return out_str1
        
        
    def __repr__(self):    # this line is incomplete: parameters needed
        ''' display the magnitude (rounded to six decimal places) and the 
            units, with one space between them.'''
        # as long as neither magnitude or units equal to none, "not a volunme" will not be printed
        if self.magnitude != 0  and self.units != None:
            out_str2 = "{:.6f} {}".format(self.magnitude, self.units)
        elif self.magnitude == None and self.units != None:
            out_str2 = "{:.6f} {}".format(self.magnitude, self.units)
        else:
            out_str2 = "Not a Volume"
        return out_str2
        
    def is_valid(self):     # this line is incomplete: parameters needed
        '''Returns a Boolean to indicate whether or not V is valid'''
        if self.magnitude == None:
            return False
        elif self.units == None and self.magnitude != 0:
            return False
        else:
            return True
    
    def get_units(self):     # this line is incomplete: parameters needed
        '''Returns units stored during construction 
            ("ml" or "oz" if V is valid, None otherwise).'''
        if self.is_valid() == True:
            return self.units
        else:
            return None
    
    def get_magnitude(self):  # this line is incomplete: parameters needed
        ''' Returns magnitude stored during construction
            (numeric value if V is valid, None otherwise)'''
        if self.is_valid() == True:
            return self.magnitude
        else:
            return None
    
    def metric(self):      # this line is incomplete: parameters needed
        '''converts the volume units and magnitude to ml if it isn't already'''
        if self.is_valid() == True:
            if self.units != "ml":
                new_magnitude = (self.magnitude * MLperOZ) 
                return Volume(new_magnitude, "ml")
            else:
                return Volume(self.magnitude, "ml")
        else:
            return "invalid Volume object"

            
        
    def customary(self):    # this line is incomplete: parameters needed
        '''converts magnitude and units to oz if it isn't alreeady'.'''
        if self.is_valid() == True:
            if self.units != "oz":
                new_magnitude = (self.magnitude /MLperOZ)
                return Volume(new_magnitude, "oz")
            else:
                return Volume(self.magnitude, "oz")
        else:
            return "invalid Volume object"
        
    def __eq__(self, other):  # this line is incomplete: parameters needed
        '''Docstring'''
        V1 = self.get_magnitude()
        V2 = other.get_magnitude()
        if abs(V1 - V2) > DELTA:
            return False
        elif abs(V1 - V1) < DELTA:
            return True
        elif abs(V1 - V2) != DELTA:
            return True
        else:
            return False
       
    def add(self, other):  # this line is incomplete: parameters needed
        '''Docstring'''
        if self.is_valid() == True and other.is_valid() == True:
            if self.get_units() == "ml" and other.get_units() == "oz":
                V1 = self.get_magnitude()
                other_metric = other.metric()
                other_volume = other_metric.get_magnitude()
                new_volume = other_volume + V1
                return new_volume
        elif self.is_valid() == True and other.is_valid() == True:
            if self.get_units() == "oz" and other.get_units() == "ml":
                V1 = self.get_magnitude()
                other_custom = other.customary()
                other_volume = other_custom.get_magnitude()
                new_volume = other_volume + V1
                return new_volume
        
        elif (self.get_units() == "ml" or self.get_units() == "oz") and self.is_valid() == True:
            V1 = self.get_magnitude()
            if type(other) == int or type(other) == float:
                other_volume = other
                new_volume = (other_volume + V1)
                return new_volume
        elif (other.get_units() == "ml" or other.get_units() == "oz") and other.is_valid() == True:
            V1 = other.get_magnitude()
            if type(self) == int or type(self) == float:
                other_volume = self
                new_volume = (other_volume + V1)
                return new_volume
        else:
            out_str = "invalid Volume object"
            return out_str
        

        
    
    def sub(): # this line is incomplete: parameters needed
        '''Docstring'''
        pass

A = Volume(59, "ml")
B = Volume(69,"oz")
# C  = A+B
Answer = A.add(B)
print(Answer)