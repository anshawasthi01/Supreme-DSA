#include <iostream>
#include<unordered_map>
using namespace std;

int main() {
  // creation
  unordered_map<string, int> m;

  // insertion
  pair<string, int> p = make_pair("Scorpio", 9);
  m.insert(p);
  pair<string, int> p2("alto", 2);
  m.insert(p2);

  m["fortuner"] = 10; 

  // access
  cout << m.at("alto") << endl;
  cout << m.at("Scorpio") << endl;
  cout << m["fortuner"] << endl;

  //search
  cout << m.count("Innova") << endl;
  if(m.find("fortuner") != m.end()){
    cout << "Fortuner Found" << endl;
  }
  else{
    cout << " Fortuner not found" << endl;
  }

  cout << m.size() << endl;
  cout << m["hammer"] << endl; // if not found in not in map then create entry and initialize with 0
  cout <<m.size() << endl;

  cout << "printing all entries: " << endl << endl;

  for(auto i: m){
    cout << i.first << "->" << i.second << endl;
  }


  // //Count Frequency
  // string str = "thfdsiuejkfsdiuesd"
  // unordered_map<char, int> freq;

  // for(int i=0; i<str.length(); i++){
  //   char ch = str[i];
  //   freq[ch]++;
  // }

  // for(auto i: freq){
  //   cout << i.first << " " << i.second << endl;
  // }
  return 0;
}


// bool checkCircular(Node* head){
//   unordered_map<node*, bool> vis;
//   Node* temp = head;

//   while(temp!=NULL){
//     if(vis.find(temp) != vis.end()){
//       vis[temp] = temp;
//     }
//     else{
//       return true;
//     }
//     temp = temp -> next;
//   }
//   return false;
// }