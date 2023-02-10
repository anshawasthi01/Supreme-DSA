# heart star pattern
size = int(input())

for i in range(int(size/2), size, 2):
    # print first spaces
    for j in range(1, size-i,2):
        print(" ",end='')

    # print first stars
    for j in range(1, i + 1):
        print("*",end='')

    # print second spaces
    for j in range(1, size-i+1):
        print(" ",end='')

    # print second stars
    for j in range(1, i + 1):
        print("*",end='')
    print()

    # lower part
    # inverted pyramid
for i in range(size,-1,-1):
    for j in range(size-i):
        print(" ",end='')
    
    for j in range(1, i * 2):
        print("*",end='')
 
    print()





# #include <iostream>
# using namespace std;

# int main() {
#   // heart star pattern
#   int size;
#   cin>>size;

#   for (int i = size / 2; i < size; i += 2) {
#     // print first spaces
#     for (int j = 1; j < size - i; j += 2) {
#       cout << " ";
#     }
#     // print first stars
#     for (int j = 1; j < i + 1; j++) {
#       cout << "*";
#     }
#     // print second spaces
#     for (int j = 1; j < size - i + 1; j++) {
#       cout << " ";
#     }
#     // print second stars
#     for (int j = 1; j < i + 1; j++) {
#       cout << "*";
#     }
#     cout << "\n";
#   }
#   // lower part
#   // inverted pyramid
#   for (int i = size; i > 0; i--) {
#     for (int j = 0; j < size - i; j++) {
#       cout << " ";
#     }
#     for (int j = 1; j < i * 2; j++) {
#       cout << "*";
#     }
#     cout << "\n";
#   }
#   return 0;
# }