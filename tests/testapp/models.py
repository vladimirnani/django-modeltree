# -*- coding: utf-8 -*-

from django.db import models


class BaseModel(models.Model):
    def __str__(self):
        model_name = type(self)._meta.model_name
        return '{} [{}]'.format(model_name, self.id)

    class Meta:
        abstract = True


class ModelA(BaseModel):
    id = models.SmallIntegerField(primary_key=True)
    model_b = models.OneToOneField('ModelB', blank=True, null=True, on_delete=models.SET_NULL)
    model_c = models.ForeignKey('ModelC', blank=True, null=True, on_delete=models.SET_NULL)
    model_d = models.ManyToManyField('ModelD', blank=True)


class ModelB(BaseModel):
    id = models.SmallIntegerField(primary_key=True)
    model_b = models.OneToOneField('ModelB', blank=True, null=True, on_delete=models.SET_NULL)
    model_c = models.ForeignKey('ModelC', blank=True, null=True, on_delete=models.SET_NULL)


class ModelC(BaseModel):
    id = models.SmallIntegerField(primary_key=True)
    model_d = models.ManyToManyField('ModelD', blank=True)


class ModelD(BaseModel):
    id = models.SmallIntegerField(primary_key=True)


class ModelE(BaseModel):
    id = models.SmallIntegerField(primary_key=True)
    model_d = models.OneToOneField('ModelD', blank=True, null=True, on_delete=models.SET_NULL)
    model_c = models.ForeignKey('ModelC', blank=True, null=True, on_delete=models.SET_NULL)
    model_b = models.ManyToManyField('ModelB', blank=True)
