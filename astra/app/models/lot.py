from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Lot(models.Model):
    id = fields.BigIntField(pk=True)