from collections import namedtuple

# defined zip code record
ZipRecord = namedtuple('zrecord', ['zipcode', 'city', 'state'])

# create zip dictionary with zip code key and city and state being the value
zip_db = {}
cities = set()

# open raw text file and read in
f = open('ZIP_Locale_Detail.txt', 'r')

# read each line and parse fields into data records
for line in f:
    fields = line.split("\t") # returns a list of fields separated by tabs
    if fields[0].isdigit(): # filter out headings
        zip = int(fields[0]) # zip code field as number
        city = fields[1] # city field
        state = fields[2].strip() # state field stripping off carriage return
        zip_db[zip] = ZipRecord(zip, city, state) # add record to dictionary
        cities.add(city) # add city to set of cities

print('Records: ', len(zip_db), 'Unique Cities: ', len(cities))

zip = -1 # continuation flag
while zip != 0: # while loop
    zip = int(input('Enter Zip Code: '))
    if zip in zip_db: # test for being in database
        print('Data for code:',zip,'is',zip_db[zip].city, zip_db[zip].state)
