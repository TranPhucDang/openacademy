# -*- coding: utf-8 -*-
from odoo import api, exceptions, fields, models


## tao doi tuong Course
### cac thuoc tinh de dinh nghia Course bao gom: _name, _description
### cac thuoc tinh de dinh nghia cac record trong Course: name, description, reponsible_id, session_ids, level
class Course(models.Model):
    _name = 'openacademy_pd.course_1'  # thuoc tinh _name quan trong dung dinh danh model
    # _name khoi tao mot bang CSDL ten 'openacademy.course'
    # ngoai ra _name tuong tac voi cac model khac thong qua ten 'openacademy.course'
    _description = 'Course'  # thuoc tinh dung de dinh nghia model Course

    name = fields.Char(name='Title',
                       required=True)  # tao thuoc tinh name cua record voi ten 'Title' va bat buoc phai nhap
    description = fields.Text()  # thuoc tinh description cho phep nguoi dung nhap du lieu voi dang text

    responsible_id = fields.Many2one('openacademy_pd.partner_1', string="Responsible")
    # tao lien ket dang many2one voi model 'openacademy.partner' thong qua thuoc tinh responsible_id
    session_ids = fields.One2many('openacademy_pd.session_1', 'course_id', string="Sessions")
    # tao lien ket dang on2many voi model 'openacademy.session' thong qua thuoc tinh session_ids
    level = fields.Selection([(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")
    # thuoc tinh level cho phep nguoi dung chon lua 3 thong tin co sang la easy, medium, hard


## tao doi tuong Session 
### cac thuoc tinh de dinh nghia Course bao gom: _name, _description
### cac thuoc tinh de dinh nghia cac record trong Course: name, active, state,...
class Session(models.Model):
    _name = 'openacademy_pd.session_1'  # _name thuoc tinh quan trong de dinh danh Session
    _description = 'Session'  # thuoc tinh dung de dinh nghia model Session gia tri cua _description la 'Session'

    name = fields.Char(required=True)  # thuoc tinh name cua record, du lieu dang chuoi va bat buoc phai co khi tao
    active = fields.Boolean(default=True)  # thuoc tinh active, kieu logic 2 gia tri True va False, mat dinh la True
    # active the hien duoi dang dau tick
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')
    # thuoc tinh level cho phep nguoi dung chon lua 3 thong tin co sang la draft, comfirmed, done & mac dinh la draft
    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)
    # thuoc tinh duration dang so thuc co gia tri toi da la 6 so va 2 so sau dau phay mac dinh la 1
    instructor_id = fields.Many2one('openacademy_pd.partner_1', string="Instructor")
    # tao lien ket dang many2one voi model 'openacademy.partner' thong qua thuoc tinh instructor_id
    course_id = fields.Many2one('openacademy_pd.course_1', ondelete='cascade', string="Course", required=True)
    # tao lien ket dang many2one voi model 'openacademy.course' thong qua thuoc tinh course_id & bat buoc phai thuc hien
    attendee_ids = fields.Many2many('openacademy_pd.partner_1', string="Attendees")
    # tao lien ket dang on voi model 'openacademy.partner' thong qua thuoc tinh attendee_ids
    seats = fields.Integer()

    ###
    ## Using computed fields
    ###
    taken_seats = fields.Float(compute='_compute_taken_seats', store=True)

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for session in self:
            if not session.seats:
                session.taken_seats = 0.0
            else:
                session.taken_seats = 100.0 * len(session.attendee_ids) / session.seats

    ###
    ## using onchange
    ###
    @api.onchange('seats', 'attendee_ids')
    def _change_taken_seats(self):
        if self.taken_seats > 100:
            return {'warning': {
                'title':   'Too many attendees',
                'message': 'The room has %s available seats and there is %s attendees registered' % (self.seats, len(self.attendee_ids))
            }}

    ###
    ## using python constrains
    ###
    @api.constrains('seats', 'attendee_ids')
    def _check_taken_seats(self):
        for session in self:
            if session.taken_seats > 100:
                raise exceptions.ValidationError('The room has %s available seats and there is %s attendees registered' % (session.seats, len(session.attendee_ids)))

    ###
    ## using SQL constrains
    ###
    _sql_constraints = [
        # possible only if taken_seats is stored
        ('session_full', 'CHECK(taken_seats <= 100)', 'The room is full'),
    ]