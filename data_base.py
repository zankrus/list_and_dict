

import psycopg2

con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="221052",
        host="127.0.0.1",
        port="5432"
    )



def data_base_creating():
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS GOODS  
         (ID SERIAL  PRIMARY KEY NOT NULL ,
         NAME VARCHAR NOT NULL,
         PACKAGE_HEIGHT FLOAT NOT NULL,
         PACKAGE_WIDTH FLOAT NOT NULL);''')


    cur.execute('''CREATE TABLE IF NOT EXISTS SHOPS_GOODS  
         (ID SERIAL  PRIMARY KEY NOT NULL ,
         ID_GOOD INT NOT NULL,
         LOCATION VARCHAR NOT NULL,
         AMOUTH INT NOT NULL,
         FOREIGN KEY (ID_GOOD)  REFERENCES GOODS (ID));''')

    con.commit()
    con.close()


def insert_bd(a: dict) -> None:
    cur = con.cursor()
    cur.execute(
        "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"
    )



def update_bd():
    cur = con.cursor()


