
from constants import *

class Station:

    def __init__(self, 
                 station_name, 
                ):
        
        self.station_name = station_name
        self.passenger_type = {}
        self.collected_amount = 0
        self.discount = 0
        self.card_numbers = []
        self.travel_count = 0
    

    def add_travel(self,
                   card_number,
                   citizen_type,
                   expense,
                   service_charge,
                   discount
                   ):
        self._update_passenger_details(citizen_type)
        self._update_financials(expense, 
                                service_charge,
                                discount)
        self._update_card_numbers(card_number, discount)
    
    def get_card_numbers(self):
        return self.card_numbers
    
    def _update_passenger_details(self, citizen_type):
        if self.passenger_type.get(citizen_type, ''):
           self.passenger_type[citizen_type] += INCREMENT
        else:
            self.passenger_type[citizen_type] = INCREMENT
    
    def _update_financials(self, expense, service_charge, discount):
        self.collected_amount += expense + service_charge
        self.discount += discount
    
    def _update_card_numbers(self, card_number, discount):
        if card_number not in self.card_numbers and not discount:
            self.card_numbers.append(card_number)

    def remove_card_number(self, card_number):
        self.card_numbers.remove(card_number)
    
    def get_ticket_price(self, citizen_type):

        if citizen_type == "SENIOR_CITIZEN":
            return SENIOR_CITIZEN
        if citizen_type == "ADULT":
            return ADULT_CITIZEN
        if citizen_type == "KID":
            return KID_CITIZEN
    
    def get_total_collected_amount(self):
        return self.collected_amount

    def get_total_discount_given(self):
        return self.discount
    
    def get_passenger_travel_summary(self):

        passenger_details = dict(sorted(self.passenger_type.items(), 
                                        key= lambda x: (-x[1], x[0])))
        return passenger_details

    def get_station_name(self):
        return self.station_name