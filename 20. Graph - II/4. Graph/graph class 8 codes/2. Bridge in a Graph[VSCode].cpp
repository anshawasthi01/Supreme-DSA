#include <iostream>
#include<unordered_map>
#include<list>
#include<queue>
#include<stack>
#include<algorithm>
#include<set>
#include<limits.h>
using namespace std;


class graph {
    public:
    unordered_map<int, list<int> > adjList;

    void addEdge(int u, int v, bool direction) {
        //direction = 1 -> undirected graph
        //direction => 0 -> directed graph;
        adjList[u].push_back(v);
        if(direction == 1) {
            adjList[v].push_back(u);
        }
    }

    void findBridges(int src, int parent, int& timer, vector<int>& tin, vector<int>& low, unordered_map<int,bool> vis) {

        vis[src] = true;
        tin[src] = timer;
        low[src] = timer;
        timer++;

        for(auto nbr: adjList[src]) {
            if(nbr == parent)
                continue;
            if(!vis[nbr]) {
                //dfs call
                findBridges(nbr, src, timer, tin, low, vis);
                //low update
                low[src] = min(low[src], low[nbr]);
                //check for bridge
                if(low[nbr] > low[src]) {
                    cout << nbr<<"--"<<src <<" is a bridge" << endl;
                }
            }
            else{
                //node is visited and not a parent
                //low update
                low[src] = min(low[src], low[nbr]);
            }
        }
    }
};

int main() {
    graph g;

    g.addEdge(0,1,1);
    g.addEdge(1,2,1);
    g.addEdge(2,0,1);
    g.addEdge(1,6,1);
    g.addEdge(3,1,1);
    g.addEdge(1,4,1);
    g.addEdge(3,5,1);
    g.addEdge(4,5,1);

    int n = 7;
    int timer = 0;
    vector<int> tin(n);
    vector<int> low(n);
    unordered_map<int,bool> vis;
    g.findBridges(0, -1,timer, tin, low, vis);

    return 0;
}
