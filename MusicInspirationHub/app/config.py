import os

class Config:
    # Configuración básica de Flask
    DEBUG = True
    SECRET_KEY = 'Salviflaskteama2024'
    
    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:Inspiration2024!@localhost/musicinspirationhub'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración JWT (para autenticación)
    JWT_SECRET_KEY = 'Salvijwtteama2024'
