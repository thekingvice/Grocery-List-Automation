'''
Munchy App MVP
v0.1
By Vicente Villareal
The purpose of munchy is to produce a 7-day dinner menu from the users favorite dishes
then create a grocery list based of the generated list.
'''
#--------import--------
from random import choice
#--------data----------
menu = []
dishes = ["Teriyaki Chicken", "Pizza", "Cheese Burger", "Tacos", "PBJ", "Mac and Cheese","Hot Dog"]
ingredients_Terichick = ["Chicken", "Teriyaki Sauce", "Rice"]
ingredients_Pizza = ["Cheese", "Tomato Sauce", "Pizza Dough"]
ingredients_Cheeseb = ["Ground Beef", "Burger Buns", "Cheese"]        
ingredients_Tacos = ["Steak", "Corn Tortillas", "Cilantro", "Onion"]
ingredients_PBJ = ["White Bread", "PB", "Jelly"]
ingredients_Mac = ["Cheese", "Milk", "Macaroni"]
ingredients_Hotdog = ["Hotdogs", "Hotdog Buns"]
#--------functions------
def inputval(answer):
    if answer.lower().strip() != "yes":
        answer = input("Invalid Input:Type 'Yes' to start.")
        
def createMenu(x):
    print("[Menu]")
    while len(menu) < x:
        chosendish = choice(dishes)
        if chosendish not in menu:
            menu.append(chosendish)
    for dish in menu:
        print(dish)
    
    
def createSL(list):
    print()
    print("[Grocery List]")
    grocery = []
    noDuplicates= []
    if "Teriyaki Chicken" in menu:
        grocery.extend(ingredients_Terichick)
    if "Pizza" in menu:
        grocery.extend(ingredients_Pizza)
    if "Cheese Burger" in menu:
        grocery.extend(ingredients_Cheeseb)
    if "Tacos" in menu:
        grocery.extend(ingredients_Tacos )
    if "PBJ" in menu:
        grocery.extend(ingredients_PBJ)
    if "Mac and Cheese" in menu:
        grocery.extend(ingredients_Mac)
    if "Hot Dog" in menu:
        grocery.extend(ingredients_Hotdog)
    for ingredient in grocery:
        if ingredient not in noDuplicates:
            noDuplicates.append(ingredient)
    for dish in noDuplicates:
        print(dish)
#--------start---------
answer = input("Start Munchy? Type 'Yes' to start.")
inputval(answer)
if answer.lower().strip() == "yes":
    print()
    print("Hey! My name is Munchy! Your personal grocery shopping assistant!")
    print()
#--------options-------
answer = input("Do yo want me to generate a 7-day menu and grocery list?")
inputval(answer)
if answer.lower().strip() == "yes":#generate menu and grocery list
    createMenu(7)
    createSL(menu)
    
 
        


    
