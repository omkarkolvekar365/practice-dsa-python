def product(num):
    n = len(num)
    output = [1]*n
    for i in range(1,n):
        output[i]=output[i-1]*num[i-1]
    suffix = 1
    for i in range(n-1,-1,-1):
        output[i]=output[i]*suffix
        suffix = suffix * num[i]
    return output
num=[1,2,3,4]
print(product(num))