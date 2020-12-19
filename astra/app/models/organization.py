from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class OrganizationModel(models.Model):
    id = fields.BigIntField(pk=True)
    orgid = fields.BigIntField(default=None,null=True)
    name = fields.TextField(default=None,null=True)
    inn = fields.TextField(default=None,null=True)
    ogrn = fields.TextField(default=None,null=True)
    kpp = fields.TextField(default=None,null=True)
    address = fields.TextField(default=None,null=True)
    email = fields.TextField(default=None,null=True)
    phone = fields.TextField(default=None,null=True)

