"""
WSGI-файл для запуска приложения через Gunicorn
"""
import os
import sys

# Автоматическое заполнение настроек перед импортом приложения
try:
    from auto_config import setup_railway_config
    setup_railway_config()
    print("✅ Автоматическая настройка успешно применена")
except Exception as e:
    print(f"⚠️ Ошибка при автоматической настройке: {str(e)}")

# Импортируем фабрику приложения после настройки переменных окружения
from my_app import create_app
from my_app.extensions import db

# Создаем экземпляр приложения
app = create_app(os.getenv('APP_SETTINGS', 'development'))

# Определяем стандартную переменную application для совместимости с WSGI серверами
application = app

# Проверяем наличие подключения к базе данных
database_url = os.environ.get('DATABASE_URL')
if database_url:
    print("✅ База данных настроена, инициализируем схему...")
    with app.app_context():
        try:
            db.create_all()
            print("✅ Схема базы данных создана/обновлена")

            # Проверяем наличие данных в базе и заполняем при необходимости
            from my_app.models import Category, Product
            products_count = Product.query.count()
            categories_count = Category.query.count()

            if products_count == 0 or categories_count == 0:
                print("⚙️ Заполняем базу данных тестовыми данными...")
                try:
                    # Импортируем и запускаем скрипт заполнения базы данных
                    from seed_db_railway import seed_database_railway
                    seed_database_railway()
                    print("✅ База данных заполнена успешно")
                except Exception as e:
                    print(f"❌ Ошибка при заполнении базы данных: {str(e)}")
            else:
                print("✅ База данных уже содержит данные, пропускаем заполнение")
        except Exception as e:
            print(f"❌ Ошибка при инициализации базы данных: {str(e)}")
                print(f"ℹ️ База данных уже содержит {categories_count} категорий и {products_count} товаров")

        except Exception as e:
            print(f"❌ Ошибка инициализации базы данных: {str(e)}")
            print("   Приложение запущено в демо-режиме")
else:
    print("ℹ️ База данных не настроена")
    print("   Приложение запущено в демо-режиме с локальной SQLite базой")

if __name__ == "__main__":
    app.run()