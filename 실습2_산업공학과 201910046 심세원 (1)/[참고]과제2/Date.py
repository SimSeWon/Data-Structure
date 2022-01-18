class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def increment(self):
        if self.lastDayOfTheMonth():
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1

    def leapYear(self):
        if self.year % 4 != 0 :
            return False
        elif self.year % 100 != 0:
            return True
        elif self.year % 400 != 0:
            return False
        else:
            return True

    def lastDayOfTheMonth(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12] and self.day == 31:
            return True
        elif self.month in [4, 6, 9, 11] and self.day == 30:
            return True
        elif self.leapYear() and self.month==2 and self.day==29:
            return True
        elif not self.leapYear() and self.month==2 and self.day==28:
            return True        
        else:
            return False
                

    def __gt__(self,rhs):
        if self.year > rhs.year:
            return True
        elif self.year < rhs.year:
            return False
        else:
            if self.month > rhs.month:
                return True
            elif self.month < rhs.month:
                return False
            else:
                if self.day > rhs.day:
                    return True
                elif self.day <= rhs.day:
                    return False

    def notEqual(self,rhs):
        if self.year!=rhs.year or self.month!=rhs.month or self.day != rhs.day:
            return True
        else:
            return False


    def __lt__(self,rhs):
        if self.year < rhs.year:
            return True
        elif self.year > rhs.year:
            return False
        else:
            if self.month < rhs.month:
                return True
            elif self.month > rhs.month:
                return False
            else:
                if self.day < rhs.day:
                    return True
                elif self.day >= rhs.day:
                    return False

    def __str__(self):
        return str(self.year)+"/"+str(self.month)+"/"+str(self.day)