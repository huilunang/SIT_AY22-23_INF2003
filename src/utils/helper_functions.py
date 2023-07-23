import utils.mariadb_queries as maria_q


def get_suggestions(search_query):
    if len(search_query) >= 2:
        suggested_words = [row[0] for row in maria_q.suggestion(search_query)]

        return suggested_words
    return False
