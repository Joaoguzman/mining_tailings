def grow_rate(start, end, years):
    # print(type(start),type(end),type(years))
    # print(1/years)
    result= ((end/start)**(1/years)-1)*100
    print(start, end, years, result)

grow_rate(457,1111,10)
grow_rate(283,718,10)
grow_rate(174,393,10)