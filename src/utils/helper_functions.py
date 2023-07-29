import os
import shutil

import utils.constant as const
import utils.mariadb_queries as maria_q
import re


def get_suggestions(search_query):
    if len(search_query) >= 2:
        suggested_words = [row[0] for row in maria_q.suggestion(search_query)]

        return suggested_words
    return False


def tmp_recycle(filename):
    filepath = os.path.join(const.SRC_PATH, "tmp")

    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    os.mkdir(filepath)

    return os.path.join(filepath, filename)


def missing_fields(fields: dict):
    missing = []

    if fields.get("form_fields") != None and fields.get("form_req") != None:
        missing += [
            field for field in fields["form_fields"] if field not in fields["form_req"]
        ]
    if fields.get("file_fields") != None and fields.get("file_req") != None:
        for file in fields["file_fields"]:
            fname = fields["file_req"][file].filename
            if fname == "":
                missing.append(file)

    if len(missing) != 0:
        return missing
    return False

def parse_html_table(regular_expression, html_str):
    # Find all matches of the row pattern
    matches = re.findall(regular_expression, html_str)

    # Create a dictionary from the matches
    data_dict = {}
    for key, value in matches:
        key = re.sub(r'<.*?>', '', key)  # Remove HTML tags from key
        value = re.sub(r'<.*?>', '', value)  # Remove HTML tags from value
        data_dict[key.strip()] = value.strip()

    return data_dict



