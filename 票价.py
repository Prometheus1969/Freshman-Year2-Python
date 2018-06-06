class Ticket :

    def setInfo( self, types, day,) :
        self.type = types
        self.day = day
        self.ticket = 100
        if types == "child" :
            self.ticket = self.ticket*0.5
        if day == "yes" :
            self.ticket = self.ticket*1.2
    def getMoney( self ) :
        return self.ticket * self.type

a = Ticket()
sum = 0
x1 = eval(input("请输入儿童个数："))
x2 = eval(input("请输入成人个数："))
y = input("请输入是否为周末：")
a.setInfo( x1, y )
sum = a.getMoney()
print(a.getMoney())
a.setInfo( x2, y )
print(a.getMoney())
sum = sum + a.getMoney()
print(sum)
            
