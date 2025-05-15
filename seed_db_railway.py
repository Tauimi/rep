
#!/usr/bin/env python
"""
Скрипт для автоматического заполнения базы данных на Railway
"""
import os
import random
from slugify import slugify
from my_app import create_app, db
from my_app.models import Product, Category

# Создаем экземпляр приложения
app = create_app(os.getenv('APP_SETTINGS', 'production'))

# Категории товаров
categories_data = [
    {
        'name': 'Смартфоны',
        'description': 'Современные смартфоны с инновационными технологиями',
        'image': 'smartphones.jpg'
    },
    {
        'name': 'Ноутбуки',
        'description': 'Мощные ноутбуки для работы и развлечений',
        'image': 'laptops.jpg'
    },
    {
        'name': 'Аксессуары',
        'description': 'Полезные аксессуары для ваших устройств',
        'image': 'accessories.jpg'
    },
    {
        'name': 'Планшеты',
        'description': 'Планшеты для работы и развлечений',
        'image': 'tablets.jpg'
    },
    {
        'name': 'Наушники',
        'description': 'Наушники высокого качества для идеального звучания',
        'image': 'headphones.jpg'
    }
]

# Товары по категориям
products_data = {
    'Смартфоны': [
        {
            'name': 'Galaxy S23 Ultra',
            'description': 'Флагманский смартфон с мощным процессором и великолепной камерой',
            'price': 89990,
            'image': 'galaxy_s23.jpg',
            'stock': 25
        },
        {
            'name': 'iPhone 14 Pro',
            'description': 'Новейший iPhone с инновационным дизайном и технологиями',
            'price': 109990,
            'image': 'iphone_14.jpg',
            'stock': 15
        },
        {
            'name': 'Xiaomi 13',
            'description': 'Мощный смартфон по доступной цене',
            'price': 59990,
            'image': 'xiaomi_13.jpg',
            'stock': 30
        },
        {
            'name': 'Nothing Phone 2',
            'description': 'Инновационный дизайн и уникальная подсветка',
            'price': 69990,
            'image': 'nothing_phone.jpg',
            'stock': 18
        },
        {
            'name': 'Google Pixel 7 Pro',
            'description': 'Лучшая мобильная камера и чистый Android',
            'price': 79990,
            'image': 'pixel_7.jpg',
            'stock': 12
        }
    ],
    'Ноутбуки': [
        {
            'name': 'MacBook Pro 16',
            'description': 'Мощный ноутбук с процессором M2 Pro для профессионалов',
            'price': 259990,
            'image': 'macbook_pro.jpg',
            'stock': 10
        },
        {
            'name': 'Dell XPS 15',
            'description': 'Тонкий и легкий ноутбук с мощным железом',
            'price': 189990,
            'image': 'dell_xps.jpg',
            'stock': 12
        },
        {
            'name': 'ASUS ROG Zephyrus G14',
            'description': 'Компактный игровой ноутбук с высокой производительностью',
            'price': 159990,
            'image': 'rog_zephyrus.jpg',
            'stock': 15
        },
        {
            'name': 'Lenovo ThinkPad X1 Carbon',
            'description': 'Бизнес-ноутбук с высокой надежностью',
            'price': 199990,
            'image': 'thinkpad_x1.jpg',
            'stock': 8
        },
        {
            'name': 'HP Spectre x360',
            'description': 'Премиальный трансформер с OLED-дисплеем',
            'price': 154990,
            'image': 'hp_spectre.jpg',
            'stock': 10
        }
    ],
    'Аксессуары': [
        {
            'name': 'Беспроводное зарядное устройство',
            'description': 'Быстрая беспроводная зарядка для вашего смартфона',
            'price': 4990,
            'image': 'wireless_charger.jpg',
            'stock': 40
        },
        {
            'name': 'Магнитный внешний аккумулятор',
            'description': 'Портативный аккумулятор с магнитным креплением для iPhone',
            'price': 6990,
            'image': 'powerbank.jpg',
            'stock': 25
        },
        {
            'name': 'Защитное стекло',
            'description': 'Ультратонкое защитное стекло с олеофобным покрытием',
            'price': 1990,
            'image': 'screen_protector.jpg',
            'stock': 50
        },
        {
            'name': 'Карта памяти 256GB',
            'description': 'Быстрая и надежная карта памяти для ваших устройств',
            'price': 3990,
            'image': 'memory_card.jpg',
            'stock': 35
        },
        {
            'name': 'Чехол-кошелек из натуральной кожи',
            'description': 'Премиальный кожаный чехол с отделениями для карт',
            'price': 3490,
            'image': 'leather_case.jpg',
            'stock': 20
        }
    ],
    'Планшеты': [
        {
            'name': 'iPad Pro 12.9" M2',
            'description': 'Мощный планшет с процессором M2 и mini-LED дисплеем',
            'price': 139990,
            'image': 'ipad_pro.jpg',
            'stock': 10
        },
        {
            'name': 'Samsung Galaxy Tab S9 Ultra',
            'description': 'Премиальный Android-планшет с AMOLED экраном',
            'price': 119990,
            'image': 'galaxy_tab.jpg',
            'stock': 12
        },
        {
            'name': 'Xiaomi Pad 6',
            'description': 'Планшет с отличным соотношением цены и качества',
            'price': 39990,
            'image': 'xiaomi_pad.jpg',
            'stock': 18
        },
        {
            'name': 'Microsoft Surface Pro 9',
            'description': 'Гибридный планшет на Windows с клавиатурой',
            'price': 129990,
            'image': 'surface_pro.jpg',
            'stock': 8
        },
        {
            'name': 'iPad Air M1',
            'description': 'Легкий и производительный планшет с чипом M1',
            'price': 79990,
            'image': 'ipad_air.jpg',
            'stock': 15
        }
    ],
    'Наушники': [
        {
            'name': 'Sony WH-1000XM5',
            'description': 'Беспроводные наушники с лучшим шумоподавлением',
            'price': 39990,
            'image': 'sony_wh1000xm5.jpg',
            'stock': 15
        },
        {
            'name': 'Apple AirPods Pro 2',
            'description': 'TWS наушники с активным шумоподавлением',
            'price': 24990,
            'image': 'airpods_pro.jpg',
            'stock': 20
        },
        {
            'name': 'Bose QuietComfort Ultra',
            'description': 'Комфортные наушники с превосходным звуком',
            'price': 44990,
            'image': 'bose_qc.jpg',
            'stock': 10
        },
        {
            'name': 'Sennheiser Momentum 4',
            'description': 'Беспроводные наушники с долгой автономностью',
            'price': 34990,
            'image': 'sennheiser_momentum.jpg',
            'stock': 12
        },
        {
            'name': 'Samsung Galaxy Buds 3 Pro',
            'description': 'Компактные TWS наушники с хорошим звуком',
            'price': 16990,
            'image': 'galaxy_buds.jpg',
            'stock': 25
        }
    ]
}

