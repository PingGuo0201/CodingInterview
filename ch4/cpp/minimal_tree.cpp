/**
Author: Ping Guo
Email: pingg104@gmail.com
Problem statement: minimal tree (4.2)
  Given a sorted (increasing order) array with unique integer elements, write an
  algorithm to create a binary search tree with minimal height.
Complexity: TODO
*/
//include<>
using namespace std;

struct node
{ int num; node *l, *r;
  node (int x)
    {num = x; l = 0; r = 0;}

};
typedef node* link;

link BinaryTree(array, int start, int end)
{
  // reach to the bottom
  if(start > end) return NULL;

  // use middle element as the root
  int m = (start+end)/2;
  link root = new node(array[m]);

  root->l = BinaryTree(array, start, m-1);
  root->r = BianryTree(array, m+1, end);
  return root
}
