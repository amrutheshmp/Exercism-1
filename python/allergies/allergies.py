class Allergies(object):
    lst = []
    def __init__(self,allergie):
        self.allergie=int(allergie)
        n =  8
        l = []
        while(self.allergie >= 256):
            self.allergie = self.allergie - 2 ** n
            n=+1
        while(self.allergie > 0) :
            if self.allergie >= 128 :
                l.append("cats")
                self.allergie = self.allergie - 128
            elif self.allergie >= 64 :
                l.append("pollen")
                self.allergie = self.allergie - 64
            elif self.allergie >= 32 :
                l.append("chocolate")
                self.allergie = self.allergie - 32
            elif self.allergie >= 16 :
                l.append("tomatoes")
                self.allergie = self.allergie - 16
            elif self.allergie >= 8 :
                l.append("strawberries")
                self.allergie = self.allergie - 8
            elif self.allergie >= 4 :
                l.append("shellfish")
                self.allergie = self.allergie - 4
            elif self.allergie >= 2 :
                l.append("peanuts")
                self.allergie = self.allergie - 2
            elif self.allergie >= 1 :
                l.append("eggs")
                self.allergie = self.allergie - 1
        self.lst = l

    def is_allergic_to(self,s):
        return s in self.lst
