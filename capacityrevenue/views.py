from django.shortcuts import render

# Create your views here.
def capacity_n_revenue(request):

    #these data are temparory just testing purpose, inplace of alphabets we need to replace them with data from database
    indexing = list(range(0,5))
    list0=['a','b','c','d','e']
    list1=['a','b','c','d','e']
    list2=['f','g','h','i','j']
    list3=['k','l','m','n','o']
    list4=['p','q','r','s','t']
    list5=['u','v','w','x','y']
    list6=['a','b','c','d','e']
    list7=['f','g','h','i','j']
    list8=['k','l','m','n','o']
    list9=['p','q','r','s','t']
    zipped_data0=zip(indexing,list0)
    zipped_data1=zip(indexing,list1)
    zipped_data2=zip(indexing,list2)
    zipped_data3=zip(indexing,list3)
    zipped_data4=zip(indexing,list4)
    zipped_data5=zip(indexing,list5)
    zipped_data6=zip(indexing,list6)
    zipped_data7=zip(indexing,list7)
    zipped_data8=zip(indexing,list8)
    zipped_data9=zip(indexing,list9)

    zipped_data10=zip(indexing,list0)
    zipped_data11=zip(indexing,list1)
    zipped_data12=zip(indexing,list2)
    zipped_data13=zip(indexing,list3)
    zipped_data14=zip(indexing,list4)
    zipped_data15=zip(indexing,list5)
    zipped_data16=zip(indexing,list6)
    zipped_data17=zip(indexing,list7)
    zipped_data18=zip(indexing,list8)
    zipped_data19=zip(indexing,list9)




    dict1={"indexing":indexing,"zipped_data0":zipped_data0,"zipped_data1":zipped_data1,"zipped_data2":zipped_data2,"zipped_data3":zipped_data3,"zipped_data4":zipped_data4,"zipped_data5":zipped_data5,"zipped_data6":zipped_data6,"zipped_data7":zipped_data7,"zipped_data8":zipped_data8,"zipped_data9":zipped_data9,"zipped_data10":zipped_data10,"zipped_data11":zipped_data11,"zipped_data12":zipped_data12,"zipped_data13":zipped_data13,"zipped_data14":zipped_data14,"zipped_data15":zipped_data15,"zipped_data16":zipped_data16,"zipped_data17":zipped_data17,"zipped_data18":zipped_data18,"zipped_data19":zipped_data19}


    return render(request,'capacitynrevenue.html',dict1)
