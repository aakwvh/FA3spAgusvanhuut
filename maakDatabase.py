import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='sp3',
    user='postgres',
    password='avhE07'
)

cur = con.cursor()
cur.execute(
    """
    CREATE TABLE product (
        product_id varchar,
        name varchar,
        price decimal,
        brand varchar,
        category varchar,
        sub_category varchar,
        PRIMARY KEY (product_id)
    );

    CREATE TABLE profile (
        object_id varchar,
        PRIMARY KEY (object_id)
    );


    CREATE TABLE sessions (
        session_id varchar,
        buid varchar(255),
        order_id SERIAL,
        product_id varchar,
        
        PRIMARY KEY (session_id)
    );

    CREATE TABLE session_product (
        order_id SERIAL,
        session_id varchar,
        product_id varchar,
        bought bool,
        viewed bool,
        PRIMARY KEY (order_id),
        FOREIGN KEY (session_id) REFERENCES sessions(session_id),
        FOREIGN KEY (product_id) REFERENCES product(product_id)
    );

    CREATE TABLE profile_product (
        profile_product_id SERIAL,
        profile_id varchar,
        product_id varchar,
        recommended bool,
        viewed bool,
        PRIMARY KEY (profile_product_id),
        FOREIGN KEY (profile_id) REFERENCES profile(object_id)
    );
    """
)

con.commit()
con.close()