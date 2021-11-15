from django.shortcuts import redirect, render
from .models import Bill
from .forms import BillForm
from .utils import Render

def index(request):
    bill = Bill.objects.all().order_by('-date')
    return render(request, 'index.html', {'bill': bill})

def detailView(request, id):
    bill_det = Bill.objects.get(id = id)
    bill = Bill.objects.filter(id =id)
    return render(request, 'bill.html', {'bill': bill, 'bill_det': bill_det})

def formView(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BillForm()
    return render(request, 'bill-form.html', {'form':form})

def deleteView(request,id):
    bill = Bill.objects.get(id = id)
    bill.delete()
    return redirect('index')

# Html to pdf view
def pdf(request, id):
    bill = Bill.objects.filter(id =id)
    return Render.render('bill.html', {'bill':bill})