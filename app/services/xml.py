from datetime import datetime

import lxml.etree as ET


async def generate_xml(products: list[dict]):
    '''
    Генерирует XML-файл с данными о продажах.
    '''
    root = ET.Element('sales_data', date=get_current_date())
    products_element = ET.SubElement(root, 'products')

    for product_data in products:
        product_element = ET.SubElement(products_element, 'product')
        ET.SubElement(
            product_element,
            'name').text = product_data.name
        ET.SubElement(
            product_element,
            'quantity').text = str(product_data.quantity)
        ET.SubElement(
            product_element,
            'price').text = str(product_data.price)
        ET.SubElement(
            product_element,
            'category').text = product_data.category

    tree = ET.ElementTree(root)
    tree.write(
        'report.xml',
        encoding='utf-8',
        xml_declaration=True,
        pretty_print=True
    )


def generate_prompt():
    '''
    Генерирует промпт для нейросети на основе XML-файла с данными о продажах.
    '''
    xml_file = 'report.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()

    date = root.get('date')
    products = root.find('products')

    total_revenue = 0
    product_data = []
    categories_count = {}

    for product_element in products.findall('product'):
        product_name = product_element.find('name').text
        product_quantity = int(product_element.find('quantity').text)
        product_price = float(product_element.find('price').text)
        product_revenue = product_quantity * product_price
        total_revenue += product_revenue

        product_data.append((product_name, product_revenue))
        category = product_element.find('category').text
        categories_count[category] = categories_count.get(category, 0) + 1

    top_products = '\n'.join(
        f'- {name}: {revenue} руб.' for name, revenue in sorted(
            product_data,
            key=lambda x: x[1], reverse=True)[:3]
    )
    categories = '\n'.join(
        f'-{category}: {count}' for category, count in categories_count.items()
    )

    prompt = f'''Проанализируй данные о продажах за {date}:

        1. Общая выручка: {total_revenue} руб.

        2. Топ-3 товара по продажам: {top_products}

        3. Распределение по категориям: {categories}

        Составь краткий аналитический отчет с выводами и рекомендациями.'''

    return prompt


def get_current_date():
    '''
    Возвращает текущую дату в формате YYYY-MM-DD.
    '''
    now = datetime.now()
    return now.strftime('%Y-%m-%d')
