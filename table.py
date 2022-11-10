
from tabulate import tabulate

class Table:
    def __init__(self):
        self.name = 'name'
        self.auto = 'auto'
        self.row = 0
        self.column = 0
        self.head = ("N","Name", "Auto")
        self.content = [[self.row, self.name, self.auto]]

    def add(self, _name, _auto):
        if self.row == False:
           self.row+=1
           self.content = [[self.row,_name,_auto]] 
        else:
          self.row+=1
          self.content.append([self.row,_name,_auto])
          

    def  replacement(self, _row, _name, _auto):
        self.content[_row-1] = [_row,_name,_auto]

    def __del__(self):
        print('Память очищена!')
        

    def prinrf(self):
       print(tabulate(self.content,headers=self.head, tablefmt="grid"))

tabl = Table()
# tabl.content = [["Ivan"],["Porche"]]         
# tabl.prinrf()    
tabl.add("Ivan", "Porche")
tabl.add("Tom","BMV")
tabl.add("Boris","Kia")
tabl.add("Inna","Audi")
tabl.prinrf()  
x = tabl.content[0][0]
tabl.replacement(x,"Vanya", "Porche")
print("Замена участника №", x)
tabl.prinrf()
print("Кол-во участников:  ",tabl.row)
del tabl     