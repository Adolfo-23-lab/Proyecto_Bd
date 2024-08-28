import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn= sqlite3.connect('northwind.db')
query2= '''
    SELECT FirstName || ' ' || LastName as Employee, COUNT(*) as Total
    From Orders o
    JOIN Employees e 
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
'''

top_employees = pd.read_sql_query(query2,conn)

conn.close()

top_employees.plot(x='Employee',y='Total',kind='line',figsize=(5,3),legend=False)

plt.title('Los 10 empleados más productivos')
plt.xlabel('Empleados')
plt.ylabel('Total vendido')
plt.xticks(rotation=45)
plt.savefig('top_empleados.png')
plt.plot('Margaret Peacock',40,'o')
plt.show()