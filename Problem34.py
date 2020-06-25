# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def to_list(n):
    num_list = list(str(n))
    return (num_list)


def fact(num):
    fact = 1
    if num < 0:
        print("No factorial")
        return 0
    elif num == 0:
        return fact
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact


def curious(n):
    n_list = to_list(n)
    n_fact = 0
    for n in n_list:
        n_fact += fact(int(n))
    return n_fact


curious_numbers = 0
for i in range(3, 9999999):
    curious_num = curious(i)
    if (curious_num == i):
        curious_numbers += i

print("The sum of all curious numbers is: " + str(curious_numbers))
print("9 factorial equals 362880, a six digit number.")
print("Therefore, past a certain number of digits, an increased order of magnitude is a larger change than adding 362880")
print("This point occurs around 87digits. 9! * 7 = 2,540,160 which is less than 9,999,999. Therefore, we only need to search until 7 digits.")
