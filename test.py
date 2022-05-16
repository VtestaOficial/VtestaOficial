import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="vtesta", user='ivan', password='lolo1639.', host='vtesta.info', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()