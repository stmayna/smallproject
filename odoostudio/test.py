for record in records:
    if (record.x_studio_reservation_item):
    record['move_ids_without_package'] = [(5,0,0)]  #clear
    record['move_lines'] = [(5,0,0)]                #clear
    for line in record.x_studio_reservation_item:
        record['move_ids_without_package'] = [(0,0,{'product_id':line.x_studio_many2one_field_vym0h, 
                                            'product_uom_qty':line.x_studio_quantity,
                                            'picking_id':record,
                                            'name':line.x_studio_many2one_field_vym0h.name,
                                            'product_uom':line.x_studio_uom,
                                            'location_id':record.location_id,
                                            'location_dest_id':record.location_dest_id
        })]
        # record['move_lines'] = [(0,0,{'product_id':line.x_studio_many2one_field_vym0h, 'product_uom_qty':line.x_studio_quantity, 'picking_id':record,'name':line.x_studio_many2one_field_vym0h.name})]




