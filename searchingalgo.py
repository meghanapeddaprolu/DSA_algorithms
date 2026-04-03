# linear search
def linear_srch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return 'not found'
 
        
arr=[1,2,3,4,5,6,7,8]
print(linear_srch(arr,2))
 
 
# Hospital Patient Lookup      
def hospital(patients,key):
    for i in range(len(patients)):
        if patients[i]["name"]==key:
            print("Patient found!")
            print("Name    :", patients[i]["name"])
            print("Age     :", patients[i]["age"])
            print("Disease :", patients[i]["disease"])
            print("Position: Record #", i+1)
            return
    print("no patient found")
patients=[
{"name": "Arjun","age": 34, "disease": "Fever"},
{"name": "Meena","age": 22, "disease": "Flu"},
{"name": "Ravi", "age": 45, "disease": "Diabetes"},
{"name": "Sneha","age": 29, "disease": "Migraine"}
]
hospital(patients,"Meena")

#super market discount finder
def superMarket(products):
    print("Products eligible for 10% discount:")
    for i in range(len(products)):
        name = products[i][0]
        price = products[i][1]
        if price > 500:
            discount_price = price - (0.10 * price)
            print(f"- {name} : ₹{price} → ₹{discount_price}")
products=[
("Rice 5kg", 450), ("Olive Oil", 850), ("Cornflakes", 380),
("Almonds 500g", 650), ("Detergent", 520), ("Bread", 60)
]
superMarket(products)

#binary search:
def binary_srch(arr,key):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if key==arr[mid]:
            return mid
        elif key<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=[2,3,4,5,6,7]
print(binary_srch(arr,6))

# Flight Ticket Availability:
def flight_tickets(available_seats,preferred_seat):
    low=0
    high=len(available_seats)-1 #  9 #3
    comparisons=0
    while low<=high:
        mid=(low+high)//2  #4 
        comparisons+=1
        if preferred_seat==available_seats[mid]: 
            print(f"Seat {preferred_seat} is available!")
            print("Position in list :", mid + 1)
            print("Comparisons made :", comparisons)
            return
        elif preferred_seat<available_seats[mid]: #9=2 < 4 2<3
            high=mid-1 #4-1=3
        else:
            low=mid+1
    print("no seats available")
available_seats=[2, 5, 9, 14, 21, 28, 35, 42, 48, 55]
print(flight_tickets(available_seats,2))
        
        
def pharmacy_shop(medicines,key):
    low=0
    high=len(medicines)-1
    comparisions=0
    
    while low<=high:
        mid=(low+high)//2
        comparisions+=1
        
        if key==medicines[mid]:
            print(f"Medicine found : {key}")
            print(f"shelf position : {mid+1}")
            print(f"comparisions : {comparisions}")
            return 
        elif key< medicines[mid]:
            high=mid-1
        else:
            low=mid+1
    print(f"{key} is not found")
    print(f"comparisons : {comparisions}")
medicines=[
"Aspirin", "Cetirizine", "Dolo650", "Ibuprofen",
"Metformin", "Omeprazole", "Paracetamol", "Ranitidine"
]
pharmacy_shop(medicines,"Amoxicillin")
        