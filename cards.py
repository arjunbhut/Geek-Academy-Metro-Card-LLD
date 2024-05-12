class CARD:
    def __init__(self, card_id, balance):
        self.card_id = card_id
        self.balance = balance
    
    def get_balance(self):
        return self.balance
    
    def get_card_id(self):
        return self.card_id
    
    def update_balance(self, deducted_balance):
        self.balance -= deducted_balance 
