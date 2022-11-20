from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=6)
    occupation = models.CharField(max_length=125)

    class Meta:
        managed = False
        db_table = 'financial_system_user'

    def __str__(self):
        return self.name

class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    firm = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    fee = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'financial_system_agent'

    def __str__(self):
        return self.name

class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    open_price = models.DecimalField(max_digits=9, decimal_places=2)
    close_price = models.DecimalField(max_digits=9, decimal_places=2)
    high_price = models.DecimalField(max_digits=9, decimal_places=2)
    low_price = models.DecimalField(max_digits=9, decimal_places=2)
    volume = models.IntegerField()
    date = models.DateField(auto_now = True)

    def __str__(self):
        return self.name

class Property(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=125)
    transaction_price = models.DecimalField(max_digits=9, decimal_places=2)
    current_owner = models.ForeignKey(User, on_delete = models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "properties"

    def __str__(self):
        return self.address

class Bond(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    issuer = models.ForeignKey(Bank, on_delete = models.CASCADE)
    bond_yield = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

class MiscProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    product_type = models.CharField(max_length=125)
    transaction_price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(max_length = 255)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Other Product"

    def __str__(self):
        return self.name

class TransactionTypes(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=125)

    class Meta:
        verbose_name = "Transaction Type"

    def __str__(self):
        return self.type

class StockTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now = True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_type = models.ForeignKey(TransactionTypes, on_delete = models.CASCADE)
    shares = models.IntegerField()

    class Meta:
        verbose_name = "Stock Transaction"

class PropertyTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now = True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_type = models.ForeignKey(TransactionTypes, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Property Transaction"

class OtherTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(MiscProduct, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now = True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    transaction_type = models.ForeignKey(TransactionTypes, on_delete = models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        verbose_name = "Other Product Transaction"
