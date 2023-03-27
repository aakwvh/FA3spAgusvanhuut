import psycopg2
import time

""""
in dit ga ik eerst zoeken naar profiel dat soortgelijk activiteit hebben dus hetzelfde product gekeken en zelfde product geviewed door een innerjoin te maken
regels 
er wordt eerst gekeken welke profiel naar de zelfde producten heeft gekocht en geviewed return het profiel die het meest aantal gelijk producten heeft 

zijn er proefuelen in de profielen database die lijken op een ingelogde persoon dus gebaseerd op  zelfde producten heeft gekocht en geviewed
stap 1 we gaan kijken naar een profiel
stap 2 welke profielen lijken er op 
stap 3 welke producten horen daarbij
"""


# maak een connectie met postgres
con = psycopg2.connect(
    host='localhost',
    database='webshopdb',
    user='postgres',
    password='avhE07'
)
cur = con.cursor()

def geef_soort_gelijke_profiel(profiel_id):
    """
    hier in wordt er gezpcht naar profiel die het meest overeenkomen met de bezoekers profiel
    dus er wordt eerst een innerjoin gemaakt en
    dan wordt er gekeken welke profiel heeft de meeste product_id gekocht als de bezoekers profiel

    """
    cur.execute(f"""
SELECT 
    pp1.profile_id AS profile_id1, 
    pp2.profile_id AS profile_id2, 
    COUNT(DISTINCT pp1.product_id) AS aantal_gelijke_producten
FROM 
    profile_product AS pp1 
    INNER JOIN profile_product AS pp2 
        ON pp1.product_id = pp2.product_id 
        AND pp1.profile_id < pp2.profile_id 
WHERE
    pp1.profile_id = '{profiel_id}'
GROUP BY 
    pp1.profile_id, pp2.profile_id 
HAVING 
    COUNT(DISTINCT pp1.product_id) >= 5 
ORDER BY 
    aantal_gelijke_producten DESC 
    LIMIT 1;
    

"""
)
    rows = cur.fetchall()
    soort_gelijk = list()

    for item in rows:
        soort_gelijk.append(item[1])
    return(soort_gelijk)


print("profiel die het meest overeenkomt is:",geef_soort_gelijke_profiel("5a393d68ed295900010384ca"))


def geef_productid(soort_gelijk):
    """
    hier in wordt eer uit de database alle product_id die is gekocht of geviewed door profiel soort_gelijk
    """
    cur.execute(f"""
    select distinct product_id from profile_product
    where profile_id = '{soort_gelijk[0]}';
"""
)
    rows = cur.fetchall()
    collaborative_filtering = list()

    for item in rows:
        collaborative_filtering.append(item[0])
    return(collaborative_filtering)

def collaborative(profile_id):
    soort_profiel = geef_soort_gelijke_profiel(profile_id)
    vergelijkbaar_producten = geef_productid(soort_profiel)
    return vergelijkbaar_producten


start = time.time()
print("product_id die door soort gelijke profiel wordt bekeken is:",collaborative('5a393d68ed295900010384ca'))

end = time.time()
print(f"time to complete = {end - start}")

con.commit()
con.close()
