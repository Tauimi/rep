
"""
Отключенный код отслеживания посетителей, который вызывает ошибку
Позже, когда база данных будет правильно настроена, этот код можно будет снова добавить в my_app/__init__.py

# Добавление отслеживания посетителей
@app.before_request
def track_visitor():
    """Отслеживает посетителей сайта"""
    # Пропускаем запросы к статическим файлам и API
    if request.path.startswith('/static') or request.path.startswith('/api'):
        return
        
    # Получаем IP-адрес и User-Agent
    from .models import Visitor
    
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    page = request.path
    
    # Сохраняем информацию о посетителе
    visitor = Visitor(
        ip_address=ip_address,
        user_agent=user_agent,
        page_visited=page
    )
    
    # Добавляем в сессию и коммитим
    db.session.add(visitor)
    db.session.commit()
"""
