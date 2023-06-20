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

	bool checkCyclicUsingBfs(int src, unordered_map<int,bool>& visited) {
		queue<int> q;
		unordered_map<int,int> parent;
		
		q.push(src);
		visited[src] = true;
		parent[src] = -1;

		while(!q.empty()) {
			int frontNode = q.front();
			q.pop();

			for(auto nbr: adjList[frontNode]) {
				if(!visited[nbr]) {
					q.push(nbr);
					visited[nbr] = true;
					parent[nbr]=frontNode;
				}
				if(visited[nbr] && nbr != parent[frontNode]) {
						//cycle present
						return true;
				}
			}
		}
		return false;
	}

	bool checkCyclicUsingDfs(int src, unordered_map<int,bool>& visited, int parent) {
		visited[src] = true;

		for(auto nbr: adjList[src]) {
			if(!visited[nbr]) {
				bool checkAageKaAns = checkCyclicUsingDfs(nbr, visited, src);
				if(checkAageKaAns == true)
					return true;
			}
			if(visited[nbr] && nbr != parent) {
				//cycle present
				return true;
			}
		}
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
	for(int i=0; i<n; i++) {
		if(!visited[i]) {
			 ans = g.checkCyclicUsingBfs(i,visited);
			if(ans == true)
				break;
		}
	}

	if(ans == true) 
		cout << "Cycle is Present" << endl;
	else
		cout << "Cycle Absent" << endl;


	// bool ansDfs = false;
	// unordered_map<int, bool> visitedDfs;
	// for(int i=0; i<n; i++) {
	// 	if(!visitedDfs[i]) {
	// 		 ansDfs = g.checkCyclicUsingDfs(i,visitedDfs, -1);
	// 		if(ansDfs == true)
	// 			break;
	// 	}
	// }

	// if(ansDfs == true) 
	// 	cout << "Cycle is Present" << endl;
	// else
	// 	cout << "Cycle Absent" << endl;

	return 0;
}