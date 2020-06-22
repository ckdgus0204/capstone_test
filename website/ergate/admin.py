from django.contrib import admin
from simulation.models import Stock_after, Stock_before
from accounts.models import User
# Register your models here.
admin.site.register(Stock_before)
admin.site.register(Stock_after)
admin.site.unregister(User)
admin.site.register(User)



