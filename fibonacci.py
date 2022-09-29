# Task 1: Generalised Fibonacci

# Write your code here:

p = 1
q = 1
fibo = [1,1]
ele = p*fibo[1]+q*fibo[0]
fibo.append(ele)
ele1 = p*fibo[2]+q*fibo[1]
fibo.append(ele1)
print(fibo)