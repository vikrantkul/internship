from django.contrib import admin
from .models import Assumptions,Absenteeis_and_Defective,Cost_Assumptions,Salary_growth_and_Incentives,Financial,Depreciation_Schedule_For_Balance_Sheet_Straight_Line,Clearing_and_Forwarding_Exports
# class AssumptionsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ('self.slug',)}

admin.site.register(Assumptions)
admin.site.register(Absenteeis_and_Defective)
admin.site.register(Cost_Assumptions)
admin.site.register(Salary_growth_and_Incentives)
admin.site.register(Financial)
admin.site.register(Depreciation_Schedule_For_Balance_Sheet_Straight_Line)
admin.site.register(Clearing_and_Forwarding_Exports)


