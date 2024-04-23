from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            repair_category = form.cleaned_data['repair_category']
            repair_category_disp = dict(form.fields['repair_category'].choices)[repair_category]
            form_inst = form.save(commit=False)
            form_inst.repair_category = repair_category_disp
            form_inst.save()
            messages.success(request, 'Заказ успешно создан.')
            return redirect('home')
    else:
        form = OrderForm(user=request.user) \
            if not isinstance(request.user, AnonymousUser) \
            else OrderForm()
    return render(request, 'order_form.html', {'form': form})


