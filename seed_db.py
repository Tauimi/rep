
"""
Скрипт для заполнения базы данных товарами и категориями
"""
import os
import random
from datetime import datetime
from slugify import slugify
from my_app import create_app, db
from my_app.models.product import Product, Specification
from my_app.models.category import Category

app = create_app('development')

# Функция для создания категорий товаров
def create_categories():
    categories = [
        {
            'name': 'Смартфоны',
            'description': 'Современные мобильные устройства с сенсорным экраном и различными функциями',
            'image': 'smartphones.jpg'
        },
        {
            'name': 'Ноутбуки',
            'description': 'Портативные компьютеры для работы, учебы и развлечений',
            'image': 'laptops.jpg'
        },
        {
            'name': 'Планшеты',
            'description': 'Мобильные устройства с большим сенсорным экраном',
            'image': 'tablets.jpg'
        },
        {
            'name': 'Аксессуары',
            'description': 'Дополнительные устройства и принадлежности для электроники',
            'image': 'accessories.jpg'
        },
        {
            'name': 'Наушники',
            'description': 'Устройства для прослушивания аудио',
            'image': 'headphones.jpg'
        }
    ]
    
    created_categories = []
    
    for category_data in categories:
        # Проверка на существование категории
        existing = Category.query.filter_by(name=category_data['name']).first()
        if existing:
            print(f"Категория '{category_data['name']}' уже существует")
            created_categories.append(existing)
            continue
            
        # Создание новой категории
        slug = slugify(category_data['name'])
        category = Category(
            name=category_data['name'],
            slug=slug,
            description=category_data['description'],
            image=category_data['image']
        )
        db.session.add(category)
        print(f"Создана категория: {category_data['name']}")
        created_categories.append(category)
    
    db.session.commit()
    return created_categories

