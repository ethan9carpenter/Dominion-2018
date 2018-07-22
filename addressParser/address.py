
class Address():
    
    def __init__(self, number, streetName, unit=None):
        self.number = number
        self.streetName = streetName
        self.unit = unit
        
        self._constructAddressString()
    
    def _constructAddressString(self):
        self.address = ""
        
        self.address += str(self.number) + " "
        
            
        self.address += self.streetName
                
        if self.unit:
            self.address += " " + self.unit
            
    def __str__(self):
        self._constructAddressString()
        return self.address