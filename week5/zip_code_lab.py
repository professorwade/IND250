from collections import namedtuple

# defined zip code record
ZipRecord = namedtuple('zrecord', ['zipcode', 'city', 'state'])

# create zip dictionary with zip code key and city and state being the value
zip_db = {}
city_db = {}
cities = set()

# open raw text file and read in
f = open('ZIP_Locale_Detail.txt', 'r')

# read each line and parse fields into data records
for line in f:
    fields = line.split("\t") # returns a list of fields separated by tabs
    if fields[0].isdigit(): # filter out headings
        zipcode = int(fields[0]) # zip code field as number
        city = fields[1] # city field
        state = fields[2].strip() # state field stripping off carriage return
        zip_db[zipcode] = ZipRecord(zipcode, city, state) # add record to dictionary
        cities.add(city) # add city to set of cities

        # add code here to create a dictionary with city names as keys

print('Records: ', len(zip_db), 'Unique Cities: ', len(cities))

""" Write menu code such that the menu automatically looks for the zip code if a 
number is entered, quits if 'quit' is entered, or looks for the city if text is 
entered"""
        
zipcode = -1 # continuation flag
while zipcode != 0: # while loop
    zipcode = int(input('Enter Zip Code: '))
    if zipcode in zip_db: # test for being in database
        print('Data for code:',zipcode,'is',zip_db[zipcode].city, zip_db[zipcode].state)
