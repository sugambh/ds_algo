if __name__=="__main__":
    table=[0]*32
    a=[6,6,3,4,3,4,5]
    repetition = 2
    for num in a:
        i=1
        while (num):
            last_set_bit=num&1
            table[32-i]=table[32-i]+last_set_bit
            num=num>>1
            i+=1
    once=0
    for i in range(0,32):
        temp=table[32-i-1]%repetition
        once+=pow(2,i)*temp
    print once



