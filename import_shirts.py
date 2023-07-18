import json
from app_1.models import Shirts

#with open('shirts.json') as file:
#    data = json.load(file)
#    
#    for item in data:
#        shirt = Shirts(
#            image=item['image'],
#            head=item['head'],
#            discount_price=item['discount_price'],
#            orginal_price=item['orginal_price'],
#            discount=item['discount'],
#            advertise=item['advertise'],
#            int_discount_price=item['int_discount_price'],
#            int_orginal_price=item['int_orginal_price'],
#            # Add other fields as necessary
#        )
#        shirt.save()
#



import json
import csv

# Open the JSON file
with open('data_utf8.json', 'r') as json_file:
    data = json.load(json_file)

# Extract table data from JSON
# table_data = data['table_name']

# Define CSV file path
csv_file = 'data.csv'

# Write table data to CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
