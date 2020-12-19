from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class SupplyModel(models.Model):
    #orm_mode = True
    id = fields.BigIntField(pk=True)
    title = fields.TextField(default=None,null=True)
    organization_id = fields.BigIntField(default=None,null=True)
    lot_id = fields.BigIntField(default=None,null=True)
    refnum = fields.TextField(default=None,null=True)
    org_name = fields.TextField(default=None,null=True)
    platform = fields.TextField(default=None,null=True)
    status = fields.TextField(default=None,null=True)
    summary = fields.TextField(default=None,null=True)
    iks = fields.TextField(default=None, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    end_at = fields.DatetimeField(auto_now=True)
    final_at = fields.DatetimeField(auto_now=True)
    price = fields.BigIntField(default=None,null=True)
    credit = fields.TextField(default=None,null=True)
    require = fields.IntField(default=0, null=True)
    partner1_id = fields.BigIntField(default=None, null=True)
    partner2_id = fields.BigIntField(default=None, null=True)
    partner1_name = fields.TextField(default=None, null=True)
    partner2_name = fields.TextField(default=None, null=True)
    partner1_type = fields.TextField(default=None, null=True)
    partner2_type = fields.TextField(default=None, null=True)
    partner1_price = fields.TextField(default=None, null=True)
    partner2_price = fields.TextField(default=None, null=True)


Supply = pydantic_model_creator(SupplyModel, name="SupplyModel")

