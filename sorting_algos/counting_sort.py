# time complexity o(n+k)
if __name__=="__main__":
    a=[34,5,6,1,1,75,100,3,1]
    n=max(a)
    count_a=[0]*(n+1)
    for i in a:
        count_a[i]=count_a[i]+1
    sum=0
    for i in range(0,n+1):
        count_a[i]=sum+count_a[i]
        sum=count_a[i]
    output_array=[0]*len(a)
    for i in range(0,len(a)):
        output_array[count_a[a[i]]-1]=a[i]
        count_a[a[i]]-=1
    print output_array



