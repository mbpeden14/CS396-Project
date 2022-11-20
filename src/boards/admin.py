from django.contrib import admin
from .import models as models
from files import models as m
from financial_system import models as fm
# Register your models here.


admin.site.register(models.Board)
admin.site.register(models.Topic)
admin.site.register(models.Post)
admin.site.register(m.MyFileUpload)
admin.site.register(fm.Agent)
admin.site.register(fm.User)
admin.site.register(fm.Bank)
admin.site.register(fm.Property)
admin.site.register(fm.Stock)
admin.site.register(fm.MiscProduct)
admin.site.register(fm.TransactionTypes)
admin.site.register(fm.StockTransaction)
admin.site.register(fm.PropertyTransaction)
admin.site.register(fm.OtherTransaction)
