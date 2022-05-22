# WRITE YOUR FUNCTIONS HERE

from os import remove
from tabnanny import check


def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

def add_or_remove_cash(petshop, money):
    petshop["admin"]["total_cash"] += money

def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]

def increase_pets_sold(petshop, nsold):
    petshop["admin"]["pets_sold"] += nsold

def get_stock_count(petshop):
    return len(petshop["pets"])

def get_pets_by_breed(petshop, desired_breed):
    new_list = []
    for pet in petshop["pets"]:
        if pet["breed"] == desired_breed:
            new_list.append(pet)
    return new_list

def find_pet_by_name(petshop, pet_name):
    for pet in petshop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

def remove_pet_by_name(petshop, pet_name):
  for index, pet in enumerate(petshop["pets"]):        
       if pet["name"] == pet_name:
            petshop["pets"].pop(index)

def add_pet_to_stock(petshop, new_pet):
    petshop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(petshop, pet, customer):
    try:
        find_pet_by_name(petshop, pet["name"])
    except:
        print("no pet found")
        return None

    can_afford = (customer_can_afford_pet(customer,pet))

    if can_afford:
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(petshop, pet["price"])
        increase_pets_sold(petshop, 1)
        add_pet_to_customer(customer, pet)
