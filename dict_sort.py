# Sample dictionary
sample_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}

# Sort the dictionary by keys in ascending order
sorted_dict_keys_asc = dict(sorted(sample_dict.items()))
print("Ascending order by keys:", sorted_dict_keys_asc)

# Sort the dictionary by keys in descending order
sorted_dict_keys_desc = dict(sorted(sample_dict.items(), reverse=True))
print("Descending order by keys:", sorted_dict_keys_desc)

# Sort the dictionary by values in ascending order
sorted_dict_values_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Ascending order by values:", sorted_dict_values_asc)

# Sort the dictionary by values in descending order
sorted_dict_values_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order by values:", sorted_dict_values_desc)
