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

    DROP_FOOD_CATEGORIES_TABLE = '''
    DROP TABLE IF EXISTS food_categories
    '''

    CREATE_FOOD_CATEGORIES_TABLE = '''
    CREATE TABLE IF NOT EXISTS food_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    )
    '''

    POPULATE_FOOD_CATEGORIES = '''
    INSERT INTO food_categories(name) VALUES 
    ('Супы'),
    ('Основные блюда'),
    ('Десерты'),
    ('Салаты'),
    ('Лимонады')
    '''

    DROP_MENU_TABLE = '''
    DROP TABLE IF EXISTS menu
    '''

    CREATE_MENU_TABLE = '''
    CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    image TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES food_categories(id)
    )
    '''

    POPULATE_MENU = '''
    INSERT INTO menu (name, price, image, category_id) VALUES
    ('Томатный суп с морепродуктами', 400, 'menu_images/томатный.jpg', 1),
    ('Суп минестроне', 220, 'menu_images/минестроне.jpg', 1),
    ('Пицца Маргарита', 400, 'menu_images/маргарита.jpg', 2),
    ('Пенне арабьята', 350, 'menu_images/пенне_арабьята.jpg', 2),
    ('Ризотто с креветками', 420, 'menu_images/ризотто.jpg', 2),
    ('Тирамису', 220, 'menu_images/тирамису.jpg', 3),
    ('Торт белый лес', 220, 'menu_images/белый_лес.jpg', 3),
    ('Севиче из форели с авокадо', 580, 'menu_images/севиче.jpg', 4),
    ('Капрезе', 450, 'menu_images/капрезе.jpg', 4),
    ('Лимонад ананас-манго', 250, 'menu_images/анман.jpg', 5),
    ('Лимонад цитрус-базилик', 200, 'menu_images/цитбаз.jpg', 5)
    '''