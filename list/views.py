from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def index(request):

	if request.method == "POST":
		form = ListForm(request.POST)

		if form.is_valid():
			form.save()
			item = form.cleaned_data.get('item')
			messages.success(request, item + ' has been added to the list')
			return render(request, 'index.html', {})
		else:
			messages.info(request, 'You entered something incorrectly, try again...')

	return render(request, 'index.html', {})

def list(request):
	all_items = List.objects.all()
	context = {'all_items': all_items}
	return render(request, 'list.html', context)

def about(request):
	return render(request, 'about.html', {})
	
def delete(request, pk):
	item = List.objects.get(pk=pk)
	item.delete()
	messages.success(request, 'This item has been deleted')
	return redirect('list')

def cross_off(request, pk):
	item = List.objects.get(pk=pk)
	item.completed = True
	item.save()
	messages.success(request, 'Item has been crossed off your list')
	return redirect('list')

def uncross(request, pk):
	item = List.objects.get(pk=pk)
	item.completed = False
	item.save()
	messages.success(request, 'Item has been uncrossed')
	return redirect('list')

def edit(request, pk):
	if request.method == "POST":
		item = List.objects.get(pk=pk)

		form = ListForm(request.POST, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, 'Item has been edited!')
			return redirect('list')

	else:
		item = List.objects.get(pk=pk)
		return render(request, 'edit.html', {'item': item})