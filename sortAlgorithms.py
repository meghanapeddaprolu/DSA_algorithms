##bubblesort:[1,2,3,4,5,6]
#problem-1 leaderboard rankings
def leaderBoard(arr):
    n=len(arr)
    rank_changes=0
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j] :
                rank_changes+=1
    print(rank_changes)
    for i in range(n-1):#[5]
        for j in range(n-i-1):#[4]
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(leaderBoard([500,100,400,200,300]))

#problem-2 sort student grades
def studentGrades(arr):
    n=len(arr)
    swaps=0
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps+=1
    print("no of swaps : ",swaps)
    return arr
print(studentGrades([200,4000,500,700,67,43,1]))

# insertion sort:
# exam scores:[1,3,14,2,6,7]
def examScores(arr):
    n=len(arr)
    shift=0
    for i in range(1,n):#[3,14,2,6,7]
        key=arr[i]#[14]
        j=i-1#i=1 =>1-1=1 i.e j=0
        while j>=0 and arr[j]>key:#i.e arr[0]>arr[1]=> 3,14,yes
                arr[j+1]=arr[j] #i.e arr[0+1]=arr[1] [3,2,14,6,7]
                
                j -= 1 #1-1 =0
                shift+=1
        arr[j+1]=key #arr[0+1]=1
    return arr  ,shift
print(examScores([300,150,400,250,100]
)) 
        
# [150,300,400,250,100]
# [150,300,250,400,100]
# [150,250,300,400,100]
# [150,250,300,100,400]
# [150,250,100,300,400]
# [150,100,250,300,400]
# [100,150,250,300,400]  

#selction sort:
def sel_sort(nums):
    n=len(nums)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
print(sel_sort([7,8,9,6,5,4,3,2,12]))    


#selection sort:153 [4,5,6,1,2,3]
def findMin(nums):
        n = len(nums)
        min_val = nums[0] # 4

        for i in range(n):
            if nums[i] < min_val: #4<4 ,no |5<4 ,no|6<4 ,no|1<4,yes|
                min_val = nums[i] 

        return min_val
print(findMin([4,5,6,1,2,3]))

#414:
def thirdMax( nums):
        
        n=len(nums)
        max_element=nums[n-1]
        for i in range(0,n):
            return max_element
print(thirdMax([2,1,2,3,1]))


# quick sort


#library book sorter
def library(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]#[1,3,5,7,8,4,3]
    
    left=[]
    right=[]
    
    for i in arr[1:]:
        if i<pivot:
            left.append(i)
        else :
            right.append(i)
            
    return library(left) + [pivot] + library(right)
            
arr=list(map(int, input("enter the library : ").split()))  
print(library(arr))

#cricket Scoreboard
def scoreboard(players):
    if len(players) <= 1:
        return players
    
    left=[]
    right=[]
    pivot=players[0]
    for i in players[1:]:
        if i[1]>pivot[1]:
            left.append(i)
        else:
            right.append(i)
    return scoreboard(left) + [pivot ]+scoreboard(right)
print(scoreboard(players=[("Rohit", 85),("Virat", 120),("Dhoni", 60),("Hardik", 95),("Rahul", 110)]))