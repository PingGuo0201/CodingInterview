'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x. If x is
contained within the list, the values of x only need to be after the elements
less than x (see below). The partition element x can appear anywhere in the
right partition; it does not need to appear between the left and right
partition.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
Reference: "Algorithms in C++, part 1-4" by Robert Sedgewick, 3.3 linked list
Complexity: TODO
Usage: partition_2 <int>
'''
# include<stdio.h>
# include<stdlib.h>


typedef struct node {
  int val;
  struct node* next;
}
node;

void concat(node* l1, node* l2) {
  node* temp;
  if (l1 == NULL) {
    l1 = l2;
  }
  else if (l2 == NULL) {
    l1 = l1;
  }
  else {
    temp = l1;
    while (temp -> next != NULL) {temp = temp -> next;}
    temp -> next = bigger;
  }
}

int x = 0;

void rearrange(node* head, int n) {
  // traverse through the linked list and insert numbers to two new linked lists
  // and combine the new linked lists in the end
  node* smaller, bigger;
  smaller = (node*)malloc(sizeof(node));
  bigger = smaller;
  smaller -> next = NULL;

  while (head != NULL){
    x = head -> val;
    if (x < n) {
      smaller -> val = x;
      smaller -> next = (node*)malloc(sizeof(node));
      smaller = smaller -> next;
    }

    else {
      bigger -> val = x;
      bigger -> next = (node*)malloc(sizeof(node));
      bigger = bigger -> next;
    }
    head = head -> next
  }
  smaller -> next = NULL;
  bigger -> next = NULL;
  concat(smaller, bigger)

}
