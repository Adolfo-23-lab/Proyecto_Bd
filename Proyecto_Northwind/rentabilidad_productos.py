import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn= sqlite3.connect('northwind.db')
query= '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query,conn)

conn.close()

top_products.plot(x='ProductName',y='Revenue',kind='bar',figsize=(5,3),legend=False)

plt.title('Los 10 productos más rentables')
plt.xlabel('Productos')
plt.ylabel('Revenue')
plt.xticks(rotation=90)
plt.savefig('top_productos.png')
plt.show()