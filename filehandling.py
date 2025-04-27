import struct
import csv

fp = open("data.txt", "w")
fp.write("Hello world")
fp.write("\nThis is a test file.")
fp.write("\nThis file is used for testing file handling in python")
fp.close()

fp=open("data.txt", "a")
fp.write("\nThis will overwrite the previous content.")
fp.close()

fp=open("data.txt","r")
str = fp.read()
print(str)
fp.close()

fp=open("data.txt","r")
str = fp.readline()
while str:
    print(str)
    str = fp.readline()

fp.close()

fp = open("binaryfile.txt", "wb")
data = struct.pack(f"i{len('ravi')}sf",1,"ravi".encode("utf-8"),3.14)
fp.write(data)
fp.close()
#if we check the size of binary file will be 12 bytes-> 4 + 8 + 4 (int 4)(ravi 2*4 = 8)(float 4)

fp=open("binaryfile.txt", "rb")
data = fp.read()
print(data)
data = struct.unpack(f"i{len('ravi')}sf",data)
print(data[0],data[1].decode("utf-8"),data[2])
fp.close()

fp = open("student.csv","r",newline = "")
csvreader = csv.reader(fp)
for row in csvreader:
    print(row)

fp.close()

fp = open("student.csv","a",newline = "")
csvwriter = csv.writer(fp)
csvwriter.writerow(["1004","Doe",12500])
csvwriter.writerow(["1005","John",2500])
csvwriter.writerow(["1006","Sindhu",2500])

fp.close()

fp = open("student.csv","r",newline = "")
csvreader = csv.reader(fp)
for row in csvreader:
    print(row)

fp.close()