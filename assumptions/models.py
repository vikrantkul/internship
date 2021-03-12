from django.db import models


# Create your models here.
class Assumptions(models.Model):
    No_of_years=models.IntegerField('No. of years',default=0,blank=True)
    No_of_working_hrs_per_day=models.IntegerField('No. of working hrs. per day',null=True,blank=True)
    Attendance_Time_hrs_perday=models.IntegerField('Attendance Time (hrs per day)',null=True,default=None)
    Working_minutes_per_day=models.IntegerField('Working minutes per day',null=True)
    No_of_working_days_per_month=models.IntegerField('No. of working days per month',null=True)
    Total_no_of_production_days_per_year=models.IntegerField('Total no of production days per year',null=True)
    No_of_shifts_per_day=models.IntegerField('No. of shifts per day',null=True)
    Exchange_rate=models.IntegerField(default=0,null=True) 
    def __str__(self):
        return str(self.id)


class Absenteeis_and_Defective(models.Model):
    Sewing=models.CharField(max_length=25,null=True)
    Cutting=models.CharField(max_length=25,null=True)
    Finishing=models.CharField(max_length=25,null=True)
    Cutting_Output_as_percentage_of_Sewing_Output=models.CharField(max_length=25,null=True)
    Finishing_Output_as_percentage_of_Sewing_Output=models.CharField(max_length=25,null=True)
    Extra_Sewing_Machines_Required=models.CharField(max_length=25,null=True)
    Cutting_Loss=models.CharField(max_length=25,null=True)
    Year1 = models.CharField(max_length=25, null=True, blank=True)
    Year2 = models.CharField(max_length=25, null=True, blank=True)
    Year3 = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.id)


class Cost_Assumptions(models.Model):
    a=models.CharField('Electricity cost per KW-Hr (INR.)',max_length=25,null=True,blank=True)
    b=models.CharField('Electricity requirement for light & fans (Kw-Hr per 1000 Sq Ft.)',max_length=250,null=True,blank=True)
    c=models.CharField('Water consumption per person per day (Lts.)',max_length=25,null=True,blank=True)
    d=models.CharField('Water Cost (INR. Per 1000 Lts.)',max_length=25,null=True,blank=True)
    e=models.CharField('Construction cost per sq ft. (INR.)',max_length=25,null=True,blank=True)
    f=models.CharField('Land Cost (INR per Acre)',max_length=25,null=True,blank=True)
    g=models.CharField('TotalBuilt up area area (Acres)',max_length=25,null=True,blank=True)
    h=models.CharField('Total land as % of covered area',max_length=25,null=True,blank=True)
    i=models.CharField('Land development cost (INR /Acre)',max_length=25,null=True,blank=True)
    j=models.CharField('Office area (Sq ft)',max_length=25,null=True,blank=True)
    k=models.CharField('Office development cost (INR./sq ft)',max_length=25,null=True,blank=True)
    l=models.CharField('False ceiling cost (INR. Per sq ft)',max_length=25,null=True,blank=True)
    m=models.CharField('Road construction cost (INR./sq ft.)',max_length=25,null=True,blank=True)
    n=models.CharField('ETP cost',max_length=25,null=True,blank=True)
    o=models.CharField('STP cost',max_length=25,null=True,blank=True)
    p=models.CharField('Generator cost (100KW)',max_length=25,null=True,blank=True)
    q=models.CharField('Generator cost (150KW)',max_length=25,null=True,blank=True)
    r=models.CharField('Electrical expenses (INR)',max_length=25,null=True,blank=True)
    s=models.CharField('Product Development Expenses (% of Total sales)',max_length=25,null=True,blank=True)
    t=models.CharField('Miscllaneous fixed asset per sewing machine (INR.)',max_length=25,default=1000,blank=True)
    u=models.CharField('Cutting',max_length=25,null=True,blank=True)
    v=models.CharField('Provision for contingency',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)


class Salary_growth_and_Incentives(models.Model):
    z=models.CharField('Salary Growth % year on year',max_length=25,null=True,blank=True)
    y=models.CharField('Wages Growth % year on year',max_length=25,null=True,blank=True)
    x=models.CharField('Incentive % per annum',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)


class Financial(models.Model):
    a=models.CharField('Ratio D/E',max_length=25,null=True,blank=True)
    b=models.CharField('Interest on Term Loan  Y1 & Y2',max_length=25,null=True,blank=True)
    c=models.CharField('Interest on Term Loan  Y3 onwards',max_length=25,null=True,blank=True)
    d=models.CharField('Interest on Working Capital Financing',max_length=25,null=True,blank=True)
    e=models.CharField('Interest Income on Cash Surplus',max_length=25,null=True,blank=True)
    f=models.CharField('Tax',max_length=25,null=True,blank=True)
    g=models.CharField('Business Commissions on Sales Value (For 1st 3 yrs)',max_length=25,null=True,blank=True)
    h=models.CharField('Duty Draw Backs',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)


class Depreciation_Schedule_For_Balance_Sheet_Straight_Line(models.Model):
    a=models.CharField('Factory Building ',max_length=25,null=True,blank=True)
    b=models.CharField('Plant & Machinery',max_length=25,null=True,blank=True)
    c=models.CharField('IT',max_length=25,null=True,blank=True)
    d=models.CharField('Misc Fixed Assets',max_length=25,null=True,blank=True)
    e=models.CharField('Amortisation of Pre Operative Expenses',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)


class Clearing_and_Forwarding_Exports(models.Model):
    a=models.CharField('For Exports',max_length=25,null=True,blank=True)
    b=models.CharField('Average pieces per container',max_length=25,null=True,blank=True)
    c=models.CharField('Port Handling charges (INR. per container) - all incl',max_length=25,null=True,blank=True)
    d=models.CharField('Transportation (in INR./ container)',max_length=25,null=True,blank=True)
    e=models.CharField('Material Handling @',max_length=25,null=True,blank=True)
    f=models.CharField('Duty - Manual Machines',max_length=25,null=True,blank=True)
    g=models.CharField('Duty - Electronic machines',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)