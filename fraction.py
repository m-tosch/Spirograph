class Fraction():
    """
    This it the doctstring for the Fraction class
    """

    def __init__(self, num, denom):
        """ num (numerator), denom (denominator) """
        self.num = num
        self.denom = denom


    def __add__(self, y):
        """
            Add two Fraction instances
            Works for positive and negative fractions
            1. expand fractions to be on the same denominator
            2. calculate result and save in a new instance
            3. break down the fraction if possible and return the instance
        """
        # 1
        expFrac = self.__expFrac(y)
        # 2
        f = Fraction(expFrac[0] + expFrac[1], expFrac[2])
        # 3
        return f.__breakDown()


    def __sub__(self, y):
        """
            Subtract a fraction instance from another
            Works for positive and negative fractions
            1. expand fractions to be on the same denominator
            2. calculate result and save in a new instance
            3. break down the fraction if possible and return the instance
        """
        # 1
        expFrac = self.__expFrac(y)
        # 2
        f = Fraction(expFrac[0] - expFrac[1], expFrac[2])
        # 3
        return f.__breakDown()


    def __expFrac(self, y):
        """
            *** EXPAND FRACTIONS ***
            (HELPER FUNCTION)
            
            Calculate new numerators for fractions to be on the same denominator.
            After this, calculations like + and - can be performed!
            
            1. calculate the new denominator (not searching for lcm to remain simplicity!)
            2. multiply both numerators with the opposite denominator
            3. return a tuple with the important values
        """
        # 1
        denom = self.denom * y.denom
        # 2
        new_num_self = self.num * y.denom
        new_num_y = y.num * self.denom
        # 3
        return [new_num_self, new_num_y, denom]
            
    
    def breakDown(self):
        """
            *** BREAK DOWN A FRACTION IF POSSIBLE ***
            (HELPER FUNCTION)
            
            check for a common divisor for the numerator and denominator
            in the range of [2,...,self.num / 2].
            
               abs(self.num) / 2 will calculate the EXACT middle number (half) for even numbers
               and the next integer below the half for uneven numbers
               (+1 is for indexing, because the second arg in range() is exclusive)
               (+1 to cover the possibility of self.num = 2, the range would be [2,2]
                   in this case and the loop would not run at all)
        """
        for i in range(2, abs(self.num) / 2 + 2):
            while self.num % i == 0 and self.denom % i == 0:
                self.num /= i
                self.denom /= i
        return self


    def __eq__(self, y):
        """ Check if two Fraction instances are equal """
        return float(self.num) / y.num == float(self.denom) / y.denom

    def __lt__(self, y):
        """ Check if one Fraction instance is less than the other """
        return float(self.num) / self.denom < float(y)

    def __ne__(self, y):
        """ Check if two Fraction instances are not equal """
        return float(self.num) / y.num != float(self.denom) / y.denom

    def __le__(self, y):
        """ Check if one Fraction instance is less than or equal to the other """
        return float(self.num) / self.denom <= float(y)

    def __gt__(self, y):
        """ Check if one Fraction instance is greater than the other """
        return float(self.num) / self.denom > float(y)

    def __ge__(self, y):
        """ Check if one Fraction instance is greater than or equal to the other """
        return float(self.num) / self.denom >= float(y)

    def __float__(self):
        """ Gets a floating point representation of a Fraction instance, called by float() """
        return float(self.num) / self.denom

    def __repr__(self):
        """ Gets a string representation of the Fraction instance, called by str() """
        return "%i/%i" % (self.num, self.denom)