def seed_database_railway():
    """Заполняет базу данных тестовыми данными для Railway"""
    with app.app_context():
        try:
            # Проверка существования категорий
            existing_categories = Category.query.count()
            existing_products = Product.query.count()

            if existing_categories > 0 and existing_products > 0:
                print("В базе данных уже есть категории и товары. Пропускаем заполнение.")
                return

            # Создание категорий
            categories = {}
            for cat_data in categories_data:
                # Проверка, существует ли уже категория с таким именем
                category = Category.query.filter_by(name=cat_data['name']).first()
                if not category:
                    # Создаем slug из имени категории
                    slug = slugify(cat_data['name'])
                    category = Category(
                        name=cat_data['name'],
                        slug=slug,
                        description=cat_data['description'],
                        image=cat_data['image']
                    )
                    db.session.add(category)
                    db.session.flush()  # Получаем ID без полного коммита
                categories[cat_data['name']] = category

            # Создание продуктов для каждой категории
            for cat_name, products in products_data.items():
                category = categories.get(cat_name)
                if not category:
                    print(f"Категория {cat_name} не создана. Пропускаем...")
                    continue

                for prod_data in products:
                    # Проверка, существует ли уже продукт с таким именем
                    product = Product.query.filter_by(name=prod_data['name']).first()
                    if not product:
                        # Создаем slug из имени продукта
                        slug = slugify(prod_data['name'])
                        
                        # Генерируем SKU (артикул) для товара
                        sku = f"{category.name[:3].upper()}-{random.randint(1000, 9999)}"
                        
                        product = Product(
                            name=prod_data['name'],
                            slug=slug,
                            sku=sku,
                            description=prod_data['description'],
                            price=prod_data['price'],
                            image=prod_data['image'],
                            stock=prod_data['stock'],
                            category_id=category.id
                        )
                        
                        # Добавляем случайную скидку некоторым товарам
                        if random.random() < 0.3:  # 30% шанс скидки
                            discount_percent = random.choice([5, 10, 15, 20, 25])
                            product.old_price = product.price
                            product.price = round(product.price * (1 - discount_percent / 100))
                            product.is_sale = True

                        # Добавляем флаг "новинка" некоторым товарам
                        if random.random() < 0.2:  # 20% шанс быть новинкой
                            product.is_new = True

                        # Добавляем флаг "featured" (избранный/рекомендуемый) некоторым товарам
                        if random.random() < 0.15:  # 15% шанс быть рекомендуемым
                            product.is_featured = True

                        db.session.add(product)

            # Сохраняем изменения в базе данных
            db.session.commit()
            print("База данных успешно заполнена тестовыми данными!")
            print(f"Добавлено {len(categories_data)} категорий и "
                  f"{sum(len(products) for products in products_data.values())} товаров.")

        except Exception as e:
            db.session.rollback()
            print(f"Ошибка при заполнении базы данных: {str(e)}")
            raise e

if __name__ == "__main__":
    seed_database_railway()
