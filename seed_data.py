#!/usr/bin/env python
"""
Скрипт для заполнения базы данных товарами и категориями
"""
import os
import random
from my_app import create_app, db
from my_app.models import Product, Category

# Создаем экземпляр приложения
app = create_app(os.getenv('APP_SETTINGS', 'development'))

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
        },
        {
            'name': 'OnePlus 11',
            'description': 'Мощный процессор и быстрая зарядка',
            'price': 64990,
            'image': 'oneplus_11.jpg',
            'stock': 22
        },
        {
            'name': 'Honor 90',
            'description': 'Стильный дизайн и хорошая автономность',
            'price': 44990,
            'image': 'honor_90.jpg',
            'stock': 28
        },
        {
            'name': 'Motorola Edge 40',
            'description': 'Тонкий корпус и защита от воды',
            'price': 39990,
            'image': 'motorola_edge.jpg',
            'stock': 15
        },
        {
            'name': 'OPPO Find X6 Pro',
            'description': 'Премиальная камера Hasselblad',
            'price': 84990,
            'image': 'oppo_find.jpg',
            'stock': 10
        },
        {
            'name': 'Vivo X90 Pro',
            'description': 'Процессор Dimensity 9200 и ZEISS оптика',
            'price': 74990,
            'image': 'vivo_x90.jpg',
            'stock': 14
        },
        {
            'name': 'Realme GT5',
            'description': 'Игровой смартфон с мощным охлаждением',
            'price': 49990,
            'image': 'realme_gt5.jpg',
            'stock': 20
        },
        {
            'name': 'ASUS ROG Phone 7',
            'description': 'Лучший игровой смартфон на рынке',
            'price': 89990,
            'image': 'rog_phone.jpg',
            'stock': 8
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
        },
        {
            'name': 'Acer Predator Helios 300',
            'description': 'Доступный игровой ноутбук с RTX 3070',
            'price': 129990,
            'image': 'predator_helios.jpg',
            'stock': 14
        },
        {
            'name': 'MSI Creator Z16',
            'description': 'Ноутбук для креативных профессионалов',
            'price': 209990,
            'image': 'msi_creator.jpg',
            'stock': 7
        },
        {
            'name': 'Razer Blade 15',
            'description': 'Премиальный игровой ноутбук в алюминиевом корпусе',
            'price': 239990,
            'image': 'razer_blade.jpg',
            'stock': 5
        },
        {
            'name': 'Microsoft Surface Laptop 5',
            'description': 'Элегантный ноутбук с сенсорным экраном',
            'price': 139990,
            'image': 'surface_laptop.jpg',
            'stock': 9
        },
        {
            'name': 'LG Gram 17',
            'description': 'Сверхлегкий ноутбук с большим экраном',
            'price': 149990,
            'image': 'lg_gram.jpg',
            'stock': 11
        }
    ],
    'Аксессуары': [
        {
            'name': 'Беспроводное зарядное устройство Samsung',
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
            'name': 'Защитное стекло Gorilla Glass',
            'description': 'Ультратонкое защитное стекло с олеофобным покрытием',
            'price': 1990,
            'image': 'screen_protector.jpg',
            'stock': 50
        },
        {
            'name': 'Карта памяти Samsung EVO Plus 256GB',
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
        },
        {
            'name': 'USB-C хаб 7-в-1',
            'description': 'Расширьте возможности вашего ноутбука с помощью многофункционального хаба',
            'price': 5990,
            'image': 'usb_hub.jpg',
            'stock': 30
        },
        {
            'name': 'Подставка для ноутбука',
            'description': 'Алюминиевая подставка с регулировкой угла наклона',
            'price': 4490,
            'image': 'laptop_stand.jpg',
            'stock': 18
        },
        {
            'name': 'Bluetooth селфи-палка',
            'description': 'Выдвижная селфи-палка с пультом управления',
            'price': 1990,
            'image': 'selfie_stick.jpg',
            'stock': 45
        },
        {
            'name': 'Автомобильный держатель с беспроводной зарядкой',
            'description': 'Удобный держатель для смартфона с функцией беспроводной зарядки',
            'price': 3990,
            'image': 'car_holder.jpg',
            'stock': 22
        },
        {
            'name': 'Внешний SSD Samsung T7 1TB',
            'description': 'Сверхбыстрый портативный SSD с интерфейсом USB-C',
            'price': 14990,
            'image': 'external_ssd.jpg',
            'stock': 15
        },
        {
            'name': 'Переходник USB-C в 3.5mm',
            'description': 'Аудиоадаптер для подключения наушников к современным смартфонам',
            'price': 990,
            'image': 'usb_adapter.jpg',
            'stock': 60
        },
        {
            'name': 'Рюкзак для ноутбука',
            'description': 'Водонепроницаемый рюкзак с отделением для ноутбука до 15.6"',
            'price': 5990,
            'image': 'laptop_backpack.jpg',
            'stock': 25
        },
        {
            'name': 'Клавиатура Bluetooth',
            'description': 'Компактная беспроводная клавиатура для планшетов и смартфонов',
            'price': 3990,
            'image': 'bluetooth_keyboard.jpg',
            'stock': 30
        },
        {
            'name': 'Стилус для сенсорных экранов',
            'description': 'Высокоточный стилус с поддержкой 4096 уровней нажатия',
            'price': 4990,
            'image': 'stylus.jpg',
            'stock': 20
        },
        {
            'name': 'Защитная пленка для ноутбука',
            'description': 'Защитная пленка для клавиатуры и тачпада',
            'price': 990,
            'image': 'keyboard_protector.jpg',
            'stock': 40
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
        },
        {
            'name': 'Lenovo Tab P12 Pro',
            'description': 'Планшет с OLED-экраном и стилусом в комплекте',
            'price': 69990,
            'image': 'lenovo_tab.jpg',
            'stock': 10
        },
        {
            'name': 'Huawei MatePad Pro',
            'description': 'Планшет с поддержкой умной клавиатуры и стилуса',
            'price': 59990,
            'image': 'huawei_matepad.jpg',
            'stock': 12
        },
        {
            'name': 'Amazon Fire HD 10',
            'description': 'Доступный планшет для развлечений и чтения',
            'price': 19990,
            'image': 'fire_hd.jpg',
            'stock': 20
        },
        {
            'name': 'ASUS Zenpad 3S',
            'description': 'Стильный планшет с качественным звуком',
            'price': 49990,
            'image': 'zenpad.jpg',
            'stock': 14
        },
        {
            'name': 'iPad Mini 6',
            'description': 'Компактный планшет с мощным железом',
            'price': 59990,
            'image': 'ipad_mini.jpg',
            'stock': 16
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
        },
        {
            'name': 'Jabra Elite 10',
            'description': 'Спортивные наушники с защитой от воды',
            'price': 19990,
            'image': 'jabra_elite.jpg',
            'stock': 18
        },
        {
            'name': 'JBL Tour One M2',
            'description': 'Наушники с глубоким басом и активным шумоподавлением',
            'price': 28990,
            'image': 'jbl_tour.jpg',
            'stock': 15
        },
        {
            'name': 'Beyerdynamic DT 990 Pro',
            'description': 'Профессиональные открытые студийные наушники',
            'price': 14990,
            'image': 'beyerdynamic.jpg',
            'stock': 8
        },
        {
            'name': 'Audio-Technica ATH-M50x',
            'description': 'Мониторные наушники для профессионалов',
            'price': 12990,
            'image': 'audio_technica.jpg',
            'stock': 10
        },
        {
            'name': 'Sony WF-1000XM5',
            'description': 'Компактные TWS наушники с Hi-Res Audio',
            'price': 27990,
            'image': 'sony_wf1000xm5.jpg',
            'stock': 14
        },
        {
            'name': 'Apple AirPods Max',
            'description': 'Премиальные полноразмерные наушники Apple',
            'price': 59990,
            'image': 'airpods_max.jpg',
            'stock': 6
        },
        {
            'name': 'Beats Studio Pro',
            'description': 'Стильные наушники с отличным звучанием',
            'price': 32990,
            'image': 'beats_studio.jpg',
            'stock': 12
        }
    ]
}

