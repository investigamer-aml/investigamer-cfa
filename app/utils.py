""" Module to store all small utility helper functions
"""
from flask import current_app as app
from werkzeug.security import generate_password_hash


def set_password(password):
    """Generate a hash of a user password to save into the db"""
    return generate_password_hash(password)


# Flatten the JSON objects for easier comparison
def flatten_json(y):
    """Extract all objects from a json and flatten it out"""
    out = {}

    def flatten(x, name=""):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + ".")
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def json_contains(json_obj, query, threshold=0.75):
    """Check if json_obj contains at least the threshold percentage of key-value pairs in query."""

    flat_json_obj = flatten_json(json_obj)
    flat_query = flatten_json(query)

    total_keys = len(flat_query)
    matching_keys = sum(
        1
        for key in flat_query
        if key in flat_json_obj and flat_json_obj[key] == flat_query[key]
    )

    similarity = matching_keys / total_keys if total_keys > 0 else 0
    formatted_similarity = f"{similarity:.2%}"
    app.logger.info(f"Similarity = {formatted_similarity}")

    return similarity >= threshold
