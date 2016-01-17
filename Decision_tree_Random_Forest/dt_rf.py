# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:21:41 2015

@author: mythcard
"""

#from utils import *
import math,random
from collections import deque
from sys import argv
crap, var1, var2, var3 = argv

lstOfLst= []
lstOfLst_tst = []

class tree:
   def __init__(self, best_attribute = -1,best_threshold=-1,info_gain = -1,left_child = None,right_child = None,node_pos = None,distr=[]):
      self.best_attribute = best_attribute
      self.best_threshold = best_threshold
#      self.target = target
      self.info_gain = info_gain
      self.left_child =left_child
      self.right_child = right_child
      self.node_pos = node_pos
      self.distr = distr                 
      
      

def isNotEmpty(s):
    return bool(s and s.strip())
    
def all_same(items):
    return all(x == items[0] for x in items) 
    
def all_same1(items):
    for x in items:
        if x != items[0]:
            return False
    return True    
    
def distribution_examples(lstOfLst):
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
#    print "Columns:",cols
    cnt1 = []
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    target_lst1 = list(set(target_lst))

#    print "target_lst1:",target_lst1
    
    m = 0
    num_elem = len(target_lst1) - 1
    while m <= num_elem:
        n = 0
        cnt = 0
        while n <= rows:
#            print lstOfLst[n][cols], target_lst1[m]
            if lstOfLst[n][cols] == target_lst1[m]:
#                print lstOfLst[n][len(lstOfLst)-1], target_lst1[m]
                cnt = cnt + 1.0
            n = n + 1
#        print     cnt
        cnt1.append(float(cnt)/float(rows+1))
        m = m + 1
#    print cnt1    
    return cnt1        
        

## entropy calculation for root of any attribute for target column    
def entropy_root(lstOfLst):
      target_lst = []
      dict = {'0':0}
      rows = len(lstOfLst) - 1
      target_col = len(lstOfLst[0]) - 1
#      print "Rows in example set: ",rows+1," and index of target set: ", target_col
      n = 0
      entropy = 0
      while n <= rows:
          target_lst.append(lstOfLst[n][target_col])
          n = n +1
      target_lst1 = list(set(target_lst))    
#      print target_lst,target_lst1
      n1 = len(target_lst1)
      n2 = len(target_lst)
      while n1 > 0:
          k = n2
          cnt = 0
          while k > 0:
              if target_lst[k-1] == target_lst1[n1-1]:
                  cnt = cnt + 1
#                  print "Inside count",cnt,target_lst[k-1],target_lst1[n1-1]
              k = k - 1 
          dict.update({target_lst1[n1-1]:cnt})    
          n1 = n1 -1
#      print dict    
      n1 = len(target_lst1)
      while n1 > 0:
#          chr = str(dict[target_lst1[n1 - 1]])
#          print dict[target_lst1[n1 - 1]]
          p = float(dict[target_lst1[n1 - 1]])/float((rows + 1))
#          print p
          entropy = entropy + (p * (math.log(p)/math.log(2)))
          n1 = n1 - 1
      return (-1*entropy)
      
#information gain of an attribute based on threshold
def information_gain(lstOfLst,attr_ind,threshold):
    h_root_entropy = entropy_root(lstOfLst)
#    print "Root Entropy:",h_root_entropy
    rows = len(lstOfLst) - 1
    target_col = len(lstOfLst[0]) - 1
    dict1 = {'zero123':1}
    dict2 = {'zero123':1}
#    len1 = len(target_lst1)
    ent1 = 0
    ent2 = 0
    inform_gain = 0
    p = q = 0
    n = 0
    while n <= rows:
        var = float(lstOfLst[n][attr_ind])
        if var < threshold:
#            print "1"
            dict1.update({lstOfLst[n][target_col]:0}) 
        elif var >= threshold:
            dict2.update({lstOfLst[n][target_col]:0})
#            print "2"
        n = n +1        
    n = 0
    while n <= rows:
        var = float(lstOfLst[n][attr_ind])
        if var < threshold:
            cnt = dict1[lstOfLst[n][target_col]]
            cnt = cnt + 1
            dict1.update({lstOfLst[n][target_col]:cnt}) 
        elif var>= threshold:
            cnt = dict2[lstOfLst[n][target_col]]
            cnt = cnt + 1
            dict2.update({lstOfLst[n][target_col]:cnt})
        n = n +1  
    cnt3 = 0
    for key in dict1:
        if key != 'zero123':
            cnt3 = cnt3 + int(dict1[key])
#    print "cnt3 is",cnt3        
    for key in dict1:
        if key != 'zero123':
#            print "Two nec values:",dict1[key],cnt3
            p = (float(dict1[key])/float (cnt3))
            q = q + (p * (math.log(p)/math.log(2)))
            q = (-1 * q)
#            print "Q value:",q
            ent1 = ent1 + q
            q = 0
#            print "Ent1 is",ent1
    ent1 = ent1 * (float(cnt3)/(float(rows)+1))
    cnt3 = 0
    for key in dict2:
        if key != 'zero123':
            cnt3 = cnt3 + dict2[key]        
    p = q = 0
    for key in dict2:
        if key != 'zero123':
            p = (float(dict2[key])/float (cnt3))
            q = q + (p * (math.log(p)/math.log(2)))
            q = (-1 * q)
#            print "Q value:",q
            ent2 = ent2 + q
            q = 0
#            print "Ent1 is",ent2
    ent2 = ent2 * (float(cnt3)/(float(rows)+1))        
#    print "Left node: ",dict1
#    print "Right Node: ",dict2
#    print "Left node entropy: ",ent1
#    print "Right Node entropy: ",ent2
    inform_gain = h_root_entropy - (ent1 + ent2)
#    print "Information gain",inform_gain
    return inform_gain
    
### choose attribute function optimized
def choose_atr(lstOfLst,attr1):
    max_gain = best_attribute = best_threshold = -1
    rows = len(lstOfLst) - 1
#    print "Rows:",rows
#    k1 = 0
    for val in attr1:
#        print "Value:",val
        n = 0
#        print "Attribut1",attr1
        attribute_val = []
        while n <= rows:
            attribute_val.append(float(lstOfLst[n][val]))
            n = n + 1  
        attribute_val.sort()
#        print attribute_val
        l = attribute_val[0]
        m = attribute_val[len(attribute_val) - 1]
#        print "L and M: ",l , m
        k = 1.0
        while k <= 50.0:
           threshold = float(l) + (float(k) * (float(m) - float(l)))/float(51)
#           print "Big threshold is:",threshold
           gain = information_gain(lstOfLst,val,threshold)
           if gain > max_gain:
               max_gain = gain
               best_attribute = val
               best_threshold = threshold
           k = k + 1
#    print "K1 value is: ",k1       
    return best_attribute,best_threshold,max_gain

### choose attribute function randomized    
def choose_atr_random(lstOfLst,attr1):
    max_gain = best_attribute = best_threshold = -1
    rows = len(lstOfLst) - 1
#    print "Rows:",rows
#    k1 = 0
    val = random.choice(attr1)
    print "Chosen attribute randomly is:",val
    n = 0
#        print "Attribut1",attr1
    attribute_val = []
    while n <= rows:
        attribute_val.append(float(lstOfLst[n][val]))
        n = n + 1  
    attribute_val.sort()
#        print attribute_val
    l = attribute_val[0]
    m = attribute_val[len(attribute_val) - 1]
#        print "L and M: ",l , m
    k = 1.0
    while k <= 50.0:
        threshold = float(l) + (float(k) * (float(m) - float(l)))/float(51)
#           print "Big threshold is:",threshold
        gain = information_gain(lstOfLst,val,threshold)
        if gain > max_gain:
            max_gain = gain
            best_attribute = val
            best_threshold = threshold
        k = k + 1
#    print "K1 value is: ",k1       
    return best_attribute,best_threshold,max_gain    
    
        
def read_input(file_name):
    lstOfLst = []
    f = open(file_name, 'r')
    rd = f.readline()#    print rd
    while rd != '': 
        sep_lst =  rd.split(' ')
#    print sep_lst[-1]
        sep_lst[-1] = sep_lst[-1].strip()
        len1 = len(sep_lst) 
#    if not isNotEmpty(sep_lst[2]):
#        print "success"
        while len1 > 0:
            if not isNotEmpty(sep_lst[len1-1]):
                sep_lst.pop(len1-1)   
            len1 = len1 -1    
#    print sep_lst
        lstOfLst.append(sep_lst)
        rd = f.readline()
    f.close() 
    return lstOfLst



#attr1 = [0,1]



#threshold = 50
##
#attr_ind = 11
#
#inform_gain = information_gain(lstOfLst,attr_ind,threshold)
#print inform_gain
#print "List baba list:",lstOfLst
#best_attribute,best_threshold = choose_atr(lstOfLst,attr1)

#print "Best attribute and best threshold: ",best_attribute,best_threshold

## DTL learner optimized
def DTL(lstOfLst,attr1,default,node_pos1):
    target_lst = []
    examples_left = []
    examples_right = []
#    vector = []
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
#    if node_pos1 == 'L':
#        print "Rows gone left:",rows
#    else:    
#        print "Rows gone right:",rows
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    if not lstOfLst:
        node1 = tree(distr = default)
        return node1
    elif all_same1(target_lst):
        node2 = tree()
        node2.distr = distribution_examples(lstOfLst)
        return node2
    else:
        best_attribute,best_threshold,max_gain = choose_atr(lstOfLst,attr1)
#        print "Best attribute and threshold and gain:",best_attribute,best_threshold,max_gain
        t1 = tree(best_attribute,best_threshold,max_gain,node_pos = node_pos1)
        n = 0
        ### directing left and right child
        while n <=rows:
            if float(lstOfLst[n][best_attribute]) < best_threshold:
                examples_left.append(lstOfLst[n])
            n = n + 1
        n = 0    
        while n <=rows:
            if float(lstOfLst[n][best_attribute]) >= best_threshold:
                examples_right.append(lstOfLst[n])
            n = n + 1
        ### application of pruning  
        if(len(examples_left)<50):
            node3 = tree()
            node3.distr = distribution_examples(lstOfLst)
            return node3
        if(len(examples_right)<50): 
            node4 = tree()
            node4.distr = distribution_examples(lstOfLst)
            return node4
        if(len(examples_left)>=50 and len(examples_right)>=50):
            t1.left_child = DTL(examples_left,attr1,distribution_examples(lstOfLst),'L')
            t1.right_child = DTL(examples_right,attr1,distribution_examples(lstOfLst),'R')
            return t1
            
## DTL learner optimized
def DTL_Random(lstOfLst,attr1,default,node_pos1):
    target_lst = []
    examples_left = []
    examples_right = []
#    vector = []
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
#    if node_pos1 == 'L':
#        print "Rows gone left:",rows
#    else:    
#        print "Rows gone right:",rows
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    if not lstOfLst:
        node1 = tree(distr = default)
        return node1
    elif all_same1(target_lst):
        node2 = tree()
        node2.distr = distribution_examples(lstOfLst)
        return node2
    else:
        best_attribute,best_threshold,max_gain = choose_atr_random(lstOfLst,attr1)
#        print "Best attribute and threshold and gain:",best_attribute,best_threshold,max_gain
        t1 = tree(best_attribute,best_threshold,max_gain,node_pos = node_pos1)
        n = 0
        ### directing left and right child
        while n <=rows:
            if float(lstOfLst[n][best_attribute]) < best_threshold:
                examples_left.append(lstOfLst[n])
            n = n + 1
        n = 0    
        while n <=rows:
            if float(lstOfLst[n][best_attribute]) >= best_threshold:
                examples_right.append(lstOfLst[n])
            n = n + 1  
#        print "Examples towards right:",examples_right  
#        print "Examples towards left:",examples_left
        ### application of pruning    
        if(len(examples_left)<50):
            node3 = tree()
            node3.distr = distribution_examples(lstOfLst)
            return node3
        if(len(examples_right)<50): 
            node4 = tree()
            node4.distr = distribution_examples(lstOfLst)
            return node4
        if(len(examples_left)>=50 and len(examples_right)>=50):
            t1.left_child = DTL(examples_left,attr1,distribution_examples(lstOfLst),'L')
            t1.right_child = DTL(examples_right,attr1,distribution_examples(lstOfLst),'R')
            return t1            
            
def bfs_tree(root,tree_id):
    # we use a queue to traverse the tree 
     lst_qu = []
     node_id = 0
     if root == None:
         "Unfortunately nothing seems to be there in the root"
         return
     lst_qu.append(root)
     while lst_qu:
         n = lst_qu.pop(0)
         node_id = node_id + 1
         print "Tree=",tree_id,"Node=",node_id,"feature= ",n.best_attribute,"Thr= ",round(n.best_threshold,2),"gain=",round(n.info_gain,6)
         if n.left_child != None:
             lst_qu.append(n.left_child)
         if n.right_child != None:
             lst_qu.append(n.right_child)   
             
def fetch_distr(obj,tree):
    ### base case
    if tree.best_attribute == -1:
        return tree.distr
    ### recursive case
    if float(obj[tree.best_attribute]) < tree.best_threshold:
        return fetch_distr(obj,tree.left_child)
    else:    
        return fetch_distr(obj,tree.right_child) 
        
def get_predicted_val(pred_distr,target_lst1):
    val = 0
    max_pred_value = max(pred_distr)
    len1 = len(pred_distr)   
    while len1 > 0:
        if pred_distr[len1 - 1] == max_pred_value:
            val = len1 - 1
        len1 = len1 - 1    
    return target_lst1[val]         
        
def predicted_val_num(pred_distr):
#    print pred_distr 
    max_counter = 0
    max_pred_value = max(pred_distr)
    pred_distr_len = len(pred_distr)
    while pred_distr_len > 0:
        if max_pred_value == pred_distr[pred_distr_len - 1]:
            max_counter = max_counter + 1
        pred_distr_len = pred_distr_len - 1
    return 1/float(max_counter)
    
def get_pred_val(pred_distr,target_lst1,actual_num):
    lst = []
    status = 0
    max_pred_value = max(pred_distr)
    pred_distr_len = len(pred_distr)
    while pred_distr_len > 0:
        if max_pred_value == pred_distr[pred_distr_len - 1]:
            lst.append(pred_distr_len - 1)
        pred_distr_len = pred_distr_len - 1
    len1 = len(lst)
#    print "F len",len1
    val = int(random.uniform(0,len1 - 1))
    while len1 > 0:
        if target_lst1[lst[len1-1]] == actual_num:
            status = 1
        len1 = len1 -1    
    return status,target_lst1[val]
    
def accuracy_test(actual_val,pred_val_num,pred_distr,target_lst1):
    if pred_val_num == 1.0:
        pred_val = get_predicted_val(pred_distr,target_lst1)
#        print pred_val,pred_distr
        if pred_val == actual_val:
            return pred_val,actual_val,1.0
        else:
            return pred_val,actual_val,0.0
    else:
        status = 0
#        print "Here 3up"
        status,pred_val = get_pred_val(pred_distr,target_lst1,actual_val)
        if status == 1:
#            print "Here 3"
            return actual_val,actual_val,pred_val_num
        else:
#            print "Here 4"
            return pred_val,actual_val,0.0
    
def class_test(lstOfLst_tst,tree,target_lst1):  
    obj_id = 0
    obj_lst = []
    pred_distr = []
    rows = len(lstOfLst_tst) - 1
    cols = len(lstOfLst_tst[0]) - 1
    accuracy_sum = 0.0
#    print "Rows:",rows,"thresh",tree.best_threshold
    n = 0
#    k = 0
    print "Order mapping of class elements:",target_lst1
    while n<= rows:
        obj_lst = lstOfLst_tst[n]
#        print "object:",obj_id,"and its value:",obj_lst 
        pred_distr = fetch_distr(obj_lst,tree)
        actual_val = obj_lst[cols]
#        pred_distr = [0.04895104895104895, 0.0, 0.013986013986013986, 0.65, 0.65, 0.0, 0.0, 0.04195804195804196, 0.6, 0.0]
        pred_val_num = predicted_val_num(pred_distr)
#        print "pred_val_num:",pred_val_num
#        if float(pred_val_num) < 1 and float(pred_val_num) > 0:
#            k = 1
        pred_val,actual_val,val = accuracy_test(actual_val,pred_val_num,pred_distr,target_lst1)
        print "Id = ",obj_id,"Predicted = ",pred_val,"true = ",actual_val,"accuracy = ",val
        accuracy_sum = accuracy_sum + val
        n = n + 1
        obj_id = obj_id + 1
    print "Classification accuracy=",round((float(accuracy_sum)/float(rows+1)),4)
#    print pred_distr 
    
def pred_distr_avg(obj_lst,tree_lst,target_lst1):
    print obj_lst
    pred_distr_temp = []
    pred_distr = []
    elem = len(tree_lst) - 1
    n = 0
    pred_distr = fetch_distr(obj_lst,tree_lst[n])
#    print "Fetching fishy distribution",pred_distr
    len1 = len(pred_distr)
    while len1 > 0:
        pred_distr_temp.append(0)
        len1 = len1 - 1
#    print "1",pred_distr_temp,pred_distr
    n = n + 1
    while n <= elem:
        pred_distr_temp = []
        pred_distr_temp = fetch_distr(obj_lst,tree_lst[n])
#        print n,"th iteration and pred_distr_temp value:",pred_distr_temp
#        print n,"th iteration and pred_distr value before addition:",pred_distr    
        pred_distr = map(sum, zip(pred_distr, pred_distr_temp))        
#        print n,"th iteration and pred_distr value after addition:",pred_distr    
        n = n + 1
    newList = map(lambda pred_distr: pred_distr/(elem + 1), pred_distr)  
#    print newList
    return newList

def class_test_forest(lstOfLst_tst,tree_lst,target_lst1):  
    obj_id = 0
    obj_lst = []
    pred_distr = []
    rows = len(lstOfLst_tst) - 1
    cols = len(lstOfLst_tst[0]) - 1
    accuracy_sum = 0.0
    print "Rows:",rows
    n = 0
#    k = 0
    print "Order mapping of class elements:",target_lst1
    while n<= rows:
        obj_lst = lstOfLst_tst[n]
#        print "object:",obj_id,"and its value:",obj_lst 
        pred_distr = pred_distr_avg(obj_lst,tree_lst,target_lst1)   #fetch_distr(obj_lst,tree)
        actual_val = obj_lst[cols]
#        pred_distr = [0.04895104895104895, 0.0, 0.013986013986013986, 0.65, 0.65, 0.0, 0.0, 0.04195804195804196, 0.6, 0.0]
        pred_val_num = predicted_val_num(pred_distr)
#        print "pred_val_num:",pred_val_num
#        if float(pred_val_num) < 1 and float(pred_val_num) > 0:
#            k = 1
        pred_val,actual_val,val = accuracy_test(actual_val,pred_val_num,pred_distr,target_lst1)
        print "Id = ",obj_id,"Predicted = ",pred_val,"true = ",actual_val,"accuracy = ",val
        accuracy_sum = accuracy_sum + val
        n = n + 1
        obj_id = obj_id + 1    
    print "Classification accuracy=",round((float(accuracy_sum)/float(rows+1)),4)
            

option = var3   ##'randomized'
#file_name = 'pendigits_training.txt'
file_name = var1   #'satellite_training.txt'
#file_name = 'yeast_training.txt'
#attr1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#attr1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
#attr1 = [0,1,2,3,4,5,6,7]
#
#default = [0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625]
#test_file_name = 'pendigits_test.txt' 

test_file_name = var2   #'satellite_test.txt'
#test_file_name = 'yeast_test.txt'   
    
if option == 'optimized':
    target_lst = []
    target_lst1 = []
    lstOfLst = read_input(file_name)
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
    attr1 = range(0, cols)
    print attr1
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    target_lst1 = list(set(target_lst))

    default = []
    n = len(target_lst1)
    n1 = n
    print n1
    while n > 0:
        default.append(1/float(n1))
        n = n -1
    
    print default
    t1 = tree()
    t1 = DTL(lstOfLst,attr1,default,'Root') 
            
#t1.printByLayer()
            
    bfs_tree(t1,0)             
    lstOfLst_tst = read_input(test_file_name)
    class_test(lstOfLst_tst,t1,target_lst1)

#print lstOfLst_tst

elif option == 'randomized':
    target_lst = []
    target_lst1 = []
    lstOfLst = read_input(file_name)
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
    attr1 = range(0, cols)
    print attr1
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    target_lst1 = list(set(target_lst))

    default = []
    n = len(target_lst1)
    n1 = n
    print n1
    while n > 0:
        default.append(1/float(n1))
        n = n -1
    
    print default
    t2 = tree()
    t2 = DTL_Random(lstOfLst,attr1,default,'Root') 
            
#t1.printByLayer()
            
    bfs_tree(t2,0)             
    lstOfLst_tst = read_input(test_file_name)
    class_test(lstOfLst_tst,t2,target_lst1)
    
elif option == 'forest3':
    tree_lst = []
    target_lst = []
    target_lst1 = []
    lstOfLst = read_input(file_name)
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
    attr1 = range(0, cols)
    print attr1
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    target_lst1 = list(set(target_lst))

    default = []
    n = len(target_lst1)
    n1 = n
    print n1
    while n > 0:
        default.append(1/float(n1))
        n = n -1
    
    print default
    t1 = tree()
    t1 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t1)
#    
    t2 = tree()
    t2 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t2)
#    
    t3 = tree()
    t3 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t3)
            
#t1.printByLayer()
            
    bfs_tree(t1,0)             
    bfs_tree(t2,1) 
    bfs_tree(t3,2) 
    print tree_lst       
    lstOfLst_tst = read_input(test_file_name)
    class_test_forest(lstOfLst_tst,tree_lst,target_lst1) 
    
elif option == 'forest15':
    tree_lst = []
    target_lst = []
    target_lst1 = []
    lstOfLst = read_input(file_name)
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
    attr1 = range(0, cols)
    print attr1
    n = 0
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    target_lst1 = list(set(target_lst))

    default = []
    n = len(target_lst1)
    n1 = n
    print n1
    while n > 0:
        default.append(1/float(n1))
        n = n -1
    
    print default
    t1 = tree()
    t1 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t1)
#    
    t2 = tree()
    t2 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t2)
#    
    t3 = tree()
    t3 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t3)
    
    t4 = tree()
    t4 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t4)
#    
    t5 = tree()
    t5 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t5)
#    
    t6 = tree()
    t6 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t6)
    
    t7 = tree()
    t7 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t7)
#    
    t8 = tree()
    t8 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t8)
#    
    t9 = tree()
    t9 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t9)
    
    t10 = tree()
    t10 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t10)
#    
    t11 = tree()
    t11 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t11)
#    
    t12 = tree()
    t12 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t12)
    
    t13 = tree()
    t13 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t13)
#    
    t14 = tree()
    t14 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t14)
#    
    t15 = tree()
    t15 = DTL_Random(lstOfLst,attr1,default,'Root')
    tree_lst.append(t15)
            
#t1.printByLayer()
            
    bfs_tree(t1,0)             
    bfs_tree(t2,1) 
    bfs_tree(t3,2)
    bfs_tree(t4,3)             
    bfs_tree(t5,4) 
    bfs_tree(t6,5)
    bfs_tree(t7,6)             
    bfs_tree(t8,7) 
    bfs_tree(t9,8)
    bfs_tree(t10,9)             
    bfs_tree(t11,10) 
    bfs_tree(t12,11)
    bfs_tree(t13,12)             
    bfs_tree(t14,13) 
    bfs_tree(t15,14)
#    print tree_lst       
    lstOfLst_tst = read_input(test_file_name)
    class_test_forest(lstOfLst_tst,tree_lst,target_lst1)    
        

