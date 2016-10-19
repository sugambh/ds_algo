def encode(s):
    result=""
    counter=1
    previous=s[0]
    i=1
    while(i<len(s)):
        current=s[i]
        if current!=previous:
            result=result+previous+str(counter)
            counter=1
        else:
            counter+=1
        previous=current
        i+=1
    result=result+previous+str(counter)
    return result

if __name__=="__main__":
    s="sssuruurtrrrrrrrrrrrrrrrrrrrrrrr"
    print encode(s)