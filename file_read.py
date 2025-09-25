#Txt file reading
file = open('fruit.txt', 'r')

content = file.read()
print(content)

file.close()

'''
with open('fruit.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()
'''

#csv file reading
import csv
import io


with open('csv_data.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for sor in reader:
       if int(sor["Year"]) <= 2014:
        print(sor)