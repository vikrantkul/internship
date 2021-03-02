from django.contrib import admin
from .models import Assumptions,Absenteeis_and_Defective,Cost_Assumptions,Salary_growth_and_Incentives,Financial
# Register your models here.
# from .views import create_assumption
# class AssumptionsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ('self.slug',)}

admin.site.register(Assumptions)
admin.site.register(Absenteeis_and_Defective)
admin.site.register(Cost_Assumptions)
admin.site.register(Salary_growth_and_Incentives)
admin.site.register(Financial)


