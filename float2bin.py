def dec2bin(x):
    x=x-int(x)
    x_bin=[] #empty list
    while x:
        x*=2
        if x>=1:
            x_bin.append(str(1))
        else:
            x_bin.append(str(0))
        x=x-int(x)
    x_bins="".join(x_bin)
    return x_bins

def int2bin(x):
    x_int=int(x)
    bin_list=[]
    while x_int:
        x_reminder=str(x_int%2)
        bin_list.append(x_reminder)
        x_int=x_int//2
    return "".join(bin_list[::-1])

def num2bin(x):
    integers=int2bin(x)
    decimals=dec2bin(x)
    #print(intergers,decimals)
    return integers+'.'+decimals

if __name__=="__main__":
    x=float(input('Please enter a float number: '))
    x_bin=num2bin(x)
    print('The binary number of {} is {}'.format(x,x_bin))
