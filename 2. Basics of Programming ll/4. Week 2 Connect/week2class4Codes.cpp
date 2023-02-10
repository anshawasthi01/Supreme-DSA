// Hello C++
#include <iostream>
using namespace std;
int main() {
  int age = 25;

  //(age>=18) ? cout << "Can Vote" : cout << "Cannot Vote";

  int num = 6;

  (num%2 == 0) ? cout << "Even" : cout << "Odd";

  return 0;
}

int n = 528;
for(;n!=0;n = n/10){
  int rem = n%10;
  cout << rem << " ";
}

# while num != 0:
#     rem = num % 10
#     print(rem)
#     num = num / 10