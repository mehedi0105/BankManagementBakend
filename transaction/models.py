from django.db import models
from accounts import models as Accounts
# Create your models here.
class OtherBank(models.Model):
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name

# Save Transaction History

class TransactionHistory(models.Model):
    account = models.ForeignKey(Accounts.UserAccount, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    paid_in = models.DecimalField(max_digits=12,decimal_places=2)
    paid_out = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return self.account.user.first_name