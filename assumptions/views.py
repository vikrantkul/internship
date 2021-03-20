from django.shortcuts import render
from django.http import HttpResponse
from .models import Assumptions,Absenteeis_and_Defective,Cost_Assumptions,Salary_growth_and_Incentives,Financial,Depreciation_Schedule_For_Balance_Sheet_Straight_Line,Clearing_and_Forwarding_Exports,Working_capital_ratios_and_assumtpions,Preliminary_and_Preoperative_expenses,Number_of_Lines,Assumptions_for_Production_Calculations,Machinery_Growth_Figures,No_of_Operators_per_line_as_per_Operation_Bulletin,Number_of_machines_planned,Productivity_Build_Up_for_New_Capactites_Year1,Productivity_Build_Up_for_New_Capactites_Year2,Productivity_Build_Up_for_New_Capactites_Year3,Summary_year1,Summary_year2,Summary_year3



def create_assumption(request):
    print('im activated')

    if request.method=='POST' and 'btnform1' in request.POST:
        No_of_years=request.POST.get('No_of_years')
        No_of_working_hrs_per_day=request.POST.get('No_of_working_hrs_per_day')
        Working_minutes_per_day = request.POST.get('Working_minutes_per_day')
        No_of_working_days_per_month = request.POST.get('No_of_working_days_per_month')
        Total_no_of_production_days_per_year = request.POST.get('Total_no_of_production_days_per_year')
        No_of_shifts_per_day = request.POST.get('No_of_shifts_per_day')
        Exchange_rate = request.POST.get('Exchange_rate')
        if bool(No_of_working_hrs_per_day) is True:
            Attendance_Time_hrs_perday=int(No_of_working_hrs_per_day)+1
        else:
            No_of_working_hrs_per_day=0
            Attendance_Time_hrs_perday=0
        if bool(No_of_years) is True:
            x=int(No_of_years)
            list1=list(range(1,x+1))
            context={'list1':list1}
        else:
            No_of_years=0
            list1=list(range(0,1))
            context={'list1':list1}

        a=Assumptions(No_of_years=No_of_years,No_of_working_hrs_per_day=No_of_working_hrs_per_day,Attendance_Time_hrs_perday=Attendance_Time_hrs_perday,
                      Working_minutes_per_day=Working_minutes_per_day,No_of_working_days_per_month=No_of_working_days_per_month,
                      Total_no_of_production_days_per_year=Total_no_of_production_days_per_year,No_of_shifts_per_day=No_of_shifts_per_day,
                      Exchange_rate=Exchange_rate)
        a.save()

        return render(request,'aform.html',context)

    if request.method=='POST' and 'btnform2' in request.POST:
        a=Absenteeis_and_Defective()
        a.Sewing=request.POST.get('Sewing')
        a.Cutting = request.POST.get('Cutting')
        a.Finishing = request.POST.get('Finishing')
        a.Cutting_Output_as_percentage_of_Sewing_Output = request.POST.get('Cutting_Output_as_percentage_of_Sewing_Output')
        a.Finishing_Output_as_percentage_of_Sewing_Output = request.POST.get('Finishing_Output_as_percentage_of_Sewing_Output')
        a.Extra_Sewing_Machines_Required = request.POST.get('Extra_Sewing_Machines_Required')
        a.Cutting_Loss=request.POST.get('Cutting_Loss')
        a.Year1=request.POST.get('Year1')
        a.Year2=request.POST.get('Year2')
        a.Year3=request.POST.get('Year3')

        a.save()

        return render(request,'aform.html')

    if request.method == 'POST' and 'btnform3' in request.POST:
        a=request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        e = request.POST.get('e')
        f = request.POST.get('f')
        g=request.POST.get('g')
        h=request.POST.get('h')
        i=request.POST.get('i')
        j=request.POST.get('j')
        k = request.POST.get('k')
        l = request.POST.get('l')
        m = request.POST.get('m')
        n = request.POST.get('n')
        o = request.POST.get('o')
        p = request.POST.get('p')
        q = request.POST.get('q')
        r = request.POST.get('r')
        s = request.POST.get('s')
        t = request.POST.get('t')
        u = request.POST.get('u')
        v = request.POST.get('v')

        ch=Cost_Assumptions(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,
                               k=k,l=l,m=m,n=n,o=o,p=p,q=q,r=r,s=s,t=t,u=u,v=v)

        ch.save()

        return render(request,'aform.html')

    if request.method == 'POST' and 'btnform4' in request.POST:
        z=request.POST.get('z')
        y = request.POST.get('y')
        x = request.POST.get('x')

        ch= Salary_growth_and_Incentives(z=z,y=y,x=x)

        ch.save()

        return render(request,'aform.html')



    if request.method=='POST' and 'btnform5' in request.POST:
        z=Financial()
        z.a=request.POST.get('a')
        z.b=request.POST.get('b')
        z.c=request.POST.get('c')
        z.d=request.POST.get('d')
        z.e=request.POST.get('e')
        z.f=request.POST.get('f')
        z.g=request.POST.get('g')
        z.h=request.POST.get('h')

        z.save()
        return render(request,'aform.html')


    if request.method=='POST' and 'btnform6' in request.POST:
        z=Depreciation_Schedule_For_Balance_Sheet_Straight_Line()
        z.a=request.POST.get('a')
        z.b=request.POST.get('b')
        z.c=request.POST.get('c')
        z.d=request.POST.get('d')
        z.e=request.POST.get('e')

        z.save()
        return render(request,'aform.html')


    if request.method=='POST' and 'btnform7' in request.POST:
        z=Clearing_and_Forwarding_Exports()
        z.a=request.POST.get('a')
        z.b=request.POST.get('b')
        z.c=request.POST.get('c')
        z.d=request.POST.get('d')
        z.e=request.POST.get('e')
        z.f=request.POST.get('f')
        z.g=request.POST.get('g')

        z.save()
        return render(request,'aform.html')

    if request.method == 'POST' and 'btnform8' in request.POST:
        a=request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        e = request.POST.get('e')
        f = request.POST.get('f')
        g =request.POST.get('g')
        h=request.POST.get('h')
        i=request.POST.get('i')
        j=request.POST.get('j')
        k = request.POST.get('k')
        l = request.POST.get('l')
        m = request.POST.get('m')
        n = request.POST.get('n')
        o = request.POST.get('o')
        p = request.POST.get('p')
        q = request.POST.get('q')
        r = request.POST.get('r')
        z=Working_capital_ratios_and_assumtpions(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,
                               k=k,l=l,m=m,n=n,o=o,p=p,q=q,r=r)
        z.save()
        return render(request,'aform.html')

    if request.method=='POST' and 'btnform9' in request.POST:
        z=Preliminary_and_Preoperative_expenses()
        z.a=request.POST.get('a')
        z.b=request.POST.get('b')
        z.c=request.POST.get('c')
        z.d=request.POST.get('d')
        z.e=request.POST.get('e')
        z.f=request.POST.get('f')

        z.save()
        return render(request,'aform.html')

    if request.method=='POST' and 'btnform10' in request.POST:
        z=Number_of_Lines()
        z.a=request.POST.get('Year1')
        z.b=request.POST.get('Year2')
        z.c=request.POST.get('Year3')
        z.d=request.POST.get('Year4')
        z.e=request.POST.get('Year5')

        z.save()
        return render(request,'aform.html')

    if request.method=='POST' and 'btnform11' in request.POST:
        z=Assumptions_for_Production_Calculations()
        z.a=request.POST.get('Year1')
        z.b=request.POST.get('Year2')
        z.c=request.POST.get('Year3')
        z.d=request.POST.get('Year4')
        z.e=request.POST.get('Year5')

        z.save()
        return render(request,'aform.html')

    if request.method=='POST' and 'btnform12' in request.POST:
        z=Machinery_Growth_Figures()
        z.a=request.POST.get('Year1')
        z.b=request.POST.get('Year2')
        z.c=request.POST.get('Year3')
        z.d=request.POST.get('Year4')
        z.e=request.POST.get('Year5')

        z.save()
        return render(request,'aform.html')

    if request.method=='POST' and 'btnform13' in request.POST:
        z=No_of_Operators_per_line_as_per_Operation_Bulletin()
        z.a=request.POST.get('a')
        z.b=request.POST.get('b')
        z.c=request.POST.get('c')
        z.d=request.POST.get('d')


        z.save()
        return render(request,'aform.html')


    if request.method == 'POST' and 'btnform14' in request.POST:
        a=request.POST.get('1Year1')
        b = request.POST.get('1Year2')
        c = request.POST.get('1Year3')
        d = request.POST.get('1Year4')
        e = request.POST.get('1Year5')
        f = request.POST.get('2Year1')
        g =request.POST.get('2Year2')
        h=request.POST.get('2Year3')
        i=request.POST.get('2Year4')
        j=request.POST.get('2Year5')
        k = request.POST.get('3Year1')
        l = request.POST.get('3Year2')
        m = request.POST.get('3Year3')
        n = request.POST.get('3Year4')
        o = request.POST.get('3Year5')
        ch=Number_of_machines_planned(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,
                               k=k,l=l,m=m,n=n,o=o)
        ch.save()
        return render(request,'aform.html')

    if request.method == 'POST' and 'btnform15' in request.POST:
        print('hello')
        ch = Productivity_Build_Up_for_New_Capactites_Year1()
        ch.a=request.POST.get('a1')
        ch.b = request.POST.get('b1')
        ch.c = request.POST.get('c1')
        ch.d = request.POST.get('d1')
        ch.e = request.POST.get('e1')
        ch.f = request.POST.get('f1')
        ch.g =request.POST.get('g1')
        ch.h=request.POST.get('h1')
        ch.i=request.POST.get('i1')
        ch.j=request.POST.get('j1')
        ch.k = request.POST.get('k1')
        ch.l = request.POST.get('l1')
        ch.m = request.POST.get('m1')
        ch.n = request.POST.get('n1')
        ch.o = request.POST.get('o1')
        ch.save()
        dh=Productivity_Build_Up_for_New_Capactites_Year2()
        dh.a=request.POST.get('a2')
        dh.b = request.POST.get('b2')
        dh.c = request.POST.get('c2')
        dh.d = request.POST.get('d2')
        dh.e = request.POST.get('e2')
        dh.f = request.POST.get('f2')
        dh.g =request.POST.get('g2')
        dh.h=request.POST.get('h2')
        dh.i=request.POST.get('i2')
        dh.j=request.POST.get('j2')
        dh.k = request.POST.get('k2')
        dh.l = request.POST.get('l2')
        dh.m = request.POST.get('m2')
        dh.n = request.POST.get('n2')
        dh.o = request.POST.get('o2')

        dh.save()
        eh=Productivity_Build_Up_for_New_Capactites_Year3()
        eh.a=request.POST.get('a3')
        eh.b = request.POST.get('b3')
        eh.c = request.POST.get('c3')
        eh.d = request.POST.get('d3')
        eh.e = request.POST.get('e3')
        eh.f = request.POST.get('f3')
        eh.g =request.POST.get('g3')
        eh.h=request.POST.get('h3')
        eh.i=request.POST.get('i3')
        eh.j=request.POST.get('j3')
        eh.k = request.POST.get('k3')
        eh.l = request.POST.get('l3')
        eh.m = request.POST.get('m3')
        eh.n = request.POST.get('n3')
        eh.o = request.POST.get('o3')

        eh.save()
        return render(request,'aform.html')
    if request.method == 'POST' and 'btnform16' in request.POST:
        z=Summary_year1()
        z.a= request.POST.get('a1')
        z.b= request.POST.get('b1')
        z.c= request.POST.get('c1')
        z.save()

        y=Summary_year2()
        y.a=request.POST.get('a2')
        y.b=request.POST.get('b2')
        y.c=request.POST.get('c2')
        y.save()

        x=Summary_year3()
        x.a=request.POST.get('a3')
        x.b=request.POST.get('b3')
        x.c=request.POST.get('c3')
        x.save()
    else:
        return render(request,'aform.html')