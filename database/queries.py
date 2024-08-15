class Queries:
    CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_number TEXT,
    visit_date DATE,
    food_rating INTEGER,
    cleanliness_rating INTEGER,
    comments TEXT
    )
    '''
