from python_bst import *
import os,sys,random

def preorderTravese(preorderlist,node):
    if node is None:
        return
    nodevalue(preorderlist,node)
    preorderTravese(preorderlist,node.left)
    preorderTravese(preorderlist,node.right)
    

def nodevalue(preorderlist,node):
        preorderlist.append(node.key)
        
def allAncestors(root,node):
    ancestorsList = list()
    while node is not None and node.parent is not None:
        ancestorsList.append(node.parent)
        node = node.parent
    return ancestorsList
    
def findLeastCommonParent(root,node1Ancestors,node2Ancestors):
    if type(node1Ancestors) is list and type(node2Ancestors) is list:
        for node1ancestoritem in node1Ancestors:
            for node2ancestoritem in node2Ancestors:
                if node1ancestoritem.key == node2ancestoritem.key:
                    return node1ancestoritem
    else:
        return root

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
            leastCommonParent = findLeastCommonParent(tree.root,node1Ancestors,node2Ancestors)
            
            print 'least common parent ' + str(leastCommonParent.key)
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