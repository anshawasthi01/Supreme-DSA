// https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

Node *merge(Node*a, Node*b){
    if(!a) return b;
    if(!b) return a;

    Node *ans=0;
    if(a ->data <b-> data) {
        ans = a;
        a-> bottom = merge(a->bottom, b);
    } 
    else{
        ans= b;
        b->bottom= merge(a, b->bottom);
    }   
    return ans;
}


Node *flatten(Node *root)
{
    if(!root) return 0;
    Node *mergedLL= merge(root, flatten(root->next));
    return mergedLL;
}