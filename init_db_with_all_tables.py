
"""
Скрипт для полной инициализации базы данных со всеми таблицами
Запустите этот скрипт после того, как основное приложение начнет работать

import os
from my_app import create_app, db
from my_app.models import User, Product, Category, Order, Visitor, Review, ReviewVote, Rating

app = create_app(os.getenv('APP_SETTINGS', 'development'))

with app.app_context():
    try:
        # Создание всех таблиц
        db.create_all()
        print("✅ Все таблицы базы данных созданы успешно")
        
        # Проверка существования таблицы visitors
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        
        if 'visitors' in inspector.get_table_names():
            print("✅ Таблица 'visitors' создана")
        else:
            print("❌ Таблица 'visitors' не создана")
            
    except Exception as e:
        print(f"❌ Ошибка при инициализации базы данных: {str(e)}")
"""
