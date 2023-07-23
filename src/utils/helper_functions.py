from database.mariadb_conn import MariaDBConnManager
maria_db = MariaDBConnManager()

def retrieve_suggested_words_from_database(search_query):
    if len(search_query) >= 2:
        conn = maria_db.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT item FROM info1 WHERE item LIKE %s ORDER BY item LIMIT 10", ('%' + search_query.replace(' ', '%') + '%',))
        suggested_words = [row[0] for row in cur.fetchall()]
        return suggested_words
    return False
