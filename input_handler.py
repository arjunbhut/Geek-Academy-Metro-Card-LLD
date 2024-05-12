from cards import *
from stations import *
import math
from constants import *

def card_manager(card_id, balance):
    new_card = CARD(card_id= card_id, balance= int(balance))
    return new_card

def create_stations(station_name):
    new_station = Station(station_name= station_name)
    return new_station

def get_card(card_number, card_objects):
    for card_object in card_objects:
        if card_number == card_object.get_card_id():
            return card_object

def check_and_get_discount_for_round_trip(card_number,
                                          other_station_obj,
                                          expense
                                          ):
    discount = 0
    if card_number in other_station_obj.get_card_numbers():
        discount = expense/HALF
        other_station_obj.remove_card_number(card_number)
    
    return discount

def check_current_balance_and_load_money_if_needed(card_number, card_objects, expense):

    service_charge = 0 
    card = get_card(card_number, card_objects)
    card_current_balance = card.get_balance()
    if card_current_balance < expense:
        extra_balance_needed = expense - card_current_balance
        service_charge = math.ceil(extra_balance_needed * SERVICE_CHARGE_RATE)
        card.update_balance(card_current_balance)
    else:
        card.update_balance(expense)
    
    return service_charge

def create_check_in(card_number,
                    citizen_type,
                    station,
                    card_objects,
                    airport_station,
                    central_station):
    # import ipdb;ipdb.set_trace()
    station_obj = airport_station if station == "AIRPORT" else central_station
    other_station_obj = central_station  if station == "AIRPORT" else airport_station
    
    # Get price based on citizen type
    expense = station_obj.get_ticket_price(citizen_type)
    # Check and get discount for round trip
    discount = check_and_get_discount_for_round_trip(card_number, 
                                                     other_station_obj,
                                                     expense)
    expense = expense - discount
    # Check if the current balance is enough or need to load money
    service_charge = check_current_balance_and_load_money_if_needed(card_number, card_objects, expense)
    # Add travel details
    station_obj.add_travel(card_number,
                        citizen_type,
                        expense,
                        service_charge,
                        discount)

def input_manager(lines):
    card_objects = []
    airport_station = create_stations("AIRPORT")
    central_station = create_stations("CENTRAL")
    station_objs = [central_station, airport_station]

    
    for line in lines:
        inputs_list = line.strip().split(" ")

        operation = inputs_list[0]
        # import ipdb;ipdb.set_trace()
        if "BALANCE" in operation:
            card_number = inputs_list[1]
            balance = inputs_list[2]
            card_obj = card_manager(card_id= card_number,
                        balance= balance)
            card_objects.append(card_obj)

        if "CHECK_IN" in operation:
            card_number = inputs_list[1]
            citizen_type = inputs_list[2]
            station = inputs_list[3]

            create_check_in(card_number,
                            citizen_type,
                            station,
                            card_objects,
                            airport_station,
                            central_station)
        
        if "PRINT_SUMMARY" in operation:
            for station in station_objs:
                passenger_details = station.get_passenger_travel_summary()
                total_collected_amount = int(station.get_total_collected_amount())
                total_discount_given = int(station.get_total_discount_given())
                station_name = station.get_station_name()
                print("TOTAL_COLLECTION ", 
                    station_name,
                    " ",
                    total_collected_amount, 
                    " ", 
                    total_discount_given)
            
                print("PASSENGER_TYPE_SUMMARY")
                for citizen_type, no_of_citizens in passenger_details.items():
                    print(citizen_type, " ", no_of_citizens)
            

            

