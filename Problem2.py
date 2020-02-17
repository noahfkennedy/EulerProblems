# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

i = 1
j = 0
temp = 0
sum = 0
while (i < 4000000):
    if (i % 2 == 0):
        sum += i
    temp = i
    i += j
    j = temp
print(sum)

# Answer matches stackoverflow: https://stackoverflow.com/questions/18927767/project-euler-2-in-java