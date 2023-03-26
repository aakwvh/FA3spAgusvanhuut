import psycopg2
import time

# maak een connectie met postgres
con = psycopg2.connect(
    host='localhost',
    database='opdracht2',
    user='postgres',
    password='avhE07'
)
cur = con.cursor()

