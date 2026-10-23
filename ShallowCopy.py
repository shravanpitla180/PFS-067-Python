#ShallowCopy:-
# --> Shallow Copy is used to create a new object but does not recursively
# import copy
# original = [[10, 20], [30,40]]
# Copied = copy.copy(original)
# Copied.append([50])
# print("Original: ",original)
# print("Copied: ",Copied)


# import copy
# original = [[10, 20], [30,40]]
# Copied = copy.copy(original)
# Copied.append([50, 60])
# print("Original: ",original)
# print("Copied: ",Copied)

# import copy
# original = [[10, 20], [30,40]]
# Copied = copy.copy(original)
# Copied[0].append(98)
# print("Original: ",original)
# print("Copied: ",Copied)


# DeepCopy
# Original does not change
import copy
original = [[10, 20], [30,40]]
Copied = copy.deepcopy(original)
Copied[0].append(98)
print("Original: ",original)
print("Copied: ",Copied)
