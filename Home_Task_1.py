# part_1
import random

lis = random.sample(range(0, 1001), 100)  # Create a list with function 'random.sample'
                                          # which generate 100 random numbers from 0 to 1000
                                          # 1001 - an integer number specifying
                                          # at which position to stop in 'range' (not included).
# part_2
for i in range(len(lis)):  # 'i' will stand for index of element
    for j in range(i + 1, len(lis)):  # 'j' will stand for index of the following element
        if lis[i] > lis[j]:  # Compare remaining elements of list 'lis' with lis[i] element
                             # (compare every element with others)
           lis[i], lis[j] = lis[j], lis[i] # Rearranges elements (from min to max)
#print(lis)
# part_3
def average_lis():  # Create a function
    even = []       # Create an empty list for further count of even numbers
    odd = []        # Create an empty list for further count of odd numbers
    sum_even = 0    # Create a 'summator' for even numbers
    sum_odd = 0     # Create a 'summator' for odd numbers
    for i in lis:
        if (i % 2) == 0:  # Check whether the element of list is even number
            sum_even += i  # Sum of even numbers
            even.append(i)  # Append every even number to list 'even'
        if (i % 2) == 1:  # Check whether the element of list is odd number
            sum_odd += i  # Sum of odd numbers
            odd.append(i)  # Append every even number to list 'odd'
    avg_even = sum_even / len(even)  # Calculate the average of even numbers
    avg_odd = sum_odd / len(odd)  # Calculate the average of odd numbers
    return avg_even, avg_odd

print('Averages of even and odd numbers:', average_lis())