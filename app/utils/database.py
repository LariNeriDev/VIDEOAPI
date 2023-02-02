from pymongo import MongoClient

def get_db():
    # Conectando ao banco de dados MongoDB
    client = MongoClient("mongodb://mongo:27017/")
    # Selecionando o banco de dados "video_posts_db"
    db = client["video_posts_db"]
    return db

def get_posts_collection():
    # Obtendo a coleção de posts do banco de dados
    db = get_db()
    posts_collection = db["posts"]
    return posts_collection

def get_users_collection():
    # Obtendo a coleção de usuários do banco de dados
    db = get_db()
    users_collection = db["users"]
    return users_collection