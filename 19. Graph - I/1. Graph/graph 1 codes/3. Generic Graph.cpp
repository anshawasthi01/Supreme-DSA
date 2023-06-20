// Generic Graph

#include <iostream>
#include<vector>
#include<unordered_map>
#include<list>
using namespace std;
template <typename T>

class Graph {
public:
 unordered_map<T, list<T > > adjList;   

 void addEdge(T u, T v, bool direction) {
   //direction = 0 -> undirected graph
   //direction = 1 -> directed graph
   //create an edge from u to v
   adjList[u].push_back(v);
   if(direction == 0)
   {
     //undirected edge
     //create an edge from v to u
     adjList[v].push_back(u);
   }
 }

 void printAdjacencyList() {
   for(auto node: adjList) {
     cout << node.first << "-> " ;
     for(auto neighbour: node.second) {
       cout << neighbour << ", ";
     }
     cout << endl;
   }
 }
};

int main() {
  Graph<char> g;
  g.addEdge('a','b', 0);
  g.addEdge('b', 'c', 0);
  g.addEdge('a', 'c', 0);
  g.printAdjacencyList();

  return 0;
}