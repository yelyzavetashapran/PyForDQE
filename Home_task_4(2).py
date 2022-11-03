from collections import defaultdict
import random, string


# Task 1
def create_list_of_dicts():
    output_1 = []  # Dicts list
    for dict_num in range(random.randint(2, 10)):  # Dicts counter
        dictionary = {}
        for elem_num in range(random.randint(3, 7)):  # Elements counter
            dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)  # Key(random letter), value(random number from 0 to 100)
        output_1.append(dictionary)  # Append every dict to dicts list
    return output_1


dicts = create_list_of_dicts()


# Task 2
def new_collective_dict_with_n_suffix(n):
    output_2 = defaultdict(lambda: float('-inf'))  # To ensure you always get the
    # correct output to include if there are negative
    # values use float('-inf') as the default value
    for cntr in range(0, len(n)):  # Create a counter for later adding of '_number_of_dictionary' for the same keys
        for k, v in n[cntr].items():
            if output_2[k] != float('-inf'):  # Check whether value exists previously
                if output_2[k] > v:  # If stored value > actual than we do nothing
                    continue
                del output_2[k]  # Delete key with max value
                k = f'{k}_{cntr + 1}'  # Create new key with adding '_number_of_dictionary'

            output_2[k] = max(output_2[k], v)  # Add key: value
    return output_2


new_dict = dict(new_collective_dict_with_n_suffix(dicts))


def better_displaying(n):
    for i in range(0, len(n)):
        print(f'Dict {i+1}:  {n[i]}')  # Just for better display


better_displaying(dicts)
print('')
print('New dictionary:', new_dict)