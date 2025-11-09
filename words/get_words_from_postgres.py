import psycopg2
import datetime as dt

def retrieve(count):

    # Establish connection with the Postgres database
    connection = psycopg2.connect(database="murmurate"
                                , user="postgres"
                                , password=x
                                , host="localhost"
                                , port=5432)

    # Write the query that takes a sample from the bottom 20% of recent words.
    sql = f"""
    SELECT *
    FROM (
        SELECT word, meaning FROM words
        ORDER BY LAST_USED DESC, RANDOM()
        LIMIT ROUND((SELECT COUNT(*) FROM words)*0.2)
    )
    ORDER BY RANDOM()
    LIMIT {count}
    """

    # Connect to the database and extract the words
    with connection.cursor() as cursor:
        cursor.execute(sql)
        records = cursor.fetchall()

    # Prepare an UPDATE statement to set the last_used date in the table
    date = dt.datetime.today().strftime('%Y-%m-%d')
    sql_update = ""
    for word in [record[0] for record in records]:
        sql_update += f"UPDATE words SET last_used = '{date}' WHERE word = '{word}'; "

    # Execute the last_used UPDATE
    with connection.cursor() as cursor: 
        cursor.execute(sql_update)
    connection.commit()
            
    # Return a list of the Words of the Day
    return records
