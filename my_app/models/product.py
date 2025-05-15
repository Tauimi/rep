"""
Модели товаров и спецификаций
"""
from datetime import datetime
from my_app.extensions import db

class Specification(db.Model):
    """Модель спецификаций товара"""
    __tablename__ = 'specifications'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Specification {self.name}: {self.value}>'

class Product(db.Model):
    """Модель товара"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    sku = db.Column(db.String(50), nullable=True, default=None)  # Артикул товара с явным default=None
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    old_price = db.Column(db.Float, nullable=True)
    stock = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255), nullable=True, default='default-product.jpg')
    is_featured = db.Column(db.Boolean, default=False)
    is_new = db.Column(db.Boolean, default=False)
    is_sale = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Связи
    specifications = db.relationship('Specification', backref='product', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Product {self.name}>'
        
    @property
    def brand_info(self):
        """Возвращает информацию о бренде товара или создает стандартную спецификацию"""
        if self.brand:
            return {'name': self.brand.name, 'logo': self.brand.logo}
        return {'name': 'Не указан', 'logo': 'default-brand.png'}

    @property
    def discount_percent(self):
        """Вычисляет процент скидки, если есть старая цена"""
        if self.old_price and self.old_price > self.price:
            return int(100 - (self.price / self.old_price * 100))
        return 0 

    @property
    def avg_rating(self):
        """Рассчитывает средний рейтинг товара с учетом отзывов и простых оценок"""
        try:
            from sqlalchemy import func
            from my_app.models.review import Review
            from my_app.models.rating import Rating

            # Сумма и количество оценок из обычных отзывов
            reviews_rating = db.session.query(
                func.avg(Review.rating), func.count(Review.id)
            ).filter(Review.product_id == self.id).first()

            # Сумма и количество быстрых оценок
            ratings_rating = db.session.query(
                func.avg(Rating.rating), func.count(Rating.id)
            ).filter(Rating.product_id == self.id).first()

            # Получаем значения из результатов запроса
            reviews_avg = reviews_rating[0] or 0
            reviews_count = reviews_rating[1] or 0
            ratings_avg = ratings_rating[0] or 0
            ratings_count = ratings_rating[1] or 0

            # Если нет ни одной оценки, возвращаем 0
            if reviews_count + ratings_count == 0:
                return 0

            # Рассчитываем средневзвешенное значение рейтинга
            total_avg = (reviews_avg * reviews_count + ratings_avg * ratings_count) / (reviews_count + ratings_count)
            return round(total_avg, 1)
        except:
            return 0

    @property
    def total_ratings_count(self):
        """Возвращает общее количество оценок (отзывы + быстрые оценки)"""
        try:
            from sqlalchemy import func
            from my_app.models.review import Review
            from my_app.models.rating import Rating

            reviews_count = db.session.query(func.count(Review.id)).filter(Review.product_id == self.id).scalar() or 0
            ratings_count = db.session.query(func.count(Rating.id)).filter(Rating.product_id == self.id).scalar() or 0

            return reviews_count + ratings_count
        except:
            return 0