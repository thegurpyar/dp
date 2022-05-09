def bsearch(arr,n):
    l=0
    h=len(arr)-1
    
    while l<=h:
       

        mid=(l+h)//2

        
        if arr[mid]<n:
            l=mid+1
        elif arr[mid]>n:
            h=mid-1
        else:
            if mid-1<0:
                return mid
            elif arr[mid-1]!=n:
                return mid
            else:
                h=mid+1
    else:
        return -1


arr=[2,4,4,4,7,7,9]
n=[9,4,5,2]

for i in range(len(n)):
    print(bsearch(arr,n[i]))    