def seed_database():
    """Заполняет базу данных тестовыми данными"""
    with app.app_context():
        try:
            # Проверка существования категорий
            existing_categories = Category.query.count()
            if existing_categories > 0:
                print(f"В базе данных уже есть {existing_categories} категорий.")
                choice = input("Хотите очистить таблицы перед заполнением? (y/n): ")

                if choice.lower() == 'y':
                    # Удаление всех продуктов (из-за зависимостей)
                    Product.query.delete()
                    # Удаление всех категорий
                    Category.query.delete()
                    db.session.commit()
                    print("Таблицы очищены.")
                else:
                    print("Добавляем данные без очистки таблиц...")

            # Создание категорий
            categories = {}
            for cat_data in categories_data:
                # Проверка, существует ли уже категория с таким именем
                category = Category.query.filter_by(name=cat_data['name']).first()
                if not category:
                    # Создаем slug из имени категории (транслитерация и замена пробелов на дефисы)
                    slug = cat_data['name'].lower().replace(' ', '-')
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
                        # Создаем slug из имени продукта (транслитерация и замена пробелов на дефисы)
                        slug = prod_data['name'].lower().replace(' ', '-')
                        # Генерируем SKU (артикул) для товара
                        sku = f"{cat_name[:3].upper()}-{random.randint(1000, 9999)}"

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
                            product.discount_price = round(product.price * (1 - discount_percent / 100))

                        # Добавляем флаг "новинка" некоторым товарам
                        if random.random() < 0.2:  # 20% шанс быть новинкой
                            product.is_new = True

                        # Добавляем флаг "хит продаж" некоторым товарам
                        if random.random() < 0.15:  # 15% шанс быть хитом продаж
                            product.is_bestseller = True

                        # Добавляем бренд товару
                        from my_app.models.brand import Brand
                        
                        # Словарь соответствия названий товаров и брендов
                        brand_mapping = {
                            'Galaxy': 'Samsung',
                            'iPhone': 'Apple',
                            'iPad': 'Apple',
                            'MacBook': 'Apple',
                            'Xiaomi': 'Xiaomi',
                            'Huawei': 'Huawei',
                            'Sony': 'Sony',
                            'Nothing': 'Nothing',
                            'Google': 'Google',
                            'OnePlus': 'OnePlus',
                            'Honor': 'Huawei',
                            'Motorola': 'Motorola',
                            'OPPO': 'Oppo',
                            'Vivo': 'Vivo',
                            'Realme': 'Realme',
                            'ASUS': 'Asus',
                            'Dell': 'Dell',
                            'Lenovo': 'Lenovo',
                            'HP': 'HP',
                            'MSI': 'MSI',
                            'Razer': 'Razer',
                            'Microsoft': 'Microsoft',
                            'LG': 'LG',
                            'Bose': 'Bose',
                            'JBL': 'JBL',
                            'Sennheiser': 'Sennheiser',
                            'Jabra': 'Jabra',
                            'Beyerdynamic': 'Beyerdynamic',
                            'Audio-Technica': 'Audio-Technica',
                            'Beats': 'Beats',
                            'Acer': 'Acer'
                        }
                        
                        # Определяем бренд по названию товара
                        brand_name = None
                        for key, value in brand_mapping.items():
                            if key in product.name:
                                brand_name = value
                                break
                        
                        # Если бренд определен, ищем его в базе данных и привязываем к товару
                        if brand_name:
                            brand = db.session.query(Brand).filter_by(name=brand_name).first()
                            if brand:
                                product.brand_id = brand.id
                        
                        db.session.add(product)

            # Сохраняем изменения в базе данных
            db.session.commit()
            print("База данных успешно заполнена тестовыми данными!")
            print(f"Добавлено {len(categories_data)} категорий и "
                  f"{sum(len(products) for products in products_data.values())} товаров.")

        except Exception as e:
            db.session.rollback()
            print(f"Ошибка при заполнении базы данных: {str(e)}")

if __name__ == "__main__":
    seed_database()