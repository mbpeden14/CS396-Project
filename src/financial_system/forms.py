from django import forms
from .models import *
from .import models

class UserChoiceField(forms.Form):
    users = forms.ModelChoiceField(
        queryset=User.objects.values_list("name", flat=True).distinct(),
        empty_label=None
    )

class AgentChoiceField(forms.Form):
    agents = forms.ModelChoiceField(
        queryset=Agent.objects.values_list("name", flat=True).distinct(),
        empty_label=None
    )

class NewPropertyForm(forms.ModelForm):
    class Meta:
        model = models.Property
        fields = ['address', 'transaction_price', 'agent', 'current_owner']

class NewBondForm(forms.ModelForm):
    class Meta:
        model = models.Bond
        fields = ['issuer', 'name', 'bond_yield']

class NewMiscProductForm(forms.ModelForm):
    description = forms.CharField(
		widget=forms.Textarea(attrs={'rows':5,'placeholder':"Type something..."}),
		max_length=250,
		help_text="250 words max.")
        
    class Meta:
        model = models.MiscProduct
        fields = ['name', 'product_type', 'transaction_price', 'description', 'agent']

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = models.StockTransaction
        fields = ['transaction_type', 'shares', 'agent', 'user']

class PropertyTransactionForm(forms.ModelForm):
    class Meta:
        model = models.PropertyTransaction
        fields = ['agent', 'user']

class OtherTransactionForm(forms.ModelForm):
    class Meta:
        model = models.OtherTransaction
        fields = ['amount', 'user']

class AddUserExpendituresForm(forms.ModelForm):
    class Meta:
        model = models.UserExpenditures
        fields = [
            'user', 
            'food',
            'health',
            'entertainment',
            'vehicle_fuel',
            'children',
            'travel',
            'other',
            'start_date',
            'end_date'
        ]

    start_date = forms.DateField(
        widget=forms.SelectDateWidget
    )

    end_date = forms.DateField(
        widget=forms.SelectDateWidget
    )

class ExpenditureDateForm(forms.Form):
    user = forms.CharField(max_length=125)

    start_date = forms.DateField(
        widget=forms.SelectDateWidget
    )

    end_date = forms.DateField(
        widget=forms.SelectDateWidget
    )

class UserTransactionsForm(forms.Form):
    name = forms.CharField(max_length=125)
    date = forms.DateTimeField()

class StockDataOnDateForm(forms.Form):
    name = forms.CharField(max_length=125)
    date = forms.DateTimeField()

class PropertyDataForm(forms.Form):
    address = forms.CharField(max_length=125)

class BondDataForm(forms.Form):
    name = forms.CharField(max_length=125)

class AgentAssetsForm(forms.Form):
    name = forms.CharField(max_length=125)

class LoanRatingsForm(forms.Form):
    name = forms.CharField(max_length=125)