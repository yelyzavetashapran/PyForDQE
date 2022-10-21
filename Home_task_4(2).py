from collections import defaultdict
import random, string

# Task 1
def dicts():
    output = []  # Dicts list
    for dict_num in range(random.randint(2, 10)):  # Dicts counter
        dictionary = {}
        for elem_num in range(random.randint(3, 7)):  # Elements counter
            dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)  # Key(random letter), value(random number from 0 to 100)
        output.append(dictionary)  # Append every dict to dicts list
    return output

# Task 2
output = defaultdict(lambda: float('-inf'))  # To ensure you always get the
                                             # correct output to include if there are negative
                                             # values use float('-inf') as the default value
dicts = dicts()

def two():
    for cntr in range(0, len(dicts)):  # Create a counter for later adding of '_number_of_dictionary' for the same keys
        for k, v in dicts[cntr].items():
            if output[k] != float('-inf'):  # Check whether value exists previously
                if output[k] > v:  # If stored value > actual than we do nothing
                    continue
                del output[k]  # Delete key with max value
                k = f'{k}_{cntr + 1}'  # Create new key with adding '_number_of_dictionary'

            output[k] = max(output[k], v)  # Add key: value
    return output

def three():
    for i in range(0, len(dicts)):
        print(f'Dict {i+1}:  {dicts[i]}')  # Just for better display

three()
print('')
print('New dictionary:', dict(two()))