# Функция для создания продуктов
def create_products(categories):
    # Данные товаров по категориям
    products_data = {
        'Смартфоны': [
            {
                'name': 'Samsung Galaxy S21',
                'description': 'Флагманский смартфон с 6,2-дюймовым дисплеем, процессором Exynos 2100 и тройной камерой',
                'price': 69999.00,
                'old_price': 79999.00,
                'stock': 15,
                'image': 'samsung_s21.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,2" Dynamic AMOLED 2X'},
                    {'name': 'Процессор', 'value': 'Exynos 2100'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Основная камера', 'value': '12 МП + 12 МП + 64 МП'},
                    {'name': 'Аккумулятор', 'value': '4000 мАч'}
                ]
            },
            {
                'name': 'iPhone 13 Pro',
                'description': 'Смартфон с процессором A15 Bionic, OLED-дисплеем и системой камер Pro',
                'price': 89999.00,
                'old_price': 99999.00,
                'stock': 10,
                'image': 'iphone_13_pro.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,1" Super Retina XDR'},
                    {'name': 'Процессор', 'value': 'Apple A15 Bionic'},
                    {'name': 'Оперативная память', 'value': '6 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Основная камера', 'value': '12 МП + 12 МП + 12 МП'},
                    {'name': 'Аккумулятор', 'value': '3095 мАч'}
                ]
            },
            {
                'name': 'Xiaomi Mi 11',
                'description': 'Мощный смартфон с процессором Snapdragon 888, 108-мегапиксельной камерой и AMOLED-дисплеем',
                'price': 59999.00,
                'old_price': 64999.00,
                'stock': 20,
                'image': 'xiaomi_mi11.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,81" AMOLED'},
                    {'name': 'Процессор', 'value': 'Snapdragon 888'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Основная камера', 'value': '108 МП + 13 МП + 5 МП'},
                    {'name': 'Аккумулятор', 'value': '4600 мАч'}
                ]
            },
            {
                'name': 'Google Pixel 6',
                'description': 'Смартфон с чистым Android, отличной камерой и процессором Google Tensor',
                'price': 54999.00,
                'old_price': 64999.00,
                'stock': 12,
                'image': 'google_pixel6.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,4" AMOLED'},
                    {'name': 'Процессор', 'value': 'Google Tensor'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Основная камера', 'value': '50 МП + 12 МП'},
                    {'name': 'Аккумулятор', 'value': '4614 мАч'}
                ]
            },
            {
                'name': 'OnePlus 9 Pro',
                'description': 'Флагманский смартфон с быстрой зарядкой и камерой Hasselblad',
                'price': 64999.00,
                'old_price': 69999.00,
                'stock': 8,
                'image': 'oneplus_9pro.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,7" Fluid AMOLED'},
                    {'name': 'Процессор', 'value': 'Snapdragon 888'},
                    {'name': 'Оперативная память', 'value': '12 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Основная камера', 'value': '48 МП + 50 МП + 8 МП + 2 МП'},
                    {'name': 'Аккумулятор', 'value': '4500 мАч'}
                ]
            },
            {
                'name': 'Huawei P40 Pro',
                'description': 'Смартфон с камерой Leica и процессором Kirin 990',
                'price': 54999.00,
                'old_price': 64999.00,
                'stock': 5,
                'image': 'huawei_p40pro.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,58" OLED'},
                    {'name': 'Процессор', 'value': 'Kirin 990 5G'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Основная камера', 'value': '50 МП + 40 МП + 12 МП + ToF'},
                    {'name': 'Аккумулятор', 'value': '4200 мАч'}
                ]
            },
            {
                'name': 'Realme GT',
                'description': 'Производительный смартфон по доступной цене',
                'price': 39999.00,
                'old_price': 44999.00,
                'stock': 25,
                'image': 'realme_gt.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,43" Super AMOLED'},
                    {'name': 'Процессор', 'value': 'Snapdragon 888'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Основная камера', 'value': '64 МП + 8 МП + 2 МП'},
                    {'name': 'Аккумулятор', 'value': '4500 мАч'}
                ]
            },
            {
                'name': 'Sony Xperia 1 III',
                'description': 'Премиальный смартфон с 4K HDR OLED-дисплеем и продвинутой камерой',
                'price': 84999.00,
                'old_price': 94999.00,
                'stock': 3,
                'image': 'sony_xperia1.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,5" 4K HDR OLED'},
                    {'name': 'Процессор', 'value': 'Snapdragon 888'},
                    {'name': 'Оперативная память', 'value': '12 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Основная камера', 'value': '12 МП + 12 МП + 12 МП'},
                    {'name': 'Аккумулятор', 'value': '4500 мАч'}
                ]
            },
            {
                'name': 'ASUS ROG Phone 5',
                'description': 'Игровой смартфон с мощными характеристиками и системой охлаждения',
                'price': 74999.00,
                'old_price': 84999.00,
                'stock': 6,
                'image': 'asus_rog5.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,78" AMOLED'},
                    {'name': 'Процессор', 'value': 'Snapdragon 888'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Основная камера', 'value': '64 МП + 13 МП + 5 МП'},
                    {'name': 'Аккумулятор', 'value': '6000 мАч'}
                ]
            },
            {
                'name': 'Motorola Edge 20 Pro',
                'description': 'Смартфон с 144 Гц экраном и камерой 108 МП',
                'price': 45999.00,
                'old_price': 49999.00,
                'stock': 14,
                'image': 'motorola_edge20.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '6,7" OLED 144 Гц'},
                    {'name': 'Процессор', 'value': 'Snapdragon 870'},
                    {'name': 'Оперативная память', 'value': '12 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Основная камера', 'value': '108 МП + 16 МП + 8 МП'},
                    {'name': 'Аккумулятор', 'value': '4500 мАч'}
                ]
            }
        ],
        'Ноутбуки': [
            {
                'name': 'MacBook Pro 14"',
                'description': 'Профессиональный ноутбук Apple с процессором M1 Pro, Mini-LED экраном и длительным временем автономной работы',
                'price': 149999.00,
                'old_price': 169999.00,
                'stock': 5,
                'image': 'macbook_pro14.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '14,2" Liquid Retina XDR'},
                    {'name': 'Процессор', 'value': 'Apple M1 Pro'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 512 ГБ'},
                    {'name': 'Графика', 'value': '16-ядерный GPU'},
                    {'name': 'Время работы', 'value': 'До 17 часов'}
                ]
            },
            {
                'name': 'Dell XPS 15',
                'description': 'Премиальный ноутбук с OLED-дисплеем, процессором Intel Core i7 и дискретной графикой',
                'price': 129999.00,
                'old_price': 144999.00,
                'stock': 8,
                'image': 'dell_xps15.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '15,6" OLED 3.5K'},
                    {'name': 'Процессор', 'value': 'Intel Core i7-11800H'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 1 ТБ'},
                    {'name': 'Графика', 'value': 'NVIDIA GeForce RTX 3050 Ti'},
                    {'name': 'Время работы', 'value': 'До 12 часов'}
                ]
            },
            {
                'name': 'Lenovo ThinkPad X1 Carbon',
                'description': 'Ультрабук бизнес-класса с высоким уровнем безопасности и надежности',
                'price': 119999.00,
                'old_price': 134999.00,
                'stock': 12,
                'image': 'thinkpad_x1.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '14" IPS 2560x1440'},
                    {'name': 'Процессор', 'value': 'Intel Core i7-1165G7'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 512 ГБ'},
                    {'name': 'Графика', 'value': 'Intel Iris Xe'},
                    {'name': 'Время работы', 'value': 'До 15 часов'}
                ]
            },
            {
                'name': 'ASUS ROG Zephyrus G14',
                'description': 'Игровой ноутбук с мощной видеокартой и компактным дизайном',
                'price': 109999.00,
                'old_price': 119999.00,
                'stock': 7,
                'image': 'asus_g14.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '14" IPS 144 Гц 2560x1440'},
                    {'name': 'Процессор', 'value': 'AMD Ryzen 9 5900HS'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 1 ТБ'},
                    {'name': 'Графика', 'value': 'NVIDIA GeForce RTX 3060'},
                    {'name': 'Время работы', 'value': 'До 10 часов'}
                ]
            },
            {
                'name': 'HP Spectre x360',
                'description': 'Ультрабук-трансформер с сенсорным экраном и стильным дизайном',
                'price': 99999.00,
                'old_price': 109999.00,
                'stock': 15,
                'image': 'hp_spectre.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '13,3" OLED 4K'},
                    {'name': 'Процессор', 'value': 'Intel Core i7-1165G7'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 1 ТБ'},
                    {'name': 'Графика', 'value': 'Intel Iris Xe'},
                    {'name': 'Время работы', 'value': 'До 13 часов'}
                ]
            },
            {
                'name': 'Microsoft Surface Laptop 4',
                'description': 'Тонкий и легкий ноутбук с сенсорным дисплеем и отличной клавиатурой',
                'price': 94999.00,
                'old_price': 104999.00,
                'stock': 9,
                'image': 'surface_laptop4.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '13,5" PixelSense'},
                    {'name': 'Процессор', 'value': 'AMD Ryzen 5 4680U'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 256 ГБ'},
                    {'name': 'Графика', 'value': 'AMD Radeon Graphics'},
                    {'name': 'Время работы', 'value': 'До 19 часов'}
                ]
            },
            {
                'name': 'Acer Predator Helios 300',
                'description': 'Мощный игровой ноутбук с высокой производительностью и эффективной системой охлаждения',
                'price': 89999.00,
                'old_price': 99999.00,
                'stock': 11,
                'image': 'acer_predator.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '15,6" IPS 144 Гц'},
                    {'name': 'Процессор', 'value': 'Intel Core i7-11800H'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 512 ГБ'},
                    {'name': 'Графика', 'value': 'NVIDIA GeForce RTX 3060'},
                    {'name': 'Время работы', 'value': 'До 6 часов'}
                ]
            },
            {
                'name': 'Razer Blade 15',
                'description': 'Премиальный игровой ноутбук в алюминиевом корпусе с RGB-подсветкой',
                'price': 149999.00,
                'old_price': 164999.00,
                'stock': 4,
                'image': 'razer_blade15.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '15,6" IPS 360 Гц'},
                    {'name': 'Процессор', 'value': 'Intel Core i7-11800H'},
                    {'name': 'Оперативная память', 'value': '32 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 1 ТБ'},
                    {'name': 'Графика', 'value': 'NVIDIA GeForce RTX 3080'},
                    {'name': 'Время работы', 'value': 'До 7 часов'}
                ]
            },
            {
                'name': 'Huawei MateBook X Pro',
                'description': 'Ультратонкий ноутбук с безрамочным дисплеем и высоким разрешением',
                'price': 109999.00,
                'old_price': 119999.00,
                'stock': 6,
                'image': 'huawei_matebook.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '13,9" LTPS 3000x2000'},
                    {'name': 'Процессор', 'value': 'Intel Core i7-1165G7'},
                    {'name': 'Оперативная память', 'value': '16 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 1 ТБ'},
                    {'name': 'Графика', 'value': 'Intel Iris Xe'},
                    {'name': 'Время работы', 'value': 'До 10 часов'}
                ]
            },
            {
                'name': 'MSI GS66 Stealth',
                'description': 'Мощный тонкий игровой ноутбук с высокой частотой обновления экрана',
                'price': 129999.00,
                'old_price': 144999.00,
                'stock': 3,
                'image': 'msi_gs66.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '15,6" IPS 300 Гц'},
                    {'name': 'Процессор', 'value': 'Intel Core i9-11900H'},
                    {'name': 'Оперативная память', 'value': '32 ГБ'},
                    {'name': 'Накопитель', 'value': 'SSD 2 ТБ'},
                    {'name': 'Графика', 'value': 'NVIDIA GeForce RTX 3080'},
                    {'name': 'Время работы', 'value': 'До 8 часов'}
                ]
            }
        ],
        'Планшеты': [
            {
                'name': 'iPad Pro 12.9 (2021)',
                'description': 'Планшет Apple с процессором M1, дисплеем Mini-LED и поддержкой 5G',
                'price': 99999.00,
                'old_price': 114999.00,
                'stock': 8,
                'image': 'ipad_pro.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '12,9" Liquid Retina XDR'},
                    {'name': 'Процессор', 'value': 'Apple M1'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Камера', 'value': '12 МП + 10 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 10 часов'}
                ]
            },
            {
                'name': 'Samsung Galaxy Tab S8 Ultra',
                'description': 'Флагманский планшет Samsung с большим AMOLED-дисплеем и поддержкой S Pen',
                'price': 84999.00,
                'old_price': 94999.00,
                'stock': 6,
                'image': 'galaxy_tabs8.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '14,6" Super AMOLED'},
                    {'name': 'Процессор', 'value': 'Snapdragon 8 Gen 1'},
                    {'name': 'Оперативная память', 'value': '12 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Камера', 'value': '13 МП + 6 МП + 12 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 14 часов'}
                ]
            },
            {
                'name': 'Microsoft Surface Pro 8',
                'description': 'Планшет-трансформер с Windows 11 и Intel Core процессором',
                'price': 89999.00,
                'old_price': 99999.00,
                'stock': 4,
                'image': 'surface_pro8.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '13" PixelSense Flow 120 Гц'},
                    {'name': 'Процессор', 'value': 'Intel Core i5-1135G7'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': 'SSD 256 ГБ'},
                    {'name': 'Камера', 'value': '10 МП задняя + Windows Hello фронтальная'},
                    {'name': 'Время работы', 'value': 'До 16 часов'}
                ]
            },
            {
                'name': 'Lenovo Tab P12 Pro',
                'description': 'Премиальный Android-планшет с AMOLED экраном и функцией Project Unity',
                'price': 59999.00,
                'old_price': 69999.00,
                'stock': 10,
                'image': 'lenovo_p12pro.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '12,6" AMOLED 120 Гц'},
                    {'name': 'Процессор', 'value': 'Snapdragon 870'},
                    {'name': 'Оперативная память', 'value': '6 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Камера', 'value': '13 МП + 5 МП + 8 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 15 часов'}
                ]
            },
            {
                'name': 'Huawei MatePad Pro',
                'description': 'Производительный планшет с HarmonyOS и функцией беспроводной зарядки',
                'price': 49999.00,
                'old_price': 59999.00,
                'stock': 12,
                'image': 'huawei_matepad.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '12,6" OLED'},
                    {'name': 'Процессор', 'value': 'Kirin 9000E'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '256 ГБ'},
                    {'name': 'Камера', 'value': '13 МП + 8 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 14 часов'}
                ]
            },
            {
                'name': 'iPad Air (2022)',
                'description': 'Мощный планшет с процессором M1 и улучшенной фронтальной камерой',
                'price': 54999.00,
                'old_price': 64999.00,
                'stock': 15,
                'image': 'ipad_air.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '10,9" Liquid Retina'},
                    {'name': 'Процессор', 'value': 'Apple M1'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '64 ГБ'},
                    {'name': 'Камера', 'value': '12 МП + 12 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 10 часов'}
                ]
            },
            {
                'name': 'Xiaomi Pad 5',
                'description': 'Доступный планшет с отличным экраном и квадро-динамиками',
                'price': 29999.00,
                'old_price': 34999.00,
                'stock': 20,
                'image': 'xiaomi_pad5.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '11" IPS 120 Гц'},
                    {'name': 'Процессор', 'value': 'Snapdragon 860'},
                    {'name': 'Оперативная память', 'value': '6 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Камера', 'value': '13 МП + 8 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 16 часов'}
                ]
            },
            {
                'name': 'Amazon Fire HD 10 Plus',
                'description': 'Доступный планшет с хорошей автономностью и интеграцией с сервисами Amazon',
                'price': 14999.00,
                'old_price': 17999.00,
                'stock': 25,
                'image': 'amazon_fire.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '10,1" IPS 1080p'},
                    {'name': 'Процессор', 'value': 'Octa-core 2.0 GHz'},
                    {'name': 'Оперативная память', 'value': '4 ГБ'},
                    {'name': 'Встроенная память', 'value': '64 ГБ'},
                    {'name': 'Камера', 'value': '5 МП + 2 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 12 часов'}
                ]
            },
            {
                'name': 'Samsung Galaxy Tab A8',
                'description': 'Бюджетный планшет с хорошим дисплеем и четырьмя динамиками',
                'price': 19999.00,
                'old_price': 22999.00,
                'stock': 18,
                'image': 'galaxy_taba8.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '10,5" TFT 1920x1200'},
                    {'name': 'Процессор', 'value': 'Unisoc Tiger T618'},
                    {'name': 'Оперативная память', 'value': '4 ГБ'},
                    {'name': 'Встроенная память', 'value': '64 ГБ'},
                    {'name': 'Камера', 'value': '8 МП + 5 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 10 часов'}
                ]
            },
            {
                'name': 'Lenovo Yoga Tab 13',
                'description': 'Планшет с необычным дизайном, встроенной подставкой и HDMI-портом',
                'price': 44999.00,
                'old_price': 49999.00,
                'stock': 7,
                'image': 'lenovo_yoga13.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '13" LTPS 2K'},
                    {'name': 'Процессор', 'value': 'Snapdragon 870'},
                    {'name': 'Оперативная память', 'value': '8 ГБ'},
                    {'name': 'Встроенная память', 'value': '128 ГБ'},
                    {'name': 'Камера', 'value': '8 МП фронтальная'},
                    {'name': 'Время работы', 'value': 'До 12 часов'}
                ]
            }
        ],
        'Аксессуары': [
            {
                'name': 'Apple AirTag',
                'description': 'Bluetooth-трекер для поиска вещей с точной локацией и долгим сроком службы батареи',
                'price': 2999.00,
                'old_price': 3599.00,
                'stock': 50,
                'image': 'airtag.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Bluetooth-трекер'},
                    {'name': 'Связь', 'value': 'Bluetooth LE, NFC, UWB'},
                    {'name': 'Батарея', 'value': 'CR2032, до 1 года'},
                    {'name': 'Защита', 'value': 'IP67 (водонепроницаемость)'},
                    {'name': 'Особенности', 'value': 'Интеграция с Find My'}
                ]
            },
            {
                'name': 'Xiaomi Mi Smart Band 6',
                'description': 'Фитнес-браслет с AMOLED-дисплеем, пульсоксиметром и 30 режимами тренировок',
                'price': 3499.00,
                'old_price': 3999.00,
                'stock': 30,
                'image': 'mi_band6.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '1,56" AMOLED'},
                    {'name': 'Связь', 'value': 'Bluetooth 5.0'},
                    {'name': 'Батарея', 'value': 'До 14 дней'},
                    {'name': 'Защита', 'value': '5 ATM (водонепроницаемость)'},
                    {'name': 'Датчики', 'value': 'Пульсометр, акселерометр, гироскоп, SpO2'}
                ]
            },
            {
                'name': 'Samsung Galaxy Watch 4',
                'description': 'Умные часы с возможностью измерения состава тела и ЭКГ',
                'price': 19999.00,
                'old_price': 24999.00,
                'stock': 15,
                'image': 'galaxy_watch4.jpg',
                'specs': [
                    {'name': 'Экран', 'value': '1,4" Super AMOLED'},
                    {'name': 'Процессор', 'value': 'Exynos W920'},
                    {'name': 'Память', 'value': '1,5 ГБ ОЗУ + 16 ГБ встроенной'},
                    {'name': 'Батарея', 'value': 'До 40 часов'},
                    {'name': 'Датчики', 'value': 'Биоэлектрический, ЭКГ, пульсометр, SpO2, компас, барометр'},
                    {'name': 'Защита', 'value': 'IP68, 5 ATM'}
                ]
            },
            {
                'name': 'Anker PowerCore 20000',
                'description': 'Портативный аккумулятор с емкостью 20000 мАч и поддержкой быстрой зарядки',
                'price': 2999.00,
                'old_price': 3599.00,
                'stock': 40,
                'image': 'anker_powercore.jpg',
                'specs': [
                    {'name': 'Емкость', 'value': '20000 мАч'},
                    {'name': 'Выходы', 'value': '2x USB-A'},
                    {'name': 'Вход', 'value': 'Micro USB, USB-C'},
                    {'name': 'Технологии', 'value': 'PowerIQ, VoltageBoost'},
                    {'name': 'Размеры', 'value': '166 x 62 x 22 мм'},
                    {'name': 'Вес', 'value': '356 г'}
                ]
            },
            {
                'name': 'Logitech MX Master 3',
                'description': 'Премиальная беспроводная мышь с электромагнитным колесом прокрутки и расширенными функциями',
                'price': 7999.00,
                'old_price': 8999.00,
                'stock': 25,
                'image': 'mx_master3.jpg',
                'specs': [
                    {'name': 'Сенсор', 'value': 'Darkfield, 4000 DPI'},
                    {'name': 'Подключение', 'value': 'Bluetooth, USB-приемник'},
                    {'name': 'Батарея', 'value': 'До 70 дней'},
                    {'name': 'Кнопки', 'value': '7 программируемых'},
                    {'name': 'Особенности', 'value': 'Магнитное колесо прокрутки MagSpeed'},
                    {'name': 'Совместимость', 'value': 'Windows, macOS, Linux'}
                ]
            },
            {
                'name': 'Apple Pencil (2-го поколения)',
                'description': 'Стилус для iPad с беспроводной зарядкой и функцией двойного касания',
                'price': 9999.00,
                'old_price': 11999.00,
                'stock': 20,
                'image': 'apple_pencil2.jpg',
                'specs': [
                    {'name': 'Совместимость', 'value': 'iPad Pro, iPad Air (4-5 gen)'},
                    {'name': 'Зарядка', 'value': 'Магнитная беспроводная'},
                    {'name': 'Функции', 'value': 'Двойное касание, распознавание нажатия, наклона'},
                    {'name': 'Соединение', 'value': 'Bluetooth'},
                    {'name': 'Время работы', 'value': 'До 12 часов'}
                ]
            },
            {
                'name': 'JBL Flip 5',
                'description': 'Портативная Bluetooth-колонка с мощным звуком и защитой от воды',
                'price': 6999.00,
                'old_price': 8499.00,
                'stock': 35,
                'image': 'jbl_flip5.jpg',
                'specs': [
                    {'name': 'Мощность', 'value': '20 Вт'},
                    {'name': 'Батарея', 'value': 'До 12 часов'},
                    {'name': 'Защита', 'value': 'IPX7 (водонепроницаемость)'},
                    {'name': 'Связь', 'value': 'Bluetooth 4.2'},
                    {'name': 'Функции', 'value': 'PartyBoost для соединения колонок'},
                    {'name': 'Размеры', 'value': '181 x 69 x 74 мм'}
                ]
            },
            {
                'name': 'Belkin 3-in-1 Wireless Charger',
                'description': 'Беспроводная зарядная станция для iPhone, Apple Watch и AirPods',
                'price': 8999.00,
                'old_price': 9999.00,
                'stock': 15,
                'image': 'belkin_charger.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Беспроводная зарядная станция'},
                    {'name': 'Поддержка устройств', 'value': 'iPhone, Apple Watch, AirPods'},
                    {'name': 'Мощность зарядки', 'value': 'iPhone - 7.5 Вт, Apple Watch - 5 Вт, AirPods - 5 Вт'},
                    {'name': 'Вход', 'value': 'USB-C'},
                    {'name': 'Комплектация', 'value': 'Зарядная станция, адаптер питания'}
                ]
            },
            {
                'name': 'SanDisk Extreme Pro 128GB',
                'description': 'Высокоскоростная карта памяти SDXC для профессиональной фото и видеосъемки',
                'price': 3999.00,
                'old_price': 4499.00,
                'stock': 45,
                'image': 'sandisk_extreme.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'SDXC UHS-I'},
                    {'name': 'Емкость', 'value': '128 ГБ'},
                    {'name': 'Скорость чтения', 'value': 'До 170 МБ/с'},
                    {'name': 'Скорость записи', 'value': 'До 90 МБ/с'},
                    {'name': 'Класс скорости', 'value': 'V30, U3, Class 10'},
                    {'name': 'Защита', 'value': 'Ударопрочная, защита от рентгеновского излучения, влагостойкая'}
                ]
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Беспроводные наушники с активным шумоподавлением и высоким качеством звука',
                'price': 27999.00,
                'old_price': 31999.00,
                'stock': 10,
                'image': 'sony_wh1000xm4.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Накладные беспроводные'},
                    {'name': 'Шумоподавление', 'value': 'Активное с процессором QN1'},
                    {'name': 'Аудио', 'value': 'LDAC, DSEE Extreme'},
                    {'name': 'Батарея', 'value': 'До 30 часов'},
                    {'name': 'Функции', 'value': 'Speak-to-Chat, сенсорное управление, мультиточка'},
                    {'name': 'Разъем', 'value': 'USB-C, 3.5 мм'}
                ]
            }
        ],
        'Наушники': [
            {
                'name': 'Apple AirPods Pro 2',
                'description': 'Беспроводные наушники с активным шумоподавлением, адаптивным звуком и зарядным футляром MagSafe',
                'price': 19999.00,
                'old_price': 24999.00,
                'stock': 25,
                'image': 'airpods_pro2.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'Активное (ANC)'},
                    {'name': 'Защита', 'value': 'IPX4 (влагозащита)'},
                    {'name': 'Время работы', 'value': 'До 6 часов (30 часов с футляром)'},
                    {'name': 'Особенности', 'value': 'Адаптивная прозрачность, персонализированный 3D-звук, динамическое отслеживание движений головы'},
                    {'name': 'Зарядка', 'value': 'Lightning, MagSafe, беспроводная'}
                ]
            },
            {
                'name': 'Sony WF-1000XM4',
                'description': 'Премиальные TWS-наушники с лучшим в классе шумоподавлением и поддержкой Hi-Res Audio',
                'price': 16999.00,
                'old_price': 19999.00,
                'stock': 15,
                'image': 'sony_wf1000xm4.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'Активное с процессором V1'},
                    {'name': 'Защита', 'value': 'IPX4 (влагозащита)'},
                    {'name': 'Время работы', 'value': 'До 8 часов (24 часа с футляром)'},
                    {'name': 'Особенности', 'value': 'LDAC, DSEE Extreme, Speak-to-Chat'},
                    {'name': 'Зарядка', 'value': 'USB-C, беспроводная (Qi)'}
                ]
            },
            {
                'name': 'Samsung Galaxy Buds Pro 2',
                'description': 'Беспроводные наушники с активным шумоподавлением, 3D-звуком и улучшенным качеством звонков',
                'price': 13999.00,
                'old_price': 16999.00,
                'stock': 20,
                'image': 'galaxy_budspro2.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'Интеллектуальное ANC'},
                    {'name': 'Защита', 'value': 'IPX7 (водонепроницаемость)'},
                    {'name': 'Время работы', 'value': 'До 5 часов с ANC (18 часов с футляром)'},
                    {'name': 'Особенности', 'value': '360 Audio, Voice Detect, SmartThings Find'},
                    {'name': 'Зарядка', 'value': 'USB-C, беспроводная'}
                ]
            },
            {
                'name': 'Bose QuietComfort 45',
                'description': 'Накладные наушники с фирменным шумоподавлением Bose и комфортной посадкой',
                'price': 22999.00,
                'old_price': 26999.00,
                'stock': 10,
                'image': 'bose_qc45.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Накладные беспроводные'},
                    {'name': 'Шумоподавление', 'value': 'Технология Bose ANC'},
                    {'name': 'Время работы', 'value': 'До 24 часов'},
                    {'name': 'Особенности', 'value': 'Режим Aware, эквалайзер в приложении'},
                    {'name': 'Подключение', 'value': 'Bluetooth 5.1, мультиточка'},
                    {'name': 'Зарядка', 'value': 'USB-C, быстрая зарядка (15 мин = 3 часа)'}
                ]
            },
            {
                'name': 'Sennheiser Momentum True Wireless 3',
                'description': 'Аудиофильские TWS-наушники с фирменным звучанием Sennheiser и адаптивным шумоподавлением',
                'price': 18999.00,
                'old_price': 21999.00,
                'stock': 8,
                'image': 'sennheiser_momentum3.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'Адаптивное ANC'},
                    {'name': 'Защита', 'value': 'IPX4 (влагозащита)'},
                    {'name': 'Время работы', 'value': 'До 7 часов (28 часов с футляром)'},
                    {'name': 'Особенности', 'value': 'aptX Adaptive, Sound Zones, Sound Check'},
                    {'name': 'Зарядка', 'value': 'USB-C, беспроводная'}
                ]
            },
            {
                'name': 'Jabra Elite 7 Pro',
                'description': 'Компактные TWS-наушники с технологией MultiSensor Voice для кристально чистых звонков',
                'price': 12999.00,
                'old_price': 14999.00,
                'stock': 22,
                'image': 'jabra_elite7pro.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'Регулируемое ANC'},
                    {'name': 'Защита', 'value': 'IP57 (пыле- и водонепроницаемость)'},
                    {'name': 'Время работы', 'value': 'До 8 часов (30 часов с футляром)'},
                    {'name': 'Особенности', 'value': 'MultiSensor Voice, HearThrough, настраиваемый эквалайзер'},
                    {'name': 'Зарядка', 'value': 'USB-C, беспроводная (Qi)'}
                ]
            },
            {
                'name': 'Nothing Ear (1)',
                'description': 'Стильные прозрачные TWS-наушники с активным шумоподавлением и уникальным дизайном',
                'price': 8999.00,
                'old_price': 10999.00,
                'stock': 30,
                'image': 'nothing_ear1.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'ANC до 40 дБ'},
                    {'name': 'Защита', 'value': 'IPX4 (влагозащита)'},
                    {'name': 'Время работы', 'value': 'До 5.7 часов (34 часа с футляром)'},
                    {'name': 'Особенности', 'value': 'Прозрачный дизайн, настраиваемые жесты'},
                    {'name': 'Зарядка', 'value': 'USB-C, беспроводная'}
                ]
            },
            {
                'name': 'Audio-Technica ATH-M50xBT2',
                'description': 'Беспроводная версия легендарных студийных наушников с фирменным звучанием',
                'price': 15999.00,
                'old_price': 17999.00,
                'stock': 12,
                'image': 'ath_m50xbt2.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Накладные беспроводные'},
                    {'name': 'Драйверы', 'value': '45 мм с редкоземельными магнитами'},
                    {'name': 'Время работы', 'value': 'До 50 часов'},
                    {'name': 'Особенности', 'value': 'Кодеки LDAC, AAC, SBC, мультиточка'},
                    {'name': 'Подключение', 'value': 'Bluetooth 5.0, 3.5 мм кабель'},
                    {'name': 'Зарядка', 'value': 'USB-C, быстрая зарядка'}
                ]
            },
            {
                'name': 'Apple AirPods Max',
                'description': 'Премиальные полноразмерные наушники Apple с фирменным чипом H1 и пространственным звуком',
                'price': 44999.00,
                'old_price': 54999.00,
                'stock': 5,
                'image': 'airpods_max.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Накладные беспроводные'},
                    {'name': 'Шумоподавление', 'value': 'Активное с адаптивным эквалайзером'},
                    {'name': 'Время работы', 'value': 'До 20 часов'},
                    {'name': 'Особенности', 'value': 'Пространственный звук, динамическое отслеживание движений головы'},
                    {'name': 'Материалы', 'value': 'Алюминий, сетчатый тканевый материал, память формы'},
                    {'name': 'Зарядка', 'value': 'Lightning'}
                ]
            },
            {
                'name': 'JBL Tune 760NC',
                'description': 'Доступные беспроводные наушники с хорошим шумоподавлением и фирменным звуком JBL',
                'price': 6999.00,
                'old_price': 8499.00,
                'stock': 35,
                'image': 'jbl_tune760nc.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'Накладные беспроводные'},
                    {'name': 'Шумоподавление', 'value': 'Активное ANC'},
                    {'name': 'Время работы', 'value': 'До 35 часов с ANC (50 часов без ANC)'},
                    {'name': 'Особенности', 'value': 'JBL Pure Bass Sound, быстрая зарядка'},
                    {'name': 'Подключение', 'value': 'Bluetooth 5.0, 3.5 мм кабель'},
                    {'name': 'Зарядка', 'value': 'USB-C (5 мин = 2 часа)'}
                ]
            },
            {
                'name': 'Xiaomi Redmi Buds 3 Pro',
                'description': 'Доступные TWS-наушники с активным шумоподавлением и длительным временем работы',
                'price': 4999.00,
                'old_price': 5999.00,
                'stock': 40,
                'image': 'redmi_buds3pro.jpg',
                'specs': [
                    {'name': 'Тип', 'value': 'TWS (True Wireless Stereo)'},
                    {'name': 'Шумоподавление', 'value': 'ANC до 35 дБ'},
                    {'name': 'Защита', 'value': 'IPX4 (влагозащита)'},
                    {'name': 'Время работы', 'value': 'До 6 часов (28 часов с футляром)'},
                    {'name': 'Особенности', 'value': 'Режим прозрачности, двойное подключение'},
                    {'name': 'Зарядка', 'value': 'USB-C, беспроводная'}
                ]
            }
        ]
    }
    
    created_products = []
    
    # Получаем все категории из базы данных
    all_categories = {category.name: category for category in categories}
    
    # Создаем продукты для каждой категории
    for category_name, products in products_data.items():
        category = all_categories.get(category_name)
        if not category:
            print(f"Категория '{category_name}' не найдена в базе данных")
            continue
            
        for product_data in products:
            # Проверка на существование продукта
            existing = Product.query.filter_by(name=product_data['name']).first()
            if existing:
                print(f"Товар '{product_data['name']}' уже существует")
                created_products.append(existing)
                continue
                
            # Создание нового продукта
            slug = slugify(product_data['name'])
            product = Product(
                name=product_data['name'],
                slug=slug,
                description=product_data['description'],
                price=product_data['price'],
                old_price=product_data.get('old_price'),
                stock=product_data.get('stock', 0),
                image=product_data.get('image'),
                category_id=category.id,
                is_featured=True if random.random() > 0.7 else False,
                is_new=True if random.random() > 0.7 else False,
                is_sale=True if 'old_price' in product_data and random.random() > 0.5 else False
            )
            db.session.add(product)
            db.session.flush()  # Чтобы получить id продукта для спецификаций
            
            # Добавляем спецификации товара
            if 'specs' in product_data:
                for spec in product_data['specs']:
                    specification = Specification(
                        product_id=product.id,
                        name=spec['name'],
                        value=spec['value']
                    )
                    db.session.add(specification)
            
            created_products.append(product)
            print(f"Создан товар: {product_data['name']} в категории {category_name}")
    
    db.session.commit()
    return created_products

if __name__ == '__main__':
    with app.app_context():
        print("Инициализация базы данных...")
        try:
            db.create_all()
            print("Таблицы созданы успешно")
            
            print("\nСоздание категорий...")
            categories = create_categories()
            
            print("\nСоздание товаров...")
            products = create_products(categories)
            
            print(f"\nУспешно создано {len(categories)} категорий и {len(products)} товаров")
        except Exception as e:
            print(f"Ошибка при заполнении базы данных: {str(e)}")
