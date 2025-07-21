{
    'name': 'Restaurant Management POS',
    'version': '17.0.1.0.0',
    'author': 'Pedro Contreras',
    'website': 'https://www.tuempresa.com',
    'category': 'Sales',
    'depends': ['point_of_sale', 'base'],
    'data': [

    ],
    'assets': {
        'point_of_sale._assets_pos': [
            # Screens
            'restaurant_management_pos/static/src/app/screens/product_screen/*.js',
            'restaurant_management_pos/static/src/app/screens/product_screen/*.scss',
            'restaurant_management_pos/static/src/app/screens/product_screen/*.xml',
            
            'restaurant_management_pos/static/src/app/screens/ticket_screen/*.js',
            'restaurant_management_pos/static/src/app/screens/ticket_screen/*.scss',
            'restaurant_management_pos/static/src/app/screens/ticket_screen/*.xml',

            'restaurant_management_pos/static/src/app/screens/table_select_screen/*.scss',
            'restaurant_management_pos/static/src/app/screens/table_select_screen/*.xml',
            'restaurant_management_pos/static/src/app/screens/table_select_screen/*.js',

            'restaurant_management_pos/static/src/app/screens/product_screen/action_pad/*.js',
            'restaurant_management_pos/static/src/app/screens/product_screen/action_pad/*.xml',

            # Store components
            'restaurant_management_pos/static/src/app/store/*.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
