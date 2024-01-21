import pyodbc
import csv

conn = pyodbc.connect('Driver={MyDriver};'
                      'Server=MyServer;'
                      'Database=TESTDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM [dbo].myTable')
rows = cursor.fetchall()
csv_filename = 'output.csv'

with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for row in rows :
        csv_writer.writerow(row)
print(f'Data has been written to {csv_filename}')

conn.close()
