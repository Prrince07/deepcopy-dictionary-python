import copy

original = {'user': {'name': 'Prince', 'age': 18}}
copy_dict = copy.deepcopy(original)

print("Original:", original)
print("Copied:", copy_dict)
