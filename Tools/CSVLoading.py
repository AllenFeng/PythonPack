import csv

filename = '1.csv'
with open(filename,'rU') as f:
    reader = csv.reader(f, delimiter=' ',quotechar='|')
    for row in reader:
        print row
