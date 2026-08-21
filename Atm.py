class Atm:
    def __init__(self):
        self.pin = " "
        self.balance = 0
        
    def Menu(self):
        print("1 .Enter 1 to set pin")
        print("2. Enter 2 to Check Balance")
        print("3. Enter 3 to Deposite Money")
        print("4. Enter 4 to Withdraw Money")
        print("5. Enter 5 to Change Pin")
        print("6. Enter 6 to Exit")
        
        choice = int(input("enter your Choice:"))
        
        match choice:
            case 1:
                self.set_pin()
            case 2:
               self. check_balance()
            case 3:
               self. Deposite_money()
            case 4:
                self.Withdraw_ammount()
            case 5:
                self.change_pin()
            case 6:
                self. exist_menu()
         
    def set_pin(self):
        if self.pin == " ":
            input_pin = input("enter pin :")
            self.pin = input_pin
            print("pin set", self.pin)
            self.Menu()
        else:
            print("Pin already set")
            self.Menu()
            
    def check_balance(self):
        userpin=input("enter your pin :")
        if self.pin==userpin:
            print("your balance is :",self.balance)
            self.Menu()
        else:
            print("invalid pin")
            self.Menu()
            
    def Deposite_money(self):
        userpin=input("enter your pin :")
        
        if self.pin==userpin:
            print("your balance is :",self.balance)
            input_ammount = int(input("enter ammout for deposite :"))
            self.balance+=input_ammount
            print('your bank balance is :',self.balance)
            self.Menu()
            
        else:
            print("invalid pin")
            self.Menu()
            
    def Withdraw_ammount(self):
        userpin=input("enter your pin ")
        if self.pin==userpin:
            withdraw_ammount=int(input("enter your withdraw ammount:"))
            
            if withdraw_ammount<=self.balance:
                self.balance-=withdraw_ammount
                print("your bank balance is:",self.balance)
                self.Menu()
                
            else:
                print("insafficiant bank balance")
                self.Menu()
        else:
            print("invalid pin")
            self.Menu()
            
    def change_pin(self):
        oldpin=input("enter your old pin:")
        
        if oldpin==self.pin:
            newpin=input("enter your new pin")
            self.pin==newpin
            print("pin update :",self.pin)
            self.Menu()
            
        else:
            print("please enter a match pin")
            self.Menu()

    def exist_menu(self):
        print("thank you Visit again")
            
        
obj1=Atm()
obj1.Menu()
        
   