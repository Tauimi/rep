
"""
Модель бренда товаров
"""
from my_app.extensions import db

class Brand(db.Model):
    """Модель бренда товаров"""
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    logo = db.Column(db.String(255), nullable=True)

    # Связи
    products = db.relationship('Product', backref='brand', lazy=True)

    def __repr__(self):
        return f'<Brand {self.name}>'
