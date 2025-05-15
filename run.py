
#!/usr/bin/env python
"""
Файл для локального запуска приложения
"""
import os
from my_app import create_app, db

# Создаем экземпляр приложения
app = create_app(os.getenv('APP_SETTINGS', 'development'))

if __name__ == "__main__":
    # Создаем таблицы базы данных перед запуском
    with app.app_context():
        try:
            db.create_all()
            print("✅ База данных инициализирована успешно")
        except Exception as e:
            print(f"❌ Ошибка при инициализации базы данных: {str(e)}")
    
    # Запускаем приложение на порту 5000, доступном извне
    app.run(host='0.0.0.0', port=5000, debug=True)
