#include <iostream>
#include<vector>
#include<unordered_map>
#include<list>
#include<queue>
#include<stack>
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

	void topoSortDfs(int src, unordered_map<int, bool>& visited, stack<int>& ans) {
		
		visited[src] = true;

		for(auto neighbour: adjList[src]) {
			if(!visited[neighbour] ) {
				topoSortDfs(neighbour, visited, ans);
			}
		}
		//while returning, store the node in stack
		ans.push(src);
	}

	void topoSortBfs(int n, vector<int>& ans) {
		queue<int> q;
		unordered_map<int, int> indegree;

		//indegree calculate
		for(auto i: adjList ) {
			int src = i.first;
			for(auto nbr:i.second) {
				indegree[nbr]++;
			}
		}

		//put all nodes inside queue, which has indegree=0
		for(int i=0; i<n; i++) {
			if(indegree[i] == 0) {
				q.push(i);
			}
		}

		//bfs logic
		while(!q.empty()) {
			int fNode = q.front();
			q.pop();

			ans.push_back(fNode);
			//or we can do count++ for Cycle detection using bfs

			for(auto nbr: adjList[fNode]) {
				indegree[nbr]--;
				//check for zero again
				if(indegree[nbr] == 0) {
					q.push(nbr);
				}	
			}
			
		}
		
	}


};





int main() {

// // TOPOLOGICAL SORT Using DFS
	// Graph<int> g;
	// //n -> number of nodes in graph
	// int n = 8;
	// g.addEdge(0,1,1);
	// g.addEdge(1,2,1);
	// g.addEdge(2,3,1);
	// g.addEdge(3,4,1);
  // g.addEdge(3,5,1);
  // g.addEdge(4,6,1);
  // g.addEdge(5,6,1);
  // g.addEdge(6,7,1);

	// g.printAdjacencyList();
	// cout << endl;

//   unordered_map<int,bool> visited;
// 	stack<int> ans;
// 	for(int i=0; i<n; i++) {
// 		if(!visited[i] ){
// 			g.topoSortDfs(i,visited,ans);
// 		}
// 	}

// 	cout << "Top Sort: " << endl;
// 	while(!ans.empty()) {
// 		cout << ans.top();
// 		ans.pop();
// 	}


  // TOPOLOGICAL SORT Using DFS OR Kahn's Algorithm
	Graph<int> g;
	//n -> number of nodes in graph
	int n = 8;
	g.addEdge(2,4,1);
	g.addEdge(2,5,1);
	g.addEdge(4,6,1);
	g.addEdge(5,3,1);

	g.addEdge(3,7,1);
	g.addEdge(6,7,1);
	g.addEdge(7,0,1);
	g.addEdge(7,1,1);

	g.printAdjacencyList();
	cout << endl;


	vector<int> ans;
	//connected or disconnected 
	g.topoSortBfs(n, ans);

  // // To find Cycle Detection Using BFS use below only if else code 
  // if(ans.size() == n) {
	// cout << "It is a valid topo sort" << endl;
	// }
	// else {
	// 	cout << "Cycle Present or Invalid topo sort " << endl;
	// }

	cout << "Printing Topological Sort using BFS: " << endl;
	for(auto i: ans) {
		cout << i << ", ";
	}
  cout << endl;

	


	return 0;
}