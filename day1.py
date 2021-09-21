# to calculate simple intrest

principle,rate,time=map(float,input("enter principle rate time").split())

simple_intrest=principle*rate*time/100
print("simple intrest is {}".format(simple_intrest))