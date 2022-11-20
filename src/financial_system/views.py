from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import *
from .models import *

from financial_system.models import MiscProduct, Property, Stock

# Create your views here.

class StocksListView(ListView):
	model = Stock
	context_object_name = 'stocks'
	template_name = 'financial_system/stocks.html'

class PropertiesListView(ListView):
	model = Property
	context_object_name = 'properties'
	template_name = 'financial_system/properties.html'

class BondsListView(ListView):
	model = Bond
	context_object_name = 'bonds'
	template_name = 'financial_system/bonds.html'

class MiscListView(ListView):
    model = MiscProduct
    context_object_name = 'misc_products'
    template_name = 'financial_system/misc_products.html'

def new_property(request):
	context = dict()
	form = NewPropertyForm()
	if request.method == 'POST':
		form = NewPropertyForm(request.POST)

		if form.is_valid():
			address = form.cleaned_data["address"]
			transaction_price = form.cleaned_data["transaction_price"]
			agent = form.cleaned_data["agent"]
			current_owner = form.cleaned_data["current_owner"]

			p = Property(address=address, transaction_price=transaction_price, agent=agent, current_owner=current_owner)
			p.save()

			return redirect('../')

		else:
			pass
	
	template = 'financial_system/new_property.html'
	context['form'] = form

	return render(request, template, context)

def new_bond(request):
	context = dict()
	form = NewBondForm()
	if request.method == 'POST':
		form = NewBondForm(request.POST)

		if form.is_valid():
			issuer = form.cleaned_data["issuer"]
			name = form.cleaned_data["name"]
			bond_yield = form.cleaned_data["bond_yield"]

			b = Bond(issuer=issuer, name=name, bond_yield=bond_yield)
			b.save()

			return redirect('../')

		else:
			pass
	
	template = 'financial_system/new_bond.html'
	context['form'] = form

	return render(request, template, context)

def stock_transaction(request, id):
	data = Stock.objects.get(id=id)
	context = dict()
	form = StockTransactionForm()
	if request.method == 'POST':
		form = StockTransactionForm(request.POST)

		if form.is_valid():
			transaction_type = form.cleaned_data["transaction_type"]
			shares = form.cleaned_data["shares"]
			agent = form.cleaned_data["agent"]
			user = form.cleaned_data["user"]
			stock = data
			price = data.close_price

			st = StockTransaction(price=price, transaction_type=transaction_type, shares=shares, agent=agent, user=user, stock=stock)
			st.save()

			return redirect('../')

		else:
			pass
	
	template = 'financial_system/stock_transaction.html'
	context['form'] = form

	return render(request, template, context)

def property_transaction(request, id):
	data = Property.objects.get(id=id)
	context = dict()
	form = PropertyTransactionForm()
	if request.method == 'POST':
		form = PropertyTransactionForm(request.POST)

		if form.is_valid():
			transaction_type = TransactionTypes.objects.get(id=1)
			agent = form.cleaned_data["agent"]
			user = form.cleaned_data["user"]
			property = data
			price = data.transaction_price

			pt = PropertyTransaction(price=price, transaction_type=transaction_type, agent=agent, user=user, property=property)
			pt.save()

			return redirect('../')

		else:
			pass
	
	template = 'financial_system/property_transaction.html'
	context['form'] = form

	return render(request, template, context)

def other_transaction(request, id):
	data = MiscProduct.objects.get(id=id)
	context = dict()
	form = OtherTransactionForm()
	if request.method == 'POST':
		form = OtherTransactionForm(request.POST)

		if form.is_valid():
			transaction_type = TransactionTypes.objects.get(id=1)
			user = form.cleaned_data["user"]
			amount = form.cleaned_data["amount"]
			product = data
			price = data.transaction_price

			ot = OtherTransaction(price=price, amount=amount, product=product, transaction_type=transaction_type, user=user)
			ot.save()

			return redirect('../')

		else:
			pass
	
	template = 'financial_system/other_transaction.html'
	context['form'] = form

	return render(request, template, context)

def listUsers(request):
	query_results = User.objects.all()
	user_list = UserChoiceField()

	context = {
		'query_results': query_results,
		'user_list': user_list,
	}

	return render(request, 'financial_system/new_property.html', context)

def listAgents(request):
	query_results = Agent.objects.all()
	agent_list = AgentChoiceField()

	context = {
		'query_results': query_results,
		'agent_list': agent_list,
	}

	return render(request, 'financial_system/new_property.html', context)

def new_misc_product(request):
	context = dict()
	form = NewMiscProductForm()
	if request.method == 'POST':
		form = NewMiscProductForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data["name"]
			product_type = form.cleaned_data["product_type"]
			transaction_price = form.cleaned_data["transaction_price"]
			description = form.cleaned_data["description"]
			agent = form.cleaned_data["agent"]

			mp = MiscProduct(name=name, product_type=product_type, transaction_price=transaction_price, description=description, agent=agent)
			mp.save()

			return redirect('../')

		else:
			pass
	
	template = 'financial_system/new_misc_product.html'
	context['form'] = form

	return render(request, template, context)

def user_transactions_form(request):
	template = 'financial_system/user_transactions_form.html'
	form = UserTransactionsForm()

	if request.method == 'POST':
		form = UserTransactionsForm(data = request.POST)
		if form.is_valid():
			return redirect('../')
		else:
			pass

	context = {
	'form':form
	}
	return render(request,template,context)

def list_user_transactions(request):
	template = 'financial_system/list_user_transactions.html'

	if request.method == 'POST':
		name = request.POST['name']
		date = request.POST['date']

		user = User.objects.get(name=name)

		stock_transactions = StockTransaction.objects.filter(user=user.id, date=date)
		property_transactions = PropertyTransaction.objects.filter(user=user.id, date=date)
		other_transactions = OtherTransaction.objects.filter(user=user.id, date=date)

		context={
			'stock_transactions':stock_transactions,
			'prop_transactions':property_transactions,
			'oth_transactions':other_transactions
		}

		return render(request, template, context)

def stock_date_form(request):
	template = 'financial_system/stock_date_form.html'
	form = StockDataOnDateForm()

	if request.method == 'POST':
		form = StockDataOnDateForm(data = request.POST)
		if form.is_valid():
			return redirect('../')
		else:
			pass

	context = {
	'form':form
	}
	return render(request,template,context)

def list_stocks_on_date(request):
	template = 'financial_system/list_stocks_on_date.html'

	if request.method == 'POST':
		name = request.POST['name']
		date = request.POST['date']
		
		stock_data = Stock.objects.filter(name=name, date=date)

		context={"stock_data":stock_data}

		return render(request, template, context)

def property_data_form(request):
	template = 'financial_system/property_data_form.html'
	form = PropertyDataForm()

	if request.method == 'POST':
		form = PropertyDataForm(data = request.POST)
		if form.is_valid():
			return redirect('../')
		else:
			pass

	context = {
	'form':form
	}
	return render(request,template,context)

def list_property_data(request):
	template = 'financial_system/list_property_data.html'

	if request.method == 'POST':
		address = request.POST['address']
		
		property = Property.objects.get(address=address)

		context={"property":property}

		return render(request, template, context)

def bond_data_form(request):
	template = 'financial_system/bond_data_form.html'
	form = BondDataForm()

	if request.method == 'POST':
		form = BondDataForm(data = request.POST)
		if form.is_valid():
			return redirect('../')
		else:
			pass

	context = {
	'form':form
	}
	return render(request,template,context)

def list_bond_data(request):
	template = 'financial_system/list_bond_data.html'

	if request.method == 'POST':
		name = request.POST['name']
		
		bond = Bond.objects.get(name=name)

		context={"bond":bond}

		return render(request, template, context)

def agent_assets_form(request):
	template = 'financial_system/agent_assets_form.html'
	form = AgentAssetsForm()

	if request.method == 'POST':
		form = AgentAssetsForm(data = request.POST)
		if form.is_valid():
			return redirect('../')
		else:
			pass

	context = {
	'form':form
	}
	return render(request,template,context)

def list_agent_assets(request):
	template = 'financial_system/list_agent_assets.html'

	if request.method == 'POST':
		name = request.POST['name']

		agent = Agent.objects.get(name=name)

		properties = Property.objects.filter(agent=agent.id)
		other = MiscProduct.objects.filter(agent=agent.id)

		context={"agent":agent, "properties":properties, "other":other}

		return render(request, template, context)

def loan_ratings_form(request):
	template = 'financial_system/loan_ratings_form.html'
	form = LoanRatingsForm()

	if request.method == 'POST':
		form = LoanRatingsForm(data = request.POST)
		if form.is_valid():
			return redirect('../')
		else:
			pass

	context = {
	'form':form
	}
	return render(request,template,context)

def list_loan_ratings(request):
	template = 'financial_system/list_loan_ratings.html'

	if request.method == 'POST':
		name = request.POST['name']

		bank = Bank.objects.get(name=name)
		
		bonds = Bond.objects.filter(issuer=bank.id).order_by('bond_yield')

		context={"issuer":name, "bonds":bonds}

		return render(request, template, context)