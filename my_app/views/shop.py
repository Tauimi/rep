"""
Blueprint для основных страниц магазина
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session, abort, send_from_directory
import os
from sqlalchemy import func
from my_app.extensions import db
from my_app.models.product import Product
from my_app.models.category import Category
from my_app.models.visitor import Visitor
from my_app.models.review import Review
from my_app.models.review_vote import ReviewVote
from my_app.models.rating import Rating
from my_app.models.feedback import FeedbackMessage
# Импортируем модель Brand
from my_app.models.brand import Brand

# Создаем Blueprint
shop_bp = Blueprint('shop', __name__, url_prefix='')

@shop_bp.route('/')
def home():
    """Главная страница"""
    # Получаем популярные товары
    featured_products = Product.query.filter_by(is_featured=True).limit(8).all()
    
    # Получаем новинки
    new_products = Product.query.filter_by(is_new=True).order_by(Product.created_at.desc()).limit(8).all()
    
    # Получаем товары со скидкой
    sale_products = Product.query.filter_by(is_sale=True).order_by(Product.created_at.desc()).limit(8).all()
    
    # Получаем категории для меню
    categories = Category.query.filter_by(parent_id=None).all()
    
    # Получаем все товары для отображения на главной странице
    products = featured_products
    
    # Статистика
    stats = {
        'products_count': Product.query.count(),
        'categories_count': Category.query.count(),
    }
    
    # Получаем статистику посетителей
    try:
        visitor_stats = Visitor.get_visitors_stats()
        stats.update(visitor_stats)
    except Exception as e:
        current_app.logger.error(f"Ошибка получения статистики посетителей: {str(e)}")
    
    return render_template('index.html', 
                          featured_products=featured_products,
                          new_products=new_products,
                          sale_products=sale_products,
                          categories=categories,
                          products=products,
                          stats=stats)

@shop_bp.route('/catalog')
def catalog():
    """Страница каталога"""
    # Получаем параметры сортировки и фильтрации из запроса
    sort_by = request.args.get('sort', 'default')
    brand_ids = request.args.getlist('brand_id')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    # Получаем все категории верхнего уровня
    categories = Category.query.filter_by(parent_id=None).all()

    # Получаем все бренды для фильтрации
    brands = Brand.query.order_by(Brand.name).all()

    # Базовый запрос товаров
    products_query = Product.query

    # Применяем фильтры
    if brand_ids:
        products_query = products_query.filter(Product.brand_id.in_(brand_ids))

    if min_price and min_price.isdigit():
        products_query = products_query.filter(Product.price >= float(min_price))

    if max_price and max_price.isdigit():
        products_query = products_query.filter(Product.price <= float(max_price))

    # Применяем сортировку
    if sort_by == 'rating_high':
        # Сортировка по рейтингу (от высокого к низкому)
        products = sorted(products_query.all(), key=lambda p: p.avg_rating, reverse=True)
    elif sort_by == 'rating_low':
        # Сортировка по рейтингу (от низкого к высокому)
        products = sorted(products_query.all(), key=lambda p: p.avg_rating)
    elif sort_by == 'reviews_high':
        # Сортировка по количеству положительных отзывов (отзывы с рейтингом 4-5)
        try:
            products = sorted(
                products_query.all(),
                key=lambda p: len([r for r in p.reviews if r.rating >= 4]),
                reverse=True
            )
        except:
            # Если у товара нет связи reviews, используем другую сортировку
            products = products_query.order_by(Product.created_at.desc()).all()
    elif sort_by == 'price_high':
        # Сортировка по цене (от высокой к низкой)
        products = products_query.order_by(Product.price.desc()).all()
    elif sort_by == 'price_low':
        # Сортировка по цене (от низкой к высокой)
        products = products_query.order_by(Product.price).all()
    elif sort_by == 'newest':
        # Сортировка по новизне
        products = products_query.order_by(Product.created_at.desc()).all()
    else:
        # По умолчанию - без сортировки
        products = products_query.all()

    return render_template('catalog.html', 
                          categories=categories,
                          brands=brands,
                          products=products,
                          sort_by=sort_by)

@shop_bp.route('/category/<int:category_id>')
def category(category_id):
    """Страница категории"""
    # Получаем параметры сортировки и фильтрации из запроса
    sort_by = request.args.get('sort', 'default')
    brand_ids = request.args.getlist('brand_id')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')

    category = Category.query.get_or_404(category_id)

    # Получаем все бренды для фильтрации
    brands = Brand.query.order_by(Brand.name).all()

    # Базовый запрос товаров в этой категории
    products_query = Product.query.filter_by(category_id=category_id)

    # Применяем фильтры
    if brand_ids:
        products_query = products_query.filter(Product.brand_id.in_(brand_ids))

    if min_price and min_price.isdigit():
        products_query = products_query.filter(Product.price >= float(min_price))

    if max_price and max_price.isdigit():
        products_query = products_query.filter(Product.price <= float(max_price))

    # Применяем сортировку
    if sort_by == 'rating_high':
        # Сортировка по рейтингу (от высокого к низкому)
        products = sorted(products_query.all(), key=lambda p: p.avg_rating, reverse=True)
    elif sort_by == 'rating_low':
        # Сортировка по рейтингу (от низкого к высокому)
        products = sorted(products_query.all(), key=lambda p: p.avg_rating)
    elif sort_by == 'reviews_high':
        # Сортировка по количеству положительных отзывов (отзывы с рейтингом 4-5)
        try:
            products = sorted(
                products_query.all(),
                key=lambda p: len([r for r in p.reviews if r.rating >= 4]),
                reverse=True
            )
        except:
            # Если у товара нет связи reviews, используем другую сортировку
            products = products_query.order_by(Product.created_at.desc()).all()
    elif sort_by == 'price_high':
        # Сортировка по цене (от высокой к низкой)
        products = products_query.order_by(Product.price.desc()).all()
    elif sort_by == 'price_low':
        # Сортировка по цене (от низкой к высокой)
        products = products_query.order_by(Product.price).all()
    elif sort_by == 'newest':
        # Сортировка по новизне
        products = products_query.order_by(Product.created_at.desc()).all()
    else:
        # По умолчанию - без сортировки
        products = products_query.all()

    # Получаем подкатегории
    subcategories = Category.query.filter_by(parent_id=category_id).all()

    return render_template('category.html', 
                          category=category, 
                          products=products, 
                          subcategories=subcategories,
                          brands=brands,
                          sort_by=sort_by)

@shop_bp.route('/product/<int:product_id>')
def product(product_id):
    """Страница товара"""
    product = Product.query.get_or_404(product_id)
    
    # Добавляем товар в список просмотренных, если его там еще нет
    if 'visited_products' not in session:
        session['visited_products'] = []
    
    visited_products = session['visited_products']
    if product_id not in visited_products:
        visited_products.append(product_id)
        session['visited_products'] = visited_products[:10]  # Храним только 10 последних
    
    return render_template('product.html', product=product)

@shop_bp.route('/search')
def search():
    """Поиск товаров"""
    query = request.args.get('q', '')
    
    if not query:
        return redirect(url_for('shop.catalog'))
    
    # Поиск товаров с похожим названием
    products = Product.query.filter(
        Product.name.ilike(f'%{query}%') | 
        Product.description.ilike(f'%{query}%')
    ).all()
    
    # Поиск категорий с похожим названием
    categories = Category.query.filter(
        Category.name.ilike(f'%{query}%')
    ).all()
    
    return render_template('search_results.html', 
                          query=query, 
                          products=products, 
                          categories=categories)

@shop_bp.route('/carousel/<int:slide_id>')
def get_carousel_image(slide_id):
    """Возвращает изображение для карусели"""
    # Словарь с именами файлов для каждого слайда
    carousel_images = {
        1: 'carousel-1.jpg',
        2: 'carousel-2.jpg',
        3: 'carousel-3.jpg'
    }
    
    # Получаем имя файла или используем запасное изображение
    image_name = carousel_images.get(slide_id, 'carousel-default.jpg')
    
    # Путь к директории с изображениями карусели
    carousel_dir = os.path.join(current_app.static_folder, 'images', 'carousel')
    
    # Если директория не существует, создаем ее
    if not os.path.exists(carousel_dir):
        os.makedirs(carousel_dir)
        
        # Если файлы не существуют, используем запасное изображение
        if not os.path.exists(os.path.join(carousel_dir, image_name)):
            image_name = 'default.jpg'
    
    return send_from_directory(os.path.join(current_app.static_folder, 'images', 'carousel'), image_name)