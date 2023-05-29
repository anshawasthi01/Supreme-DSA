m = {}

# insertion
m["Scorpio"] = 9
m["alto"] = 2
m["fortuner"] = 10

# access
print(m["alto"])
print(m["Scorpio"])
print(m["fortuner"])

# search
print(m.get("Innova", 0))
if "fortuner" in m:
    print("Fortuner Found")
else:
    print("Fortuner not found")

print(len(m))
print(m.get("hammer", 0))
print(len(m))

print("printing all entries:\n")
for key, value in m.items():
    print(key, "->", value)


# Count Frequency
str = "thfdsiuejkfsdiuesd"
freq = {}

for ch in str:
    freq[ch] = freq.get(ch, 0) + 1

for key, value in freq.items():
    print(key, value)

# Check Circular or Loop in a LinkedList
def checkCircular(head):
    visited = {}
    temp = head

    while temp is not None:
        if temp in visited:
            visited[temp] = temp
        else:
            return True
        temp = temp.next

    return False

