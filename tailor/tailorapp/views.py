from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Size
from .forms import CustomerForm, SizeForm

def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            request.session['customer_id'] = customer.id  # Store customer ID in session
            request.session['suit_count'] = customer.number_of_suits
            request.session['current_suit'] = 1  # Start suit entry from 1
            
            return redirect('enter_size')  # Redirect to enter first suit size
    else:
        form = CustomerForm()

    return render(request, 'customer_form.html', {'form': form})

def enter_size(request):
    customer_id = request.session.get('customer_id')
    suit_count = request.session.get('suit_count', 0)
    current_suit = request.session.get('current_suit', 1)

    if not customer_id:
        return redirect('create_customer')

    customer = get_object_or_404(Customer, id=customer_id)

    # Get the last entered size for autofill
    last_size = Size.objects.filter(customer=customer).order_by('-id').first()
    
    if request.method == "POST":
        form = SizeForm(request.POST, instance=last_size)  # Pre-fill with last entry
        if form.is_valid():
            size = form.save(commit=False)
            size.customer = customer
            size.save()

            if current_suit < suit_count:
                request.session['current_suit'] += 1  # Move to next suit
                return redirect('enter_size')
            else:
                del request.session['customer_id']
                del request.session['suit_count']
                del request.session['current_suit']
                return redirect('success_page')  # Redirect after final submission
    else:
        form = SizeForm(instance=last_size)  # Pre-fill with last suit details

    return render(request, 'size_form.html', {
        'form': form,
        'current_suit': current_suit,
        'total_suits': suit_count,
    })




"""
class CustomerView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer.html'
    success_url ='size'
 
class SizeView(CreateView):
    model = Size
    form_class = SizeForm
    template_name = 'size.html'
    success_url =reverse_lazy('billing')
 
    
def billing_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    
    # Get or create a billing record for the customer
    billing, created = Billing.objects.get_or_create(customer=customer)

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        billing.payment_method = payment_method
        billing.save()
        return render(request, "billing_success.html", {"billing": billing})  # Redirect to success page

    return render(request, "billing_detail.html", {"billing": billing, "customer": customer})   """