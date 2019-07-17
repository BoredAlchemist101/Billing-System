#making an billing application this will contain all modules
import json
id = 1

class bill():
    fooda = food()
    def __init__(self,customer_name,order_list):
        self.customer_name = customer_name
        self.order_list = order_list
        self.id = id
        id +=1

    def retrive_bill(self,id):
        file2 = open('detail.txt','r')
        lines=file2.readlines()
        x = json.loads(lines[id])
        self.customer_name = x[customer_name]
        self.order_list = x[order_list]
        self.id = x[id]


    def save_bill(self,bill):
        file = open('detail.txt','a')
        tempbill = {'customer_name':self.customer_name,
                'order_list':self.order_list,
                'id':self.id}
        savedbill = json.dumps(x)
        file.write(y+"\n")


    """def print_bill(self):
        price = 0
        print("Hello Hotel")
        print("--------------")
        for i in self.order_list():
            pricew = fooda.price(i)
            print(f"{i}      {pricew}")
            price += pricew
        print("Thanks For Ordering")
        print(f"Have a nice day {self.customer_name}")"""
class food():
    def __init__(self):
        food_list = {
        "Punjabi" : 100,
        "Gujarati" : 80,
        "Chinese" : 30,
        "South Indian": 40}

    def price(self,food_name):
        try:
            self.price = self.food_foodlist[food_name]
        except KeyError:
            print("no food under this name")
        else:
            return self.price
    def add_food(self,food_name,food_price):
        try:
            if food_price > 0:
                self.food_list[food_name]=food_price
        except TypeError:
            print("Price must be an integer bro !")
    def del_food(self,food_name):
        try:
            del self.foodlist[food_name]
        except KeyError:
            print("no food exist by this name")
    def change_price(self,food_name,new_price):
        try:
            self.foodlist[food_name] = new_price
        except KeyError:
            print("no food exist by this name")
    def change_name(self,old_name,new_name):
        temp = self.foodlist[old_name]
        self.del_food(foodlist[old_name])
        self.add_food(new_name,temp)

hello = bill('Harsh gandhi',['Punjabi'])
hello.print_bill()
