import xml.etree.ElementTree as ET


async def generate_xml(products: list[dict]):
    root = ET.Element('sales_data')
    products_element = ET.SubElement(root, 'products')

    for product_data in products:
        product_element = ET.SubElement(products_element, 'product')
        ET.SubElement(product_element, 'name').text = product_data.name
        ET.SubElement(product_element, 'quantity').text = str(product_data.quantity)
        ET.SubElement(product_element, 'price').text = str(product_data.price)
        ET.SubElement(product_element, 'category').text = product_data.category

    tree = ET.ElementTree(root)
    tree.write('report.xml', encoding='utf-8', xml_declaration=True)
