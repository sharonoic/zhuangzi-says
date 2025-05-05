import sqlite3
import random

tag_map = {
        "Stressed": ["chaos", "resistance"],
        "Bored": ["detachment", "stagnation"],
        "Lost": ["illusion", "directionlessness"],
        "Content": ["acceptance", "non-action"],

        "Freedom": ["uselessness", "non-action"],
        "Meaning": ["paradox", "confusion"],
        "Clarity": ["detachment", "insight"],
        "Sleep": ["surrender", "illusion"],

        "Butterfly dream": ["illusion", "dream"],
        "Useless tree": ["uselessness", "freedom"],
        "Fish in a drying pond": ["struggle", "urgency"],
        "Frog in a well": ["ignorance", "perspective"]
    }

def map_answers_to_tags(answers):

    tags = []
    for ans in answers:
        if ans in tag_map:
            tags.extend(tag_map[ans])
    return tags

def get_matching_quote(tags):
    conn = sqlite3.connect("database/quotes.db") # connects to database/ folder
    cur = conn.cursor() # cursor object --> runs SQL commands

    q_marks = ','.join(['?'] * len(tags)) # prevents SQL injection
    query = f"""
    SELECT q.quote, q.source, q.commentary
    FROM quotes q
    JOIN quote_tags qt ON q.id = qt.quote_id
    JOIN tags t ON qt.tag_id = t.id
    WHERE t.name IN ({q_marks})
    GROUP BY q.id
    ORDER BY RANDOM()
    LIMIT 1;
    """

    cur.execute(query, tags)
    result = cur.fetchone()
    conn.close()

    return result