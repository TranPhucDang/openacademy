# -*- coding: utf-8 -*-
from odoo import fields, models
## tao doi tuong Course 
### cac thuoc tinh de dinh nghia Course bao gom: _name, _description
### cac thuoc tinh de dinh nghia cac record trong Course: name, description, reponsible_id, session_ids, level
class Course(models.Model):
    _name = 'academy_dang.course' # thuoc tinh _name quan trong dung dinh danh model
				 # _name khoi tao mot bang CSDL ten 'academy_dang.course'
				 # ngoai ra _name tuong tac voi cac model khac thong qua ten 'openacademy.course'
    _description = 'Course'	 # thuoc tinh dung de dinh nghia model Course
				

    name = fields.Char(name='Title', required=True) # tao thuoc tinh name cua record voi ten 'Title' va bat buoc phai nhap
    description = fields.Text()  # thuoc tinh description cho phep nguoi dung nhap du lieu voi dang text

    responsible_id = fields.Many2one('academy_dang.partner', string="Responsible")
	                         # tao lien ket dang many2one voi model 'academy_dang.partner' thong qua thuoc tinh responsible_id 
    session_ids = fields.One2many('academy_dang.session', 'course_id', string="Sessions")
				 # tao lien ket dang on2many voi model 'academy_dang.session' thong qua thuoc tinh session_ids
    level = fields.Selection([(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")
				 # thuoc tinh level cho phep nguoi dung chon lua 3 thong tin co sang la easy, medium, hard


## tao doi tuong Session 
### cac thuoc tinh de dinh nghia Course bao gom: _name, _description
### cac thuoc tinh de dinh nghia cac record trong Course: name, active, state,...
class Session(models.Model):
    _name = 'academy_dang.session' # _name thuoc tinh quan trong de dinh danh Session 
    _description = 'Session'      # thuoc tinh dung de dinh nghia model Session gia tri cua _description la 'Session'

    name = fields.Char(required=True) # thuoc tinh name cua record, du lieu dang chuoi va bat buoc phai co khi tao
    active = fields.Boolean(default=True) # thuoc tinh active, kieu logic 2 gia tri True va False, mat dinh la True
					  # active the hien duoi dang dau tick 
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')
                                          # thuoc tinh level cho phep nguoi dung chon lua 3 thong tin co sang la draft, comfirmed, done & mac dinh la draft
    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)
					 # thuoc tinh duration dang so thuc co gia tri toi da la 6 so va 2 so sau dau phay mac dinh la 1
    instructor_id = fields.Many2one('academy_dang.partner', string="Instructor")
					# tao lien ket dang many2one voi model 'academy_dang.partner' thong qua thuoc tinh instructor_id
    course_id = fields.Many2one('academy_dang.course', ondelete='cascade', string="Course", required=True)
					 # tao lien ket dang many2one voi model 'academy.course' thong qua thuoc tinh course_id & bat buoc phai thuc hien
    attendee_ids = fields.Many2many('academy_dang.partner', string="Attendees")
					 # tao lien ket dang on voi model 'academy_dang.partner' thong qua thuoc tinh attendee_ids

