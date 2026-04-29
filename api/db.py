import psycopg2

def get_conn():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="MGCI",
        user="ING_SOFT_II",
        password="1234",
    )
