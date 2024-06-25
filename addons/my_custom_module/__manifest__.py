{
    'name': 'My Custom Module',
    'version': '1.0',
    'depends': ['base', 'website'],
    'data': ['security/ir.model.access.csv', 'views/menu.xml', 'views/action.xml', 'views/template.xml'],
    'assets': {
        'web.assets_frontend': [
            'my_custom_module/static/js/my_script.js',
            'my_custom_module/static/css/my_style.css'
        ]
    },
    'installable': True,
    'application': True,
}
