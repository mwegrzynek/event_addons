# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Event question pricing (ticket configurator)',
    'version': '1.0.0',
    'category': 'Marketing',
    'description': 'Adds prices to answers to questions to create a ticket configurator',
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
