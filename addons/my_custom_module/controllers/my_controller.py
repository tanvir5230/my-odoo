from odoo import http
from odoo.http import request


class MyModelController(http.Controller):

    @http.route('/test', auth='public', website=True)
    def test_page(self, **kwargs):
        records = request.env['my_custom_model.my_custom_model'].search([])
        return request.render('my_custom_module.test_template', {'records': records})
