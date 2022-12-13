# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class school(models.Model):
#     _name = 'school.school'
#     _description = 'school.school'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char()
    description = fields.Text()


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char()
    description = fields.Text()
    year = fields.Integer()
    topic_id = fields.Many2one("school.topic")

class topic(models.Model):
    _name = 'school.topic'
    _description = 'school.topic'
    name = fields.Char(String = "Topic")
