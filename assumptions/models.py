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

class Working_capital_ratios_and_assumtpions(models.Model):
    a=models.CharField('Working Capital Ratio(Owner)',max_length=25,null=True,blank=True)
    b=models.CharField('Working Capital Ratio(Bank)',max_length=25,null=True,blank=True)
    c=models.CharField('Inv. Raw Material (at Raw material Cost) Month(Owner)',max_length=25,null=True,blank=True)
    d=models.CharField('Inv. Raw Material (at Raw material Cost) Month(Bank)',max_length=25,null=True,blank=True)
    e=models.CharField('Work In Process(at Raw material Cost) Month(owner)',max_length=25,null=True,blank=True)
    f=models.CharField('Work In Process(at Raw material Cost) Month](Bank)',max_length=25,null=True,blank=True)
    g=models.CharField('Finished Goods (at Variable/Sourcing Cost) Month(Owner)',max_length=25,null=True,blank=True)
    h=models.CharField('Finished Goods (at Variable/Sourcing Cost) Month(Bank)',max_length=25,null=True,blank=True)
    i=models.CharField('Finished Goods In Transit + Buyers Credit(at Cost of Prod) Month(Owner)',max_length=25,null=True,blank=True)
    j=models.CharField('Finished Goods In Transit + Buyers Credit(at Cost of Prod) Month(Bank)',max_length=25,null=True,blank=True)
    k=models.CharField('Spare Parts ( Month)(owner)',max_length=25,null=True,blank=True)
    l=models.CharField('Spare Parts ( Month)(Bank)',max_length=25,null=True,blank=True)
    m = models.CharField('Creditors (at Raw material cost) Month(owner)', max_length=25, null=True, blank=True)
    n = models.CharField('Creditors (at Raw material cost) Month(Bank)', max_length=25, null=True, blank=True)
    o = models.CharField('Debtors (at cost of Finished goods) Month(owner)', max_length=25, null=True, blank=True)
    p= models.CharField('Debtors (at cost of Finished goods) Month(Bank)', max_length=25, null=True, blank=True)
    q = models.CharField('Indirect Expenses(owner)', max_length=25, null=True, blank=True)
    r = models.CharField('Indirect Expenses(Bank)', max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.id)

class Preliminary_and_Preoperative_expenses(models.Model):
    a=models.CharField('Hiring Costs',max_length=25,null=True,blank=True)
    b=models.CharField('Relocation for Key Staff',max_length=25,null=True,blank=True)
    c=models.CharField('Salaries',max_length=25,null=True,blank=True)
    d=models.CharField('Overheads',max_length=25,null=True,blank=True)
    e=models.CharField('Cost of raw material during Training & Trial production',max_length=25,null=True,blank=True)
    f=models.CharField('Consulting Fees and Technology Fee for Garment Unit',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)

class Number_of_Lines(models.Model):
    a=models.CharField('Hi Fashion(Year1)',max_length=25,null=True,blank=True)
    b=models.CharField('Hi Fashion(Year2)',max_length=25,null=True,blank=True)
    c=models.CharField('Hi Fashion(Year3)',max_length=25,null=True,blank=True)
    d=models.CharField('Hi Fashion(Year4)',max_length=25,null=True,blank=True)
    e=models.CharField('Hi Fashion(Year5)',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)

class Assumptions_for_Production_Calculations(models.Model):
    a=models.CharField('Area per sewing machine (sq ft.)(Year1)',max_length=25,null=True,blank=True)
    b=models.CharField('Area per sewing machine (sq ft.)(Year2)',max_length=25,null=True,blank=True)
    c=models.CharField('Area per sewing machine (sq ft.)(Year3)',max_length=25,null=True,blank=True)
    d=models.CharField('Area per sewing machine (sq ft.)(Year4)',max_length=25,null=True,blank=True)
    e=models.CharField('Area per sewing machine (sq ft.)(Year5)',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)

class Machinery_Growth_Figures(models.Model):
    a=models.CharField('Cummulative Machines(Year1)',max_length=25,null=True,blank=True)
    b=models.CharField('Cummulative Machines(Year2)',max_length=25,null=True,blank=True)
    c=models.CharField('Cummulative Machines(Year3)',max_length=25,null=True,blank=True)
    d=models.CharField('Cummulative Machines(Year4)',max_length=25,null=True,blank=True)
    e=models.CharField('Cummulative Machines(Year5)',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)

class No_of_Operators_per_line_as_per_Operation_Bulletin(models.Model):
    a=models.CharField('Hi Fashion(no. of machines)',max_length=25,null=True,blank=True)
    b=models.CharField('Sampling(no. of machines)',max_length=25,null=True,blank=True)
    c=models.CharField('Training(no. of machines)',max_length=25,null=True,blank=True)
    d=models.CharField('Style variation summary(no. of machines)',max_length=25,null=True,blank=True)
    def __str__(self):
        return str(self.id)

