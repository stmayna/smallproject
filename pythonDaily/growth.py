
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class TestModel(models.Model):
    _inherit = 'TestModel'


    '''
    Project: PIM
    Technical:
    
    '''

    def create_return_request_pim(self):
        for line in record:
            rec_opr_type = 0
            opr_type = env['stock.picking.type'].search(
                [('name', '=', 'Returns')])
            for row_opr_type in opr_type:
                rec_opr_type = row_opr_type.id

            rec_src_loc = 0
            src_loc = env['stock.location'].search(['&',('name', '=', 'Stock'),('location_id', '=', 'QUA')])
            for row_src_loc in src_loc:
                rec_src_loc = row_src_loc.id

            if rec_opr_type:
                if rec_src_loc:
                    seq_no = env['ir.sequence'].next_by_code('return.request')

                    return_doc = env['stock.picking'].create({'location_dest_id': rec_src_loc,
                                                            'location_id': rec_src_loc,
                                                            'picking_type_id': rec_opr_type,
                                                            'x_studio_return_request': line.id,
                                                            'x_studio_many2one_reservation': line.x_studio_reservation_list.id,
                                                            'x_studio_equipment': line.x_studio_equipment.id,
                                                            'x_studio_work_order': line.x_studio_work_order.id
                                                            })

                    if return_doc:
                        for row_return in return_doc:
                            record['x_studio_returns'] = row_return.id
                            return_id = row_return.id

                        for item in line.x_studio_one2many_field_GZr1p:
                            env['stock.move'].create({'product_id': item.x_studio_product.id,
                                                    'product_uom_qty': item.x_studio_quantity,
                                                    'picking_id': return_id,
                                                    'name': item.x_studio_product.name,
                                                    'product_uom': item.x_studio_uom.id,
                                                    'location_id': rec_src_loc,
                                                    'location_dest_id': rec_src_loc
                                                    })


    '''
    Project: Prager
    Technical:

    '''

    def create_return_request_prager(self):
        for transaction in records:
            if transaction.x_studio_status_bar == 'in progress' and not transaction.x_studio_returns:
                # Find the picking type for returns in the given warehouse
                picking_type_name = 'Returns'
                picking_type = env['stock.picking.type'].search([('name', '=', picking_type_name), ('warehouse_id', '=', transaction.x_studio_destination_warehouse.id)], limit=1)
                if not picking_type:
                    raise UserError("No picking type found for warehouse {} and type {}".format(transaction.x_studio_destination_warehouse.id, picking_type_name))
            
                # Find the source location with the complete name of the return request
                src_loc = env['stock.location'].search([('complete_name', '=', transaction.x_studio_location.complete_name)], limit=1)
                if not src_loc:
                    raise UserError("No location found with name {}".format(transaction.x_studio_location.complete_name))
                    
                # Find the destination location with the complete name of the return request
                dest_loc = env['stock.location'].search([('complete_name', '=', transaction.x_studio_destination_location.complete_name)], limit=1)
                if not dest_loc:
                    raise UserError("No location found with name {}".format(transaction.x_studio_destination_location.complete_name))
                    
                stock_move_vals = {
                    'location_id': src_loc.id,
                    'location_dest_id': dest_loc.id,
                    'picking_type_id': picking_type.id,
                    'x_studio_return_request': transaction.id,
                    'x_studio_many2one_reservation': transaction.x_studio_reservation_list.id,
                    'x_studio_equipment': transaction.x_studio_equipment.id,
                    'x_studio_work_order': transaction.x_studio_work_order.id,
                }
                
                # Create new transfer and update transaction picking ID
                stock_picking = env['stock.picking'].create(stock_move_vals)
                
                stock_picking_vals = []
                for line in transaction.x_studio_one2many_field_GZr1p:
                    stock_picking_vals.append((0, 0, {
                        'product_id': line.x_studio_product.id,
                        'product_uom_qty': line.x_studio_quantity,
                        'name': 'from return request',
                        'product_uom': line.x_studio_uom.id,
                        'location_id': src_loc.id,
                        'location_dest_id': dest_loc.id,
                        'picking_id': stock_picking.id,
                    }))

                stock_picking.write({'move_ids_without_package': stock_picking_vals})

                stock_picking.action_confirm()
                stock_picking.action_assign()

                transaction['x_studio_returns'] = stock_picking.id

