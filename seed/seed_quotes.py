import sqlite3

# Connect to database
conn = sqlite3.connect("database/quotes.db")
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT NOT NULL,
    source TEXT,
    commentary TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS quote_tags (
    quote_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (quote_id) REFERENCES quotes(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id)
)
""")

# Sample quote data with tags
sample_quotes = [
    {
        "quote": "The Perfect man has no self; the Spirit-like man, none of merit; the Sagely-minded man, none of fame.",
        "source": "Zhuangzi, Chapter 1",
        "commentary": "So basically, {{ username }}, the more you try, the less you get. It's unfortunate, I know.",
        "tags": ["self", "detachment", "fame"]
    },
    {
        "quote": "A frog in a well cannot be talked with about the sea - he is confined to the limits of his hole",
        "source": "Zhuangzi, Chapter 17",
        "commentary": "Get out of the well, {{ username }}.",
        "tags": ["ignorance", "perspective", "humor"]
    },
    {
        "quote": "You’re not a fish; how do you know what a fish enjoys?",
        "source": "Zhuangzi, Chapter 17",
        "commentary": "{{ username }}, You don’t know me. I don’t know you. Let’s stop pretending.",
        "tags": ["assumption", "subjectivity", "perspective"]
    },
    {
        "quote": "Formerly, I, Zhuang Zhou, dreamt that I was a butterfly, a butterfly flying about, feeling that it was enjoying itself",
        "source": "Zhuangzi, Chapter 2",
        "commentary": "Are you dreaming? {{ username }}, or being dreamed? Honestly, it doesn't really matter.",
        "tags": ["dream", "illusion", "directionlessness"]
    },
    {
        "quote": "Zhuangzi on the unchoppable tree: Neither bill nor axe would shorten its existence; there would be nothing to injure it. What is there in its uselessness to cause you distress?",
        "source": "Zhuangzi, Chapter 1",
        "commentary": "Maybe you are not useless, {{ username }}, maybe you are just unchoppable.",
        "tags": ["uselessness", "non-action", "acceptance"]
    },
    {
        "quote": "When the springs are dried up, the fishes collect together on the land. Than that they should moisten one another there by the damp about them, and keep one another wet by their slime, it would be better for them to forget one another in the rivers and lakes",
        "source": "Zhuangzi, Chapter 6",
        "commentary": "Let go, {{ username }}. The puddle isn't the goal. It never was.",
        "tags": ["struggle", "urgency", "surrender"]
    },
    {
        "quote": "Words are like the waves acted on by the wind; the real point of the matters discussed by them is lost. The wind and waves are easily set in motion; the success of the matter is thus easily put in peril.",
        "source": "Zhuangzi, Chapter 2 (Discussion on Making All Things Equal)",
        "commentary": "Aw, {{ username }}. Look at you trying so hard to make sense of it all. Maybe let the waves do their thing and float a little?",
        "tags": ["paradox", "confusion", "insight"]
    },
    {
        "quote": "The True Man of old did not dream when he slept, had no anxiety when he awoke, and did not care that his food should be pleasant. His breathing came from his heels — unlike ordinary men, who breathe from their throats.",
        "source": "Zhuangzi, Chapter 6 (The Great Ancestral Teacher)",
        "commentary": "Look, {{ username }}, no stress dreams, no picky eating, and heel-breathing. Not saying you gotta get there, just… maybe unclench a little?",
        "tags": ["freedom", "detachment", "non-action"]
    },
    {
        "quote": "The True men of old did not reject the views of the few; they did not seek to accomplish their ends like heroes; they did not lay plans to attain those ends. Though they might make mistakes, they had no occasion for repentance.",
        "source": "Zhuangzi, Chapter 6 (The Great and Venerable Teacher)",
        "commentary": "You don’t have to fix it all, {{ username }}. No grand plans, no need to be a hero — just don’t spiral when you mess up.",
        "tags": ["chaos", "resistance", "stagnation"]

    }

]

# Insert quotes and related tags
for q in sample_quotes:
    cur.execute("INSERT INTO quotes (quote, source, commentary) VALUES (?, ?, ?)", 
                (q["quote"], q["source"], q["commentary"]))
    quote_id = cur.lastrowid

    for tag in q["tags"]:
        cur.execute("INSERT OR IGNORE INTO tags (name) VALUES (?)", (tag,))
        cur.execute("SELECT id FROM tags WHERE name = ?", (tag,))
        tag_id = cur.fetchone()[0]
        cur.execute("INSERT INTO quote_tags (quote_id, tag_id) VALUES (?, ?)", (quote_id, tag_id))

# Finalize and close
conn.commit()
conn.close()

print("Database seeded successfully!")
