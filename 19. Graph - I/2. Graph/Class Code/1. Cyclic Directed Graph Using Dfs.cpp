#include <iostream>
#include<vector>
#include<unordered_map>
#include<list>
#include<queue>
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
				cout <<neighbour<<", ";
			}
			cout << endl;
		}
	}

	bool checkCyclicDirectedGraphUsingDfs(int src, unordered_map<int,bool>& visited,
unordered_map<int,bool> dfsVisited) {

		visited[src] = true;
		dfsVisited[src] = true;

		for(auto nbr: adjList[src]) {
			if(!visited[nbr]) {
				bool aageKaAnswer = checkCyclicDirectedGraphUsingDfs(nbr, visited, dfsVisited);
				if(aageKaAnswer == true)
					return true;
			}
			if(visited[nbr] == true && dfsVisited[nbr] == true) {
				return true;
			}
		}
		//yaha hi galti hoti h 
		dfsVisited[src] = false;
		return false;
	}
};

int main() {

	Graph<int> g;
	//n -> number of nodes in graph
	int n = 5;
	g.addEdge(0,1,1);
	g.addEdge(1,2,1);
	g.addEdge(2,3,1);
	g.addEdge(3,4,1);
	g.addEdge(4,0,1);

	g.printAdjacencyList();
	cout << endl;

	bool ans = false;
	unordered_map<int, bool> visited;
	unordered_map<int, bool> dfsVisited;
	for(int i=0; i<n; i++) {
		if(!visited[i] ) {
			ans = g.checkCyclicDirectedGraphUsingDfs(i,visited,dfsVisited);
			if(ans == true)
				break;
		}
	}

	if(ans == true) 
		cout << "Cycle is Present" << endl;
	else
		cout << "Cycle Absent" << endl;

	return 0;
}