class Number_of_machines_planned(models.Model):
    a = models.CharField('Year1', max_length=25, null=True, blank=True)
    b = models.CharField('Year2', max_length=25, null=True, blank=True)
    c = models.CharField('Year3', max_length=25, null=True, blank=True)
    d = models.CharField('Year4', max_length=25, null=True, blank=True)
    e = models.CharField('Year5', max_length=25, null=True, blank=True)
    f = models.CharField('total(Year1)', max_length=25, null=True, blank=True)
    g = models.CharField('total(Year2)', max_length=25, null=True, blank=True)
    h = models.CharField('total(Year3)', max_length=25, null=True, blank=True)
    i = models.CharField('total(Year4)', max_length=25, null=True, blank=True)
    j = models.CharField('total(Year5)', max_length=25, null=True, blank=True)
    k = models.CharField('New added capacity as % of total capacity (Year1)', max_length=25, null=True, blank=True)
    l = models.CharField('New added capacity as % of total capacity (Year2)', max_length=25, null=True, blank=True)
    m = models.CharField('New added capacity as % of total capacity (Year3)', max_length=25, null=True, blank=True)
    n = models.CharField('New added capacity as % of total capacity (Year4)', max_length=25, null=True, blank=True)
    o = models.CharField('New added capacity as % of total capacity (Year5)', max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.id)

class Productivity_Build_Up_for_New_Capactites_Year1(models.Model):
    a = models.CharField('Utilization Build-Up(Q1)', max_length=25, null=True, blank=True)
    b = models.CharField('Utilization Build-Up(Q2)', max_length=25, null=True, blank=True)
    c = models.CharField('Utilization Build-Up(Q3)', max_length=25, null=True, blank=True)
    d = models.CharField('Utilization Build-Up(Q4)', max_length=25, null=True, blank=True)
    e = models.CharField('Utilization Build-Up(AnnualAvg)', max_length=25, null=True, blank=True)
    f = models.CharField('Efficiency Build-Up(Q1)', max_length=25, null=True, blank=True)
    g = models.CharField('Efficiency Build-Up(Q2)', max_length=25, null=True, blank=True)
    h = models.CharField('Efficiency Build-Up(Q3)', max_length=25, null=True, blank=True)
    i = models.CharField('Efficiency Build-Up(Q4)', max_length=25, null=True, blank=True)
    j = models.CharField('Efficiency Build-Up(AnnualAvg)', max_length=25, null=True, blank=True)
    k = models.CharField('Productivity Factor(Q1)', max_length=25, null=True, blank=True)
    l = models.CharField('Productivity Factor(Q2)', max_length=25, null=True, blank=True)
    m = models.CharField('Productivity Factor(Q3)', max_length=25, null=True, blank=True)
    n = models.CharField('Productivity Factor(Q4)', max_length=25, null=True, blank=True)
    o = models.CharField('Productivity Factor(AnnualAvg)', max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.id)
class Productivity_Build_Up_for_New_Capactites_Year2(models.Model):
    a = models.CharField('Utilization Build-Up(Q1)', max_length=25, null=True, blank=True)
    b = models.CharField('Utilization Build-Up(Q2)', max_length=25, null=True, blank=True)
    c = models.CharField('Utilization Build-Up(Q3)', max_length=25, null=True, blank=True)
    d = models.CharField('Utilization Build-Up(Q4)', max_length=25, null=True, blank=True)
    e = models.CharField('Utilization Build-Up(AnnualAvg)', max_length=25, null=True, blank=True)
    f = models.CharField('Efficiency Build-Up(Q1)', max_length=25, null=True, blank=True)
    g = models.CharField('Efficiency Build-Up(Q2)', max_length=25, null=True, blank=True)
    h = models.CharField('Efficiency Build-Up(Q3)', max_length=25, null=True, blank=True)
    i = models.CharField('Efficiency Build-Up(Q4)', max_length=25, null=True, blank=True)
    j = models.CharField('Efficiency Build-Up(AnnualAvg)', max_length=25, null=True, blank=True)
    k = models.CharField('Productivity Factor(Q1)', max_length=25, null=True, blank=True)
    l = models.CharField('Productivity Factor(Q2)', max_length=25, null=True, blank=True)
    m = models.CharField('Productivity Factor(Q3)', max_length=25, null=True, blank=True)
    n = models.CharField('Productivity Factor(Q4)', max_length=25, null=True, blank=True)
    o = models.CharField('Productivity Factor(AnnualAvg)', max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.id)

class Productivity_Build_Up_for_New_Capactites_Year3(models.Model):
    a = models.CharField('Utilization Build-Up(Q1)', max_length=25, null=True, blank=True)
    b = models.CharField('Utilization Build-Up(Q2)', max_length=25, null=True, blank=True)
    c = models.CharField('Utilization Build-Up(Q3)', max_length=25, null=True, blank=True)
    d = models.CharField('Utilization Build-Up(Q4)', max_length=25, null=True, blank=True)
    e = models.CharField('Utilization Build-Up(AnnualAvg)', max_length=25, null=True, blank=True)
    f = models.CharField('Efficiency Build-Up(Q1)', max_length=25, null=True, blank=True)
    g = models.CharField('Efficiency Build-Up(Q2)', max_length=25, null=True, blank=True)
    h = models.CharField('Efficiency Build-Up(Q3)', max_length=25, null=True, blank=True)
    i = models.CharField('Efficiency Build-Up(Q4)', max_length=25, null=True, blank=True)
    j = models.CharField('Efficiency Build-Up(AnnualAvg)', max_length=25, null=True, blank=True)
    k = models.CharField('Productivity Factor(Q1)', max_length=25, null=True, blank=True)
    l = models.CharField('Productivity Factor(Q2)', max_length=25, null=True, blank=True)
    m = models.CharField('Productivity Factor(Q3)', max_length=25, null=True, blank=True)
    n = models.CharField('Productivity Factor(Q4)', max_length=25, null=True, blank=True)
    o = models.CharField('Productivity Factor(AnnualAvg)', max_length=25, null=True, blank=True)
    def __str__(self):
        return str(self.id)