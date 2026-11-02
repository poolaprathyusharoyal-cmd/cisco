
names = ["Aachal", "Brahmaiah", "Darshan", "Pavitra", "Vijaylakshmi"]

print(names)

names.append("Danveer")       # Append: adds at last
print(names)

names.insert(3, "Renuksawmy")
print(names)

names.pop()                   # Removes last element
print(names)

names.remove("Renuksawmy")    # Removes specified element
print(names)

names.sort()                  # Sorts alphabetically
print(names)

names.reverse()               # Reverses the list
print(names)

print("Teams Players / total Players:", len(names))

names.extend(["Ajith", "Ranganath"])  # Adds multiple elements
print(names)

print("Teams Players / total Players:", len(names))
