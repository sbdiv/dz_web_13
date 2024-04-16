import pymongo
import psycopg2


mongo_client = pymongo.MongoClient("link")
mongo_db = mongo_client["first_bd"]


mongo_collection_authors = mongo_db["authors"]
mongo_data_authors = mongo_collection_authors.find()


mongo_collection_quotes = mongo_db["quotes"]
mongo_data_quotes = mongo_collection_quotes.find()

postgres_conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="567234",
    host="127.0.0.1",
    port="5432"
)
postgres_cursor = postgres_conn.cursor()


for document in mongo_data_authors:

    postgres_cursor.execute("""
        INSERT INTO your_author_table (fullname, born_date, born_location, description)
        VALUES (%s, %s, %s, %s);
    """, (document['fullname'], document['born_date'], document['born_location'], document['description']))


for document in mongo_data_quotes:
   
    author_name = document['author']
    postgres_cursor.execute("SELECT id FROM your_author_table WHERE fullname = %s", (author_name,))
    author_id = postgres_cursor.fetchone()[0]  
    quote_text = document['quote']
    
    postgres_cursor.execute("""
        INSERT INTO your_quote_table (author_id, quote)
        VALUES (%s, %s);
    """, (author_id, quote_text))


postgres_conn.commit()


mongo_client.close()
postgres_cursor.close()
postgres_conn.close()
