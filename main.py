import psycopg2
import time

# maak een connectie met postgres
con = psycopg2.connect(
    host='localhost',
    database='webshopdb',
    user='postgres',
    password='avhE07'
)
cur = con.cursor()

""""
ik wil als eerse regel voor content filtering, een lijst genereren met product dat dezelfde category en sub_category . 
regels: 
je krijgt een product_id van de gebruiker,
van die product_id kijk je naar de category en sub_category  
dan selecteer je een product id die dezelfde category en sub_category hebben en zet je dan in een nieuwe tabel die dan gebruik als recommendation 
1. maak een nieuwe tabel genaamd content filtering 
2. 
"""

def geef_brand_category(p_id):
    cur.execute(f"""SELECT product_id,brand, name,category,sub_category
FROM product
WHERE product_id = '{p_id}';
"""
)
    rows = cur.fetchall()
    content_filtering = list()

    for item in rows:
        content_filtering.append(item[1])
        content_filtering.append(item[3])
        content_filtering.append(item[4])
    return(content_filtering)

print(geef_brand_category("44130"))

