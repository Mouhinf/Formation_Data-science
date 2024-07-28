class compte :
    def __init__(self, account_number : str, account_holder : str, solde_du_compte : int) :
        self.account_number = account_number
        self.solde_du_compte = solde_du_compte
        self.account_holder = account_holder
    def deposit(self, amount : float) : 
        self.solde_du_compte +=  amount
        print(f"La somme {amount} ajoutée du compte de {self.account_holder}. Nouveau solde {self.solde_du_compte}")
    
    def retirer(self, amount : float) :
        if amount < self.solde_du_compte :
            self.solde_du_compte -= amount
            print(f"La somme {amount} retirée du compte de {self.account_holder}. Nouveau solde {self.solde_du_compte}")
        else :
            print(f"La somme {amount} demandée ne se trouve pas dans votre compte")        

    def check_balance(self) : 
        return self.solde_du_compte
    
my_account1 = compte("1232349298", "Modou ", 200000)
my_account1.retirer(30000)
my_account1.deposit(15000)
my_account1.check_balance()

my_account2 = compte("766281976", "Fatima Zahra", 500000)
my_account2.retirer(78000)
my_account2.deposit(123000)
my_account2.check_balance()

my_account3 = compte("738829", "Yacine Niang", 1500000)
my_account3.retirer(18000)
my_account3.deposit(150000)
my_account3.check_balance()