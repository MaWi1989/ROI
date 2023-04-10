class Property():
    def __init__(self):
        self.prop_price = 0
        self.income = 0
        self.expenses = 0
        self.cash_flow = 0 
        self.pet_fee = 50
        self.tennant_pet_fee = None 
        self.laundry = 0 
        self.storage = 0 
        self.rent = None

    def prop_val(self):
        print("Lets's get started!\n\nFirst:")
        self.prop_price = input("Please enter the cost of the property you bought or are planning to buy. \n")
         

    def tennant(self):
        # self.tenn1 = {}
        print("\n\nNow, please tell me about your (future) tennant!")
        self.name = input("What is your tennant's first and last name? \n").title()
        self.rent_amount = input("The rent amount is currently set at 1 percent of the property cost. If you would like to change that amount, please enter a different amount. If not, enter 'skip'. \n")
        if self.rent_amount.lower() == 'skip':
            self.rent = int(int(self.prop_price) * 0.01)
        else:
            self.rent = self.rent_amount 
        print(f"Your rent is set at ${self.rent} a month.")     
        self.pets = input("How many pets does your tennant own? For none, please enter 0. \n")
        self.tennant_pet_fee = int(self.pets) * self.pet_fee 
        self.tenn1 = {
            'Name:': self.name,
            'Rent:' : f'${self.rent}',
            'Pets:' : self.pets,
            'Pet Fee:' : f'${self.tennant_pet_fee}',
        }
        print("\n---------------------------\n")
        print("\nHere's a breakdown of your tennant:\n")
        # print("\n  Name  ", "  Rent ", "Pets", "Pet Fee")
        for k,v in self.tenn1.items():
            print(k, v)
        print("\n")
        # print("\n")

    def calc_income(self):
        print("\nNow, let's figure out how much money you'll get monthly from your tennant(s):\n")
        self.laundry = input("Do you offer laundry on your property? If yes, please enter monthly amount you charge your tennant. If no, please enter 0. \n")
        self.storage = input("Do you offer storage on your property? If yes, please enter monthly amount you charge your tennant. If no, please enter 0. \n")
        self.other = input("Do you have any other misc. income from this proberty / this tennant? If yes, please enter monthly amount, if no, please enter 0. \n")

        self.income = (int(self.rent) + int(self.tennant_pet_fee) + int(self.laundry) + int(self.storage) + int(self.other))
        print("\n---------------------------\n")
        print(f"\nYour total monthly income adds up to ${self.income}.\n")




    def calc_expenses(self):
        print("\n\nNext, let's figure out your monthly expenses: \n")
        self.tax = input("How much do you pay in annual taxes on this property? \n")
        self.monthly_tax = int(self.tax) / 12

        self.insurance = input("How much do you pay monthly on insurance for this property?\n" )
        self.utilities = input("How much do you pay monthly for utilities on this property? \n")
        self.HOA = input("How much do you pay monthly for HOA fees? \n")
        self.vacancy = input("How much would you like to put away each month for possible vacancy? \n")
        self.repairs = input("How much would you like to put away each month for possible repairs? \n")
        self.capex = input("How much would you like to put away each month for big replacements (e.g. roof) down the line? \n")
        self.prop_man = input("Will you hire property management? If yes, what is the monthly cost? If no, please enter 0. \n")
        self.mortgage = input("How much is your mortgage payment for this property? \n")
        self.other = input("Do you have any other misc. expenses for this proberty / this tennant? If yes, please enter monthly amount, if no, please enter 0. \n")

        self.expenses = (int(self.monthly_tax) + int(self.insurance) + int(self.utilities) + int(self.HOA) +  int(self.vacancy) + int(self.repairs) + int(self.capex) + int(self.prop_man) + int(self.mortgage) + int(self.other)) 
        
        print("\n---------------------------\n")
        print(f"\nYour total monthly expenses add up to ${self.expenses}.\n")

    def cash(self):
        self.cash_flow = int(self.income) - int(self.expenses)

        print("\n---------------------------\n")
        print(f"\nYour monthly cash_flow adds up to ${self.cash_flow}.\n")

    
    def ROI(self):
        print("\nNow, let's figure out your total investment in this property: \n")
        self.down = input("How much was your down payment on this property? \n")
        self.closing = input("How much was your closing cost on this property? \n")
        self.rehab = input("How much did you put into this property for repairs / rehab? \n")
        self.other = input("Did you put in any additional money after purchasing this property? If so, how much? If not, please enter 0. \n")

        self.investment = (int(self.down) + int(self.closing) + int(self.rehab) + int(self.other))

        print(f"\nYour total investment on this property adds up to ${self.investment}.\n")

        self.annual_cash = int(self.cash_flow) * 12

        self.ret_invest = round(((int(self.annual_cash) / int(self.investment)) * 100), 1)
        print("\n---------------------------\n")
        print(f"Your return on investment on this property will be {self.ret_invest}%.\n")
        print("If that's not enough for you, consider tweaking some numbers, \nlike the rent you charge, or the amount of money you're willing to spend to purchase the property. ")
        print("Feel free to use this calculator any time you need! \n")
        print("GOOD LUCK!")



    def run(self):
        print("\nHi! Thank you for choosing Wilson's ROI Calculator! \n")

        self.prop_val()

        self.tennant()

        self.calc_income()

        self.calc_expenses()

        self.cash()

        self.ROI()        


my_prop = Property()

my_prop.run()   