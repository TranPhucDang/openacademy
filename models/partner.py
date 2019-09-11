# -*- coding: utf-8 -*-, api
from odoo import fields, models      # import fields, models vao odoo

# khoi tao doi tuong Partner
class Partner(models.Model):
    _name = 'academy_dang.partner' # thuoc tinh cua model Partner dung de dinh danh Partner & khi do tao ra 1 bang CSDL co ten la 'academy_dang.partner' 
    _description = 'Partner'      # thuoc tinh dinh nghia model Partner

    name = fields.Char()	  # thuoc tinh cua record du lieu cua thuoc tinh name o dang ky tu

    instructor = fields.Boolean(default=False) 
    session_ids = fields.Many2many('academy_dang.session', string="Attended Sessions", readonly=True)
				  # tao lien ket dang many2one voi model 'academy_dang.session' thong qua thuoc tinh instructor_ids & khong cho phep chinh sua du lieu cua 'openacademy.session'
