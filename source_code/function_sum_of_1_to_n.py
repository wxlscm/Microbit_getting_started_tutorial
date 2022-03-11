def sum_1_to_n(n):
    i=1
    sum_f=0
    while True:
        sum_f+=i
        i+=1
        if i>n:
            break
    return sum_f


n = int(input("Please enter a positive integer n: "))
sum=sum_1_to_n(n)
print('Sum of 1 to {} is {}'.format(n,sum))



