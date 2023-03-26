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
    """
    deze functie zorg ervoor, wanneer je bepaalde product_id geeft dat je het soort  brand,category en sub_category terugkrijgt.
    """
    cur.execute(f"""SELECT product_id,brand, name,category,sub_category
FROM product
WHERE product_id = '{p_id}';
"""
)
    rows = cur.fetchall()
    criteria = list()

    for item in rows:
        criteria.append(item[3])
        criteria.append(item[4])
    return(criteria)

print(geef_brand_category("44130"))


def geef_vergelijkbare_product(criteria):
    """"
    in deze functie wordt er in de database gezocht naar de product id die dezelfde category en
    sub category hebben als aangegeven product id.

    """
    cur.execute(f"""SELECT product_id,brand, name,category,sub_category
    FROM product
    WHERE category = '{criteria[0]}' and sub_category = '{criteria[1]}' ;
    """
                )
    rows = cur.fetchall()
    meest_vergelijkbare_product = list()

    for item in rows:
        meest_vergelijkbare_product.append(item[0])
    return(meest_vergelijkbare_product)


