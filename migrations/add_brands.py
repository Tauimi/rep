
#!/usr/bin/env python
"""
Миграционный скрипт для добавления таблицы брендов и связи с продуктами
"""
import os
import sys
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from my_app import create_app, db
from my_app.models.brand import Brand

# Создаем экземпляр приложения
app = create_app(os.getenv('APP_SETTINGS', 'development'))

def create_brands_table():
    """Создание таблицы брендов и добавление колонки brand_id в таблицу products"""
    with app.app_context():
        try:
            # Проверяем наличие таблицы brands
            if not db.engine.dialect.has_table(db.engine.connect(), 'brands'):
                # Создаем таблицу brands
                db.engine.execute('''
                CREATE TABLE brands (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) NOT NULL,
                    slug VARCHAR(100) NOT NULL UNIQUE,
                    description TEXT,
                    logo VARCHAR(255)
                )
                ''')
                print("Таблица 'brands' успешно создана")
            else:
                print("Таблица 'brands' уже существует")

            # Проверяем наличие колонки brand_id в таблице products
            result = db.engine.execute("PRAGMA table_info(products)")
            columns = [column[1] for column in result.fetchall()]
            
            if 'brand_id' not in columns:
                # Добавляем колонку brand_id в таблицу products
                db.engine.execute('''
                ALTER TABLE products
                ADD COLUMN brand_id INTEGER REFERENCES brands(id)
                ''')
                print("Колонка 'brand_id' добавлена в таблицу 'products'")
            else:
                print("Колонка 'brand_id' уже существует в таблице 'products'")

            # Добавляем базовые бренды
            default_brands = [
                {'name': 'Apple', 'slug': 'apple', 'logo': 'apple.png'},
                {'name': 'Samsung', 'slug': 'samsung', 'logo': 'samsung.png'},
                {'name': 'Xiaomi', 'slug': 'xiaomi', 'logo': 'xiaomi.png'},
                {'name': 'Huawei', 'slug': 'huawei', 'logo': 'huawei.png'},
                {'name': 'Sony', 'slug': 'sony', 'logo': 'sony.png'},
                {'name': 'LG', 'slug': 'lg', 'logo': 'lg.png'},
                {'name': 'Dell', 'slug': 'dell', 'logo': 'dell.png'},
                {'name': 'HP', 'slug': 'hp', 'logo': 'hp.png'},
                {'name': 'Lenovo', 'slug': 'lenovo', 'logo': 'lenovo.png'},
                {'name': 'Asus', 'slug': 'asus', 'logo': 'asus.png'},
                {'name': 'Acer', 'slug': 'acer', 'logo': 'acer.png'},
                {'name': 'MSI', 'slug': 'msi', 'logo': 'msi.png'},
                {'name': 'Google', 'slug': 'google', 'logo': 'google.png'},
                {'name': 'OnePlus', 'slug': 'oneplus', 'logo': 'oneplus.png'},
                {'name': 'Realme', 'slug': 'realme', 'logo': 'realme.png'},
                {'name': 'Oppo', 'slug': 'oppo', 'logo': 'oppo.png'},
                {'name': 'Vivo', 'slug': 'vivo', 'logo': 'vivo.png'},
                {'name': 'Nokia', 'slug': 'nokia', 'logo': 'nokia.png'},
                {'name': 'Motorola', 'slug': 'motorola', 'logo': 'motorola.png'},
                {'name': 'Bose', 'slug': 'bose', 'logo': 'bose.png'},
                {'name': 'JBL', 'slug': 'jbl', 'logo': 'jbl.png'},
                {'name': 'Sennheiser', 'slug': 'sennheiser', 'logo': 'sennheiser.png'},
                {'name': 'Audio-Technica', 'slug': 'audio-technica', 'logo': 'audio-technica.png'},
                {'name': 'Beats', 'slug': 'beats', 'logo': 'beats.png'},
                {'name': 'Razer', 'slug': 'razer', 'logo': 'razer.png'},
                {'name': 'Microsoft', 'slug': 'microsoft', 'logo': 'microsoft.png'},
                {'name': 'Logitech', 'slug': 'logitech', 'logo': 'logitech.png'},
                {'name': 'Corsair', 'slug': 'corsair', 'logo': 'corsair.png'},
                {'name': 'SteelSeries', 'slug': 'steelseries', 'logo': 'steelseries.png'},
                {'name': 'Anker', 'slug': 'anker', 'logo': 'anker.png'}
            ]
            
            # Проверяем наличие брендов в базе данных
            existing_brands = db.session.query(Brand).count()
            if existing_brands == 0:
                for brand_data in default_brands:
                    brand = Brand(**brand_data)
                    db.session.add(brand)
                
                db.session.commit()
                print(f"Добавлено {len(default_brands)} брендов")
            else:
                print(f"В базе данных уже есть {existing_brands} брендов")
                
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Ошибка при миграции: {str(e)}")
            return False

if __name__ == "__main__":
    with app.app_context():
        success = create_brands_table()
        if success:
            print("Миграция успешно выполнена")
        else:
            print("Миграция не выполнена из-за ошибок")
