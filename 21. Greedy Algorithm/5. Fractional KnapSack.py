val = [60, 100, 120]
wt = [10, 20, 30]
n = 3
capacity = 50

data = [(val[i], wt[i]) for i in range(n)]

# bool cmp(pair<int,int> a, pair<int,int> b) {
#   double ratio1 = ((1.0)*a.first) / a.second;
#   double ratio2 = ((1.0)*b.first) / b.second;
#   return ratio1 > ratio2;
# }
data.sort(key=lambda x: float(x[0]) / x[1], reverse=True)
totalValue = 0
# check eac items k entire itm lelu ya frraction lu

for i in range(n):
    itemValue, itemWeight = data[i]
    
    # entire inclusioon wala case
    if itemWeight <= capacity:

        # add kardo value ko
        totalValue += itemValue

        # update krdo capacity ko
        capacity -= itemWeight
    else:

        # fraction include krdo
        # update value
        ratio = float(itemValue) / itemWeight
        valueToAdd = ratio * capacity
        totalValue += valueToAdd
        # udpate capacity
        capacity = 0

print("Answer is:", totalValue)
