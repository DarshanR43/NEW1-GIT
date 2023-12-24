def list1(Experiment_name,Research_field,country,Year):
    L1=dict("Physics")
    L2=dict("Astronomy")
    L3=dict("Biology")
        
    if (Research_field == "Physics"):
        L1= L1.update(P,Experiment_name) 
        P += 1
    elif(Research_field == "Astronomy"):
        L1= L1.update(A,Experiment_name)
        A += 1
    else:
        L1= L1.update(B,Experiment_name)
        B += 1
    
    return L1,L2,L3,A,B,P    
     
# def list2(Experiment_name,Research_field,country,Year):
    

def list2(Experiment_name,Research_field,country,Year):
    # l1 = []
    l2 = dict()
    if (country == Country):
        n1 += 1
        l2 = l2.update(Experiment_name)
    else:
        None  
      
    return l2   
        
P = 1
A = 1
B = 1
n = 1
n1 = 0
N = int(input(""))
for i in range (0,N):
    input_str = input("")
    input_list = input_str.split(',')
    Experiment_name = (input_list[0])
    Research_field = (input_list[1])
    country = input_list[3].split(":")
    Year = int((input_list[4]))
    
    if (Research_field == "Physics"):
        P += 1
    elif(Research_field == "Astronomy"):
        A += 1
    else:
        B += 1
    # return A,B,P

    print(Experiment_name)
    list1(Experiment_name,Research_field,country,Year)
    list2(Experiment_name,Research_field,country,Year) 
    # list3(Experiment_name,Research_field,country,Year)
Country =  input()
print(L1)
print(L2)
print(L3)
print(l2)
if(A > (B&P)):
    print("Most Collaborative Field: Astronomy")
elif(B > (A&P)):
    print("Most Collaborative Field: Biology")
else:
    print("Most Collaborative Field: Physics")
