from odoo import fields, http, tools, _
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request


class CustomerPortal(http.Controller):

    @http.route('/advance_search_product', auth='public', website=True, type='json', csrf=False)
    def advance_search_product(self, **post):
        products = request.env['product.template'].sudo().search_read(
            [('name', 'ilike', post.get('product_search'))])
        return request.env['ir.ui.view'].render_template('website_advance_product_search.productsSearchBarSolution',
                                                         {'products': products})
