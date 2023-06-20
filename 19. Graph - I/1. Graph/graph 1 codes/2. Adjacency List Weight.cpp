#include <iostream>
#include<vector>
#include<unordered_map>
#include<list>
using namespace std;

class Graph {
public:
 unordered_map<int, list<pair<int,int> > > adjList;

 void addEdge(int u, int v,int weight, bool direction) {
   //direction = 0 -> undirected graph
   //direction = 1 -> directed graph
   //create an edge from u to v
   adjList[u].push_back({v,weight});
   if(direction == 0)
   {
     //undirected edge
     //create an edge from v to u
     adjList[v].push_back({u,weight});
   }
 }

 void printAdjacencyList() {
   for(auto node: adjList) {
     cout << node.first << "-> " ;
     for(auto neighbour: node.second) {
       cout <<"("<<neighbour.first<<","<<neighbour.second<<"), ";
     }
     cout << endl;
   }
 }
};

int main() {
  Graph g;

  // directed input
  // g.addEdge(srcNode, destNode, weight, direction);
  g.addEdge(0,1,5,1);
  g.addEdge(1,2,8,1);
  g.addEdge(0,2,6,1);
  cout << endl;
  g.printAdjacencyList();


  return 0;
}