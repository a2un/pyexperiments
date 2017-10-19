from python_bst import *
import os,sys,random
import numpy as np

def preorderTravese(preorderlist,node):
    if node is None:
        return
    nodevalue(preorderlist,node)
    preorderTravese(preorderlist,node.left)
    preorderTravese(preorderlist,node.right)
    
def createMatrix(root):
    height = getHeight(0,root);
    _grid_shape = (height,height)
    adjmatrix = np.zeros(_grid_shape);
    print 'height' + str(height)
    return adjmatrix

def createList(adjList,node):
    if node.left is not None:
        adjList.append((node.key,node.left.key))
        adjList.append(createList(adjList,node.left))
    if node.right is not None:
        adjList.append((node.key,node.right.key))
        adjList.append(createList(adjList,node.right))
    return adjList

def getHeight(height,node):
    height1=0;
    height2=0;
    if node.left is not None:
        height1 = getHeight(height,node.left)
    if node.right is not None:
        height2 = getHeight(height,node.right)
    height += height1+1 if (height1>=height2) else height2+1;
    return height;

def nodevalue(preorderlist,node):
        preorderlist.append(node.key)
        
def allAncestors(root,node):
    ancestorsList = list()
    while node is not None and node.parent is not None:
        ancestorsList.append(node.parent)
        node = node.parent
    return ancestorsList
    
    
def findLeastCommonParentineff(root,node1Ancestors,node2Ancestors):
    if type(node1Ancestors) is list and type(node2Ancestors) is list:
        for node1ancestoritem in node1Ancestors:
            for node2ancestoritem in node2Ancestors:
                if node1ancestoritem.key == node2ancestoritem.key:
                    return node1ancestoritem
    else:
        return root

def findLeastCommonParent(root,node1,node2):
    #adjmatrix = createMatrix(root)
    adjList = list()
    adjList = createList(adjList,root)
    print adjList
    
def findin(tree):
    if tree is not None:
        preorderlist=list()
        print 'root:' + str(tree.root.key)
        nodekey1 = raw_input('enter the two nodes to check: ')
        nodekey2 = raw_input()
        node1 = tree.find(int(nodekey1))
        node2 = tree.find(int(nodekey2))
        if(node1 is not None and node2 is not None):
            print 'all is well'
            node1Ancestors = allAncestors(tree.root,node1)
            node2Ancestors = allAncestors(tree.root,node2)
            leastCommonParentineff = findLeastCommonParentineff(tree.root,node1Ancestors,node2Ancestors)
            findLeastCommonParent(tree.root,node1,node2)
            print 'least common parent ' + str(leastCommonParentineff.key)
        else:
           print 'invalid nodekey1 or nodekey2 value'
    else:
        print 'please input valid tree'

def runTest(args=None,BSTtype=BST):
    tree = BSTtype()
    with open('./bst_input.txt') as f:
        args = f.read().split()

    tree = test(args)
    findin(tree)

if __name__ == '__main__': runTest()