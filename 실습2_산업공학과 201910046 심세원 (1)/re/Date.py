class Date:
    def __init__(self, year,month, day):
        self.year=year
        self.month=month
        self.day=day
    
    #구현해야 할 멤버 함수
    def __gt__(self, rhs):
        return ((self.year, self.month, self.day)>(rhs.year, rhs.month, rhs.day))
    
        
    def __lt__(self, rhs):
        return ((self.year, self.month, self.day)<(rhs.year, rhs.month, rhs.day))

    
        
    def __str__(self):
        return "{0}/{1}/{2}".format(self.year, self.month, self.day)   #매직메서드 정의


    def increment(self):
        if self.day==self.lastDayOfTheMonth():
            self.day=1
            if self.month==12:
                self.year+=1
                self.month=1
                #d=1
            else:
                self.month+=1
                #d=1
        else:
            self.day+=1
 


    def lastDayOfTheMonth(self):
        a=[1,3,5,7,8,10,12]
        b=[4,6,9,11]

        if self.month in a:
            return 31
        elif self.month in b:
            return 30
        elif ((self.year%4==0 and self.year%400==0) or self.year%100!=0):
            return 29
        else:
            return 28