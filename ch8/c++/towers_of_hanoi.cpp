'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    In the classic problem of the Towers of Hanoi, you have 3 towers and N
disks of different sizes which can slide onto any tower. The puzzle starts with
disks sorted in ascending order of size from top to bottom (i.e. each disk sits
on top of an even larger one). You have the following constraints:

(1) Only one disk can be move at a time.
(2) A disk is slid off the top one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.

Write a program to move the disks from the first tower to the last using
stacks.

Complexity: TODO
Usage: TODO
'''
#include <iostream>

using namespace std;

template <class Item>
class STACK {
  private:
    Item *s:int N;
  public:
    STACK (int maxN) {
      s = new Item(maxN);
    }
    int empty() const {
      return N == 0;
    }
    void push(Item item) {
      s[N++] = item;
    }
    Item pop() {
      return s[--N];
    }
    void moveplateto(STACK t) {
      t.push(tower1.pop());
    }
    void movedisk(N, STACK origin, STACK buffer, STACK destination) {
      movedisk(N-1, origin, destination, buffer);
      origin.moveplateto(destination);
      movedisk(N-1, buffer, origin, destination);

    }
};

void main(int argc, char *argv[]) {
  if (argc != 2) {
    cout << "Usage: " << argv[0] << "number of disks!" <<endl;
  }

  int n = argv[1];
  STACK<int> tower(N)
  for (int i = n; i > 0; --i) {
    tower.push(i);
  }

  tower.movedisk(n, tower, STACK tower2, STACK tower3)
}
