# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: Odoo function to compare floats based on specific precisions
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - UserError: Warning Exception to use with raise
#  - Command: x2Many commands namespace
# To return an action, assign: action = {...}

for line in record:

    line['x_studio_status'] = 'in progress'
    stage = env['x_reservation_stage'].search([('x_name', '=', 'In Progress')])
    for row_stage in stage:
        line['x_studio_stage_id'] = row_stage.id

    rec_opr_type = 0
    opr_type = env['stock.picking.type'].search(
        [('name', '=', 'Inventory Issued')])
    for row_opr_type in opr_type:
        rec_opr_type = row_opr_type.id

    rec_src_loc = 0
    src_loc = env['stock.location'].search([('name', '=', 'Quarry')])
    for row_src_loc in src_loc:
        rec_src_loc = row_src_loc.id

    if rec_opr_type:
        if rec_src_loc:
            seq_no = env['ir.sequence'].next_by_code('gi.wh.out.sequence')

            rec_gi = env['stock.picking'].create({'location_dest_id': rec_src_loc,
                                                  'location_id': rec_src_loc,
                                                  'picking_type_id': rec_opr_type,
                                                  'x_studio_many2one_reservation': line.id,
                                                  'x_studio_create_by_reservation': 1,
                                                  'name': seq_no
                                                  })

            if rec_gi:
                for row_gi in rec_gi:
                    gi_id = row_gi.id

                for item in line.x_reservation_line_ids_f5c60:
                    env['stock.move'].create({'product_id': item.x_studio_many2one_field_vym0h.id,
                                              'product_uom_qty': item.x_studio_quantity,
                                              'picking_id': gi_id,
                                              'name': item.x_studio_many2one_field_vym0h.name,
                                              'product_uom': item.x_studio_uom.id,
                                              'location_id': rec_src_loc,
                                              'location_dest_id': rec_src_loc
                                              })

                line['x_studio_create_gi'] = True
                line['x_studio_gi'] = gi_id
