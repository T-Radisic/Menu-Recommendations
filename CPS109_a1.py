# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:56:18 2023

@author: radis

Menu Recommendations.

This program takes two menus-one ‘salty’ menu and one ‘sweet’ menu-which are written 
in text files and reads them into dictionaries with each key being the name of the 
dish, and each value being the number of servings the dish consists of (number of 
people the dish serves). This program solves the problem of what you would order 
from one or both menus. It accepts the option of having sweet food, salty food, or 
both and takes the number of people dining as inputs. With these two inputs, it 
returns a list of randomly selected dish recommendations that provide the appropriate 
number of servings to accommodate the number of people dining. It then writes these
recommendations into text files as ‘food orders’. Instead of struggling with the 
indecisiveness that comes with ordering for yourself and for other people, you can 
have this program pick out the appropriate dish for you and your party.
"""

import random


#Function 1: Menu recommendations
def menuSelection(menuLst,menuD,numPeop): #function used to select menu items 
    """
    This function takes in the menulist (sweet or salty), menu dictionary, and number of people eating
    and randomly selects menu items using randomly generated integers (used as indices) in the range 1-5.
    It then returns a list of the selected menu items.
    """
    dishlst = [] #dish list that will be returned
    count = 0 #count used to make sure dish selected is appropriate for the number of people eating
    while count < numPeop:
        
        randInd = random.randint(0,5)#selecting random index and selecting random dish
        dish = menuLst[randInd]
        
        serving = menuD.get(dish) #retrieving number of servings of selected dish
        
        if (count + serving) <= numPeop: #making sure dish selected is appropriate for number of people eating
            count += serving
            dishlst.append(dish)
    
    return dishlst #returning list of dish(es)

output = open("cps109_a1_output.txt","w") #opening file that will save output displayed in terminal
#Function 2: Menu recommendation display
def selectionDisplay(selectLst,menuD):
    """
    This function takes the list of menu recommendations, and the corresponding menu
    dictionary and displays each recommended item, the number of portions that should
    be ordered, and the number of people that each menu item can serve per portion. It 
    then displays the total servings of all the recommended items with respect to the 
    number of portions. This function also writes the output text file cps109_a1_output.txt.
    This file contains everything that is displayed when this function is called.
    Returns None
    """
    print('Here are your recommedations:\n')
    output.write('Here are your recommedations:\n')
    totalServe = 0
    setSelect = set(selectLst) #removes repeats of items for iteration
    for i in setSelect:
        numDish = selectLst.count(i)#count number of portions of menu items
        dishServ = menuD.get(i) #retrieve serving number of item per portion
        print(f"{numDish} portion(s) of {i} Which serves {dishServ} person(s) per portion")
        output.write(f"{numDish} portion(s) of {i} Which serves {dishServ} person(s) per portion")
        totalServe += numDish*dishServ #total number of servings
    print("")
    output.write("")
    print(f"This list of recommendations serves a total of {totalServe} person(s)\n")
    output.write(f"This list of recommendations serves a total of {totalServe} person(s)\n")


#Function 3: Writing menu recommendings into text file
def orderWriting(selectLst,menuD,sweet):
    """
    This function inputs the list of menu recommendations, the corresponding menu 
    dictionary, and the boolean var 'sweet' (if True then you write an order for 
    sweet foods, if False then you write an order for salty foods) and opens a txt
    file to write each menu recommendation with the number of portions and number of 
    people is serves per portion.
    Returns None
    """
    setSelect = set(selectLst) #removes repeats for iterations
    if sweet:
        file = open("sweetOrder.txt","w") #open sweet order
    else:
        file = open("saltyOrder.txt","w") #open salty order
    for i in setSelect:
        numDish = selectLst.count(i) #number of portions needed of menu item
        dishServ = menuD.get(i) #retrieving number of servings per portion
        file.write(f"{numDish} portion(s) of {i} ({dishServ} servings per portion)\n") #writing menu item info
    file.close()

#organizing data. Menu reading, list creation and dictionary creation

#reading salty menu items and saving them to list
fileSalty = open("salty.txt","r")
saltyLst = list(fileSalty)
fileSalty.close()

#reading sweet menu items and saving them to list
fileSweet = open("sweet.txt","r")
sweetLst = list(fileSweet)
fileSweet.close()

saltyD = {} #salty dictionary
sweetD = {} #sweet dictionary

for i in range(0,11,2): #creating sweet and salty menu dictionaries. Keys being dish names and values being number of people dish serves
    saltyD[saltyLst[i]] = int(saltyLst[i+1])
    sweetD[sweetLst[i]] = int(sweetLst[i+1])


#removing the number of servings per dish for both salty and sweet menu lists
saltyLst = [saltyLst[i] for i in range(0,11,2)]
sweetLst = [sweetLst[i] for i in range(0,11,2)]
#end up with lists consisting of just menu items


#Main program, input and output
print("Hello! I'm here to give you menu recommendations!\n")
menuType = input("Please input \'sweet\' for sweet menu, \'salty\' for salty menu, or \'both\' for both menus: \n")
print("")
numpeop = int(input("Please enter the number of people eating: \n"))
print("")

if menuType == 'sweet':
    #menu selection, display, and order writing for sweet food
    sweetSelect = menuSelection(sweetLst,sweetD,numpeop)
    selectionDisplay(sweetSelect,sweetD)
    orderWriting(sweetSelect,sweetD,True)
    
elif menuType == 'salty':
    #menu selection, display, and order writing for salty food
    saltySelect = menuSelection(saltyLst,saltyD,numpeop)
    selectionDisplay(saltySelect,saltyD)
    orderWriting(saltySelect,saltyD,False)
    
else:
    #menu selection, display, and order writing for salty food
    saltySelect = menuSelection(saltyLst,saltyD,numpeop)
    selectionDisplay(saltySelect,saltyD)
    orderWriting(saltySelect,saltyD,False)
    
    #menu selection, display, and order writing for sweet food
    sweetSelect = menuSelection(sweetLst,sweetD,numpeop)
    selectionDisplay(sweetSelect,sweetD)
    orderWriting(sweetSelect,sweetD,True)

output.close() #closing output text file