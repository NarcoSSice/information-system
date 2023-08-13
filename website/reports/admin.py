from django.contrib import admin

from .models import *
list_models = [One, Two, Three, Four, FiveOne, FiveTwoOne, FiveTwoTwo, FiveThreeOne,
               FiveThreeTwo, FiveFourOne, FiveFourTwo, Six, Seven, AllReports, Category]

for model in list_models:
    admin.site.register(model)
