import datetime
import time

lst_violence= ['Speeding','Reckless driving','Driving while intoxicated','Illegal lane changes','Failure to stop at red light','Underage','No license','Parking violation','Broken tail light']
fine_violence=[200,300,400,200,100,600,700,100,400]
def traffic_challan(c_name,c_cnic,no_plate):

    print("_"*30)

    challan_no = 0
    new_violence=[]
    counter=0
    new_fine=[]

    for violations in lst_violence:
        challan_no+=1
        counter+=1
        violation_tick=input('{:<30}:'.format(violations))
        if violation_tick=='y' or violation_tick=='Y':
            new_violence.append(violations)
            new_fine.append(fine_violence[counter-1])
        elif violation_tick!='y' or violation_tick!='Y':
            pass

    print("\n\n")
    print(u"\u25A0"*31)
    print("               E-challan slip")
    print("-"*45)
    now=datetime.datetime.now()
    now_date= now.strftime("%Y-%m-%d")
    time_date=now.strftime("%Y-%m-%d %H:%M")
    time_now=now.strftime("%H:%M")
    print('{:<30}:{}'.format("Time",time_now))
    print('{:<30}:{}'.format("Date", now_date))
    print('{:<30}:{}'.format("Name of civilian",civilian_name))
    print('{:<30}:{}'.format("CNIC #",civilian_cnic))
    print('{:<30}:{}'.format("Vehicle No Plate",civilian_plate))
    print('\n')
    print('{:<35}:{}'.format("Violation Type","Fine"))
    print("-" * 45)
    for x in range(len(new_violence)):
        print('{:<35}:{}'.format(new_violence[x],new_fine[x]))
    print('{:<35}:{}'.format("TOTAL FINE",sum(new_fine)))
    print("-" * 45)
    print('\n')






print('{:}'.format("E-challan slip"))
new_challan= input("Do you want to generate a new challan?")
while new_challan!="n":
    civilian_name=  input("Enter civilians name:     ")
    civilian_cnic=  input("Enter civilians CNIC:     ")
    civilian_plate= input("Enter civilians no plate: ")
    traffic_challan(civilian_name,civilian_cnic,civilian_plate)
    new_challan = input("Do you want to generate a new challan?")




