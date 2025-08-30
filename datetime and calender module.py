from datetime import date , time , datetime

#calling the today
#function of the dataclass
today = date.today()
now = datetime.now()
print("Today's date is",today)
print("\nCurrent date and time is",now)

# Printing date's components
print("\nDate components",today.year,today.month,today.day)

#activity 2 - random date and time

import random #importing value
import time

def getRandomDate(startDate,endDate): #defining a function 
    print("Printing random date between",startDate,"and",endDate)
    
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    
    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endTime = time.mktime(time.strptime(endDate,dateFormat))
    
    
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
    
    
#display result
print("Random date = ",getRandomDate("1/1/2023","12/31/2025"))

#activity  - 3 - trip expendexture

def hotelcost(nights):
    return 140*nights

#define a function called plane ride cost that takes a string,city as input
def planeridecost(city):
    if "Charlotte"== city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
#define a function called rentel car cost with argument called days
def rental_car_cost(days):
    if days>=7:
       return 40*days - 50
    elif days>=3:
       return 40*days -20
    else :
       return 40*days 
   
def tripcost(city,days,spendingmoney):
    return rental_car_cost(days) + hotelcost(days) + planeridecost(city)  + spendingmoney

print("Cost of car rental:",rental_car_cost(5))
print("Cost of plane ride:",planeridecost("Los Angeles"))
print("Cost of hotel room :",hotelcost(7))
print("Cost of the trip :",tripcost("Los Angeles",7,500))

print(tripcost("Tampa",6,500))


        
    
    
    
    
    
    
    
    