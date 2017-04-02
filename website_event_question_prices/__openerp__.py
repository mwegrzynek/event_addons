# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Event question pricing',
    'version': '1.0.0',
    'category': 'Marketing',
    'description': '''
    Adds products to questions answers; selecting an answer with product will
    add it to the cart.
    ''',
    'author': 'Michał Węgrzynek',
    'website': 'https://malloc.com.pl',
    'depends': [
        'event_sale',
        'website_event_questions',
        'website_event_sale'
    ],
    'data': [
        'views/event_answer.xml'
    ],
    'demo': [
        'data/demo.xml'
    ],
    'installable': True,
    'auto_install': False
}
