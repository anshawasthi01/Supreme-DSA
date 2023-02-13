arr = [10,20,30,40]
sum = 80

for i in range(len(arr)):
    element1 = arr[i]
    for j in range(i+1, len(arr)):
        element2 = arr[j]
        for k in range(j+1, len(arr)):
            element3 = arr[k]

            if(element1 + element2 + element3 == sum):
                print(element1, "", element2,"",element3)
