class Category:
    def __init__(self,name):
        self.ledger = []
        self.name = name

    def deposit(self,amount,description =''): 
        self.ledger.append({'amount': amount, 'description': description}) 

    def withdraw(self,amount,description =''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -(amount), 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(dictionary['amount'] for dictionary in self.ledger) 

    def transfer(self,amount,category):
        if self.withdraw(amount,description =f'Transfer to {category.name}'):
            category.deposit(amount,f'Transfer from {self.name}')
            return True
        else:
            return False
         

    def check_funds(self,amount):
        if amount >  self.get_balance():
            return False
        else :
            return True 

    def __str__(self):
        title = f"{self.name:*^30}\n"
        entries = ""
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"

            entries += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + entries + total

def create_spend_chart(categories):
    lines =[] 
    title='Percentage spent by category'
    lines.append(title)
    total=[]
    for category in categories:
        spent = -sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        total.append(spent)

   
    grand_total =sum(total)
    percentage =[]  
    for spent in total:
        percentage.append((spent* 100 / grand_total )// 10 * 10)

    for label in range(100, -1, -10):
        row = f"{label:>3}|"
        for pct in percentage:
            if pct >= label:      
                 row += " o "
            else:
                row += "   "     
        row += " "
        lines.append(row)

    
    count = len(categories)
    line = "    " + "-" * (count * 3 + 1)
    lines.append(line)
   
    names = [category.name for category in categories]    
    longest = max(len(name) for name in names)
    for i in range(longest):
        row = "     "
        for name in names:
            row += (name[i] + "  " if i < len(name) else "   ")

        lines.append(row)
        
    return '\n'.join(lines)
 
