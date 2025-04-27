import csv

products = [
    ["1001", "apple", 50],
    ["1002", "banana", 20],
    ["1003", "orange", 30],
    ["1004", "mango", 60],
    ["1005", "grapes", 45]
]

fp = open("products.csv", "w", newline = "")
csvwriter = csv.writer(fp)
csvwriter.writerows(products)
fp.close()

fp = open("products.csv", "r", newline="")
csvreader = csv.reader(fp)
for row in csvreader:
    print(row)