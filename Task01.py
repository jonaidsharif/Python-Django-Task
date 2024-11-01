def sort_dict_keys(index_dict):
    # extract the keys of dictioary
    keys = list(index_dict.keys())
    

    # sort keys using bubble sort
    for i in range(len(keys) - 1):
        for j in range(len(keys) - 1 - i):
            if keys[j] > keys[j + 1]:
                # swap function if any wrong order
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    # create a new dictionary of sorted keys
    sorted_dict = {key: index_dict[key] for key in keys}
    
    return sorted_dict


index_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
sorted_dict = sort_dict_keys(index_dict)
print(sorted_dict)
