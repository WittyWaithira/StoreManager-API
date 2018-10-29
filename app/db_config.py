import psycopg2
import os

#url = os.getenv('DATABASE_URL')
db_url = "dbname='storemanager' host='localhost' port='5432' user='postgres' password='mitchmellah'"

def connection(db_url):
    """Get database connection"""
    con = psycopg2.connect(db_url)
    return con


def init_db():
    """Get database connection"""
    con = connection(db_url)
    return con


def create_tables():
    """Create tables and commit"""
    conn = connection(db_url)
    curr = conn.cursor() #to connect the db
    queries = tables()

    for query in queries:
        curr.execute(query)
    conn.commit()


def delete_tables():
    """Delete tables"""

    conn = connection(db_url)
    curr = conn.cursor()

    users_db = """DROP TABLE IF EXISTS users CASCADE"""
    sales_db = """DROP TABLE IF EXISTS sales CASCADE"""
    product_db = """DROP TABLE IF EXISTS products CASCADE"""

    # Add all tables to the queries list
    queries = [users_db, product_db, sales_db]

    for query in queries:
        curr.execute(query)
    conn.commit()


def tables():
    """Create tables"""
    db1 = """CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY NOT NULL,
            name VARCHAR (120) NOT NULL,
            email VARCHAR (50) UNIQUE NOT NULL,
            role VARCHAR (15) UNIQUE NOT NULL,
            password VARCHAR (20) NOT NULL
    )"""

    db2 = """CREATE TABLE IF NOT EXISTS sales (
            id serial PRIMARY KEY NOT NULL,
            items VARCHAR (100),
            items_sold numeric (3) NOT NULL,
            transaction_amount numeric (6) NOT NULL,
            date_created TIMESTAMP with time zone DEFAULT('now'::text)::date NOT NULL,
            user_id INTEGER REFERENCES users(id)
    )"""

    db3 = """CREATE TABLE IF NOT EXISTS products (
            id serial PRIMARY KEY NOT NULL,
            name VARCHAR (150) UNIQUE NOT NULL,
            category VARCHAR (80) NOT NULL,
            quantity numeric (4) NOT NULL,
            price numeric (6) NOT NULL,
            sale_id INTEGER REFERENCES sales(id)
    )"""

    # Add all tables to the queries list
    queries = [db1, db2, db3]
    return queries
