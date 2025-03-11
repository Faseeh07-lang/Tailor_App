from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    number_of_suits = models.IntegerField()

    def __str__(self):
        return self.name

class Size(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sizes")
    color = models.CharField(max_length=100, default= "black")
    type = models.CharField(max_length=100, default="washinwear")
    waist = models.IntegerField(default=23)
    sleeve_length = models.IntegerField(default=24)
    neck = models.IntegerField(default=12)
    shoulder_length = models.IntegerField(default=13)
    chest = models.IntegerField(default=23)
    suit_length = models.IntegerField(default=12)
    sleeve_width = models.IntegerField(default=34)
    shalwar_length = models.IntegerField(default=33)

    def __str__(self):
        return f"{self.customer.name} - {self.color} Suit"

    
class Order_details(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Condition_choices=[
        ("pending","Pending"),
        ("in_progress","In_Progress"),
        ("completed","Completed")
    ]
    given_date=models.DateField()
    delivery_date=models.DateField()
    status=models.CharField(choices=Condition_choices,max_length=200)
  
class Billing(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bills")
    suit_price = models.IntegerField(default=2000)  # Fixed price per suit
    total_amount = models.IntegerField(blank=True, null=True)  # Auto-calculated before saving

    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("cancelled", "Cancelled"),
    ]
    payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, max_length=20, default="pending")

    PAYMENT_METHOD_CHOICES = [
        ("cash", "Cash"),
        ("credit_card", "Credit Card"),
        ("bank_transfer", "Bank Transfer"),
        ("mobile_wallet", "Mobile Wallet"),
    ]
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=20, blank=True, null=True)
    
    transaction_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Get the number_of_suits from the related customer
        self.total_amount = self.customer.number_of_suits * self.suit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill for {self.customer.name} - {self.total_amount} ({self.payment_status})"
 