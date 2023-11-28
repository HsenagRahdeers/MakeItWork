import serial
import csv

port = input("Enter Port: ")

ser = serial.Serial(port, 115200)
ser.write(b'1')

conc = input("Enter Concentration: ")
name = conc + '_Percent_Solution.csv'

csv_name = name
csv_file = open(csv_name, 'w', newline = '')
csv_writer = csv.writer(csv_file)

try:
    for x in range(2660):
        data = ser.readline().decode().strip()
        csv_writer.writerow([data])
    else:
        print("Done Recording!")
        print(" 15 Samples Written!")
        
except KeyboardInterrupt:
    ser.close()
    csv_file.close()
