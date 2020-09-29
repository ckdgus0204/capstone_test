from django.contrib import admin
from accounts.models import User
from ergate.models import Autoset, Simulation, Stockitem, PredictRate


admin.site.register(Autoset) # 기본 ModelAdmin으로 등록
admin.site.register(Simulation) # 기본 ModelAdmin으로 등록
admin.site.register(Stockitem) # 기본 ModelAdmin으로 등록
admin.site.register(PredictRate) # 기본 ModelAdmin으로 등록



