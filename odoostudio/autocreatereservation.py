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


for line in records:
    if line.equipment_id:
        seq_no = env['ir.sequence'].next_by_code('resv.test')

        reservation = env['x_reservation'].create({'x_name': seq_no,
                                                   'x_studio_work_order': line.id,
                                                   'x_studio_equipment': line.equipment_id.id,
                                                   'create_date': line.create_date,
                                                   'create_uid': line.create_uid
                                                   })

        if reservation:
            resv_id = 0.
            for row_resv in reservation:
                resv_id = row_resv.id

            line['x_studio_create_reservation'] = True
            line['x_studio_reservation'] = resv_id
