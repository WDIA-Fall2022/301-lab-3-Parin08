# Name: Parin Patel
# Student Number: 040882160

import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))

# ask the user for the code of the country and save it into a variable
countryCode = input("Please enter the country code. ")

# Scan the list l line by line and add 1 to the counter if the country is the one looked for
# Define counter variable
counter = 0
#  Loop over list and checking countrycode match with input provide by user. If it is matching then increment counter by 1.
# Also transforming input to uppercase since all the records as countrycode is in uppercase
for li in l:
    if (countryCode.upper() == li):
        counter += 1;

# Format and print the result
# Printing number of countries found in list.
print("Number of countries with country code {countryCode} is  {counter}.".format(countryCode=countryCode,counter=counter))

# Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer
population = input("Enter the population ")

# Trying to cast population String as int value. 
# If user input anything apart from number then this operation will throw an error. 
# So here I am using try block for that and in except block I have create  loop which will execute till user provide valid numeric value.
try:
    int(population)
except:
    while not(population.isnumeric()):
            population = input("Enter the population ")


#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lstOfRecords = list()

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
# Looping over l1 list and checking each population is weather higher than input or lower than input. 
# If it is higher than input then it will be added into the list lstOfRecords

for li in l1:
    if(int(population)<li):
        lstOfRecords.append(l1.index(li))

#Print the list lstOfRecords

print("Index of the cities in the list")
print(lstOfRecords)

print("------------------------------------------------")
# #Bonus: Print the name of the cities whose index is in lstOfRecords
# Getting all records of cities and string into l3 list
# Looping over lstOfRecords list which have all index positions stored and than printing same index position records from l3 list
print("Name of the cities")
l3 = list(db.ws(ws='Sheet1').col(col=2))

for l in lstOfRecords:
    print(l3[l])
