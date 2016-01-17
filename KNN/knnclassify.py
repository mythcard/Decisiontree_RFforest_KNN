# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:37:01 2015

@author: mythcard
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 05:19:50 2015

@author: mythcard
"""
import math
from sys import argv
crap, var1, var2, var3 = argv

#v = 4700

def isNotEmpty(s):
    return bool(s and s.strip())


def get_normalised_val(mean,sd,val):
    n = float(val - mean)/float(sd)
    return n
    
def calculate_mean(lst):
    n = sum(lst)
#    print n
#    if len(lst) == 0:
#        print "Yes here"
    len1 = len(lst)
    if len1 == 0:
        n = float(n)/1.0
    else:        
        n = float(n)/float(len1)
    return n
    
def cal_mean_and_sd_attr(lst_of_lst,attr):
    x_lst = []
    rows = len(lst_of_lst) - 1  
    n = 0
#    print "Calculate length of intermediate list: ",rows
    while n <= rows:
        val = float(lst_of_lst[n][attr])
        x_lst.append(val)
        n = n + 1  
#    print "Claculate length of intermediate list: ",x_lst   
    mean1 = calculate_mean(x_lst)    
    sd1 = calculate_sd(x_lst)
    return mean1,sd1
    
def calculate_sd(lst):
    len1 = len(lst)
    mean = sum(lst)
    if len1 == 0:
        mean = float(mean)/1.0
    else:        
        mean = float(mean)/float(len1)
    n = 0
    sd = 0
    while n < len1:
        val = 0
        val = mean - lst[n]
        val = val ** 2
        sd = sd + val
        n = n + 1
    if len1 == 0:
        print "Please correct the test or training file."
        return 1   
    sd = sd / (len1-1) 
    sd = math.sqrt(sd)
    return sd   
    
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


def genrate_mean_sd_list(lstOfLst):
    mean =[]
    sd = []
    cols = len(lstOfLst[0]) - 1
    n = 0
    while n < cols:
#        print "Checking length of list genrate_mean_sd_list",len(lstOfLst)
        mean_val,sd_val = cal_mean_and_sd_attr(lstOfLst,n)
        mean.append(mean_val)
        sd.append(sd_val)
        n = n + 1
    return mean,sd   


    
def generate_normal_lst(lstOfLst,mean,sd):
    rows = len(lstOfLst) - 1
    lst_of_lst = [[] for _ in range(rows+1)]
    sep_lst = []
    cols = len(lstOfLst[0]) - 1
    k = 0
    while k <= rows:
        n = 0
        del sep_lst[:]
        while n < cols:
            
            normalized_val = get_normalised_val(mean[n],sd[n],float(lstOfLst[k][n]))
#            print k,n,normalized_val
            lst_of_lst[k].append(normalized_val)
#            print sep_lst
            n = n + 1
#        lst_of_lst.append(sep_lst)
        k = k + 1
    return lst_of_lst
    
def calculate_distance(test_object_lst,train_object_lst):
    len1 = len(test_object_lst)
    len2 = len(train_object_lst)
    sum1 = 0
    if(len1 == len2):
#        print "We are good to go"
        n = 0
        while n < len1:
            sum1 = sum1 + ((test_object_lst[n] - train_object_lst[n])**2)
            n = n + 1
        sum1 = math.sqrt(sum1)
        return sum1
    else:
#        print "Something is wrong"
        return 0
        
### generating distance function list between one test object and all training objects
def generate_distance_func_lst(lst_of_lst_train,test_object_lst):
      distance_func_lst = []
      len1 = len(lst_of_lst_train)
      n = 0
      while n < len1:
          val = calculate_distance(test_object_lst,lst_of_lst_train[n])
          distance_func_lst.append(val)
          n = n + 1  
      return distance_func_lst
      
def generate_class_dict(distance_func_lst,lstOfLst,knn_n):
    class_dict1 = {'zero123':1}
    min_index = -1
    min_dist = -1
    class_dict1.clear()   
    target_lst = []
    target_lst1 = []
    rows = len(lstOfLst) - 1
    cols = len(lstOfLst[0]) - 1
    n = 0
    ### getting distinct classes and sorting it    
    while n <= rows:
        target_lst.append(lstOfLst[n][cols])
        n = n +1
    target_lst1 = list(set(target_lst))
    target_lst1.sort()
    ### creating a dict of class/counter pairs with counter being 0 in the begining
    k = 0
    len1 = len(target_lst1)
    while k < len1:
        class_dict1.update({target_lst1[k]:0})
        k = k +1
#    print class_dict1 
    knn_counter = 0
    while knn_counter < knn_n:   
    ### find min and index and pop it from distance_func_lst and add the class/counter pair
        counter = 0
        index_val = distance_func_lst.index(min(distance_func_lst))
        popped_val = distance_func_lst.pop(distance_func_lst.index(min(distance_func_lst)))
#        print "Popped value: ",popped_val,len(distance_func_lst)
        class_val = lstOfLst[index_val][cols]
#    print class_val
        for key in class_dict1.iterkeys():
#            print key
            if key == class_val:
                counter =  class_dict1[key]
#            print counter
                counter = counter + 1
#            print counter
                class_dict1.update({key:counter})
                break
        if knn_counter == 0:
            min_index = index_val
            min_dist = popped_val
        knn_counter = knn_counter + 1    
    return class_dict1,min_index,min_dist

def max_val_key(d):  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]  
     
def check_pred_class_match(d,pred_class,true_class,max_val):
    class_match = 0
    itr_cnt = 0
#    print "Pred class and true class: ",pred_class,true_class
    for key in d.iterkeys():
        if key == true_class and d[key] == max_val:
            class_match = 1
            break
    for key in d.iterkeys():
        if d[key] == max_val:
            itr_cnt = itr_cnt + 1    
#    print "Class match and iteration count:",class_match, itr_cnt        
    return class_match, itr_cnt       

def get_class_accuracy(d,pred_class,true_class):
    v=list(d.values())
    k=list(d.keys())
    max_val_counter = 0
    len1 = len(v)
    tie = 0
#    print "Maximum value",max(v)
    k = 0
    for key in d.iterkeys():
        if key != pred_class and d[key] == max(v):
            tie = 1
            break
        else:
            continue
#    print "tie:",tie   
    if tie == 0:
        if pred_class == true_class:
            return 1
        else:
            return 0
    elif tie == 1:
        pred_class_match, itr_cnt = check_pred_class_match(d,pred_class,true_class,max(v)) 
        if pred_class_match == 1:
#            print "Here3"
            return 1/float(itr_cnt)
        elif pred_class_match == 0:
#            print "Here4"
            return 0
        else:
            print "Something went wrong"
            return -1
    
lstOfLst = []
lstOfLst_test = []    
lst_of_lst_train = []
lst_of_lst_test = []
distance_func_lst = []
class_dict1 = {'zero123':1}
class_dict1.clear()
min_index = -1
mean =[]
sd = []
knn_n = int(var3)
test_file_name = var2  ##'pendigits_test.txt'
lstOfLst_test = read_input(test_file_name)
rows = len(lstOfLst_test) - 1 
cols = len(lstOfLst_test[0]) - 1
#print "Checking length:",len(lstOfLst_test)
mean,sd = genrate_mean_sd_list(lstOfLst_test)
lst_of_lst_test = generate_normal_lst(lstOfLst_test,mean,sd) 
#print lst_of_lst_test[0]        

#del lstOfLst[:]
del mean[:]
del sd[:]

train_file_name = var1  ##'pendigits_training.txt'
lstOfLst = read_input(train_file_name)   

mean,sd = genrate_mean_sd_list(lstOfLst)
#print "SD list as follows:",sd
#print "Mean list as follows:",mean

#lst_of_lst_train = generate_normal_lst(lstOfLst,mean,sd)             
#print lst_of_lst_train[0]
#test_id = 0
#sum_accuracy = 0.0
#while test_id<=rows:
#    ## calculating distance list for one test object
#    del distance_func_lst[:]
#    distance_func_lst = generate_distance_func_lst(lst_of_lst_train,lst_of_lst_test[test_id])
#
#    ## getting classification dictonary, minimum element from traning examples, and minimum distance
#    class_dict1,min_index,min_dist  = generate_class_dict(distance_func_lst,lstOfLst,knn_n)
#    pred_class = max_val_key(class_dict1)
#    accuracy = get_class_accuracy(class_dict1,pred_class,lstOfLst_test[test_id][cols])
#    print "Id= ",test_id,", predicted= ",pred_class,", true= ",lstOfLst_test[test_id][cols],", nn= ",min_index,", distance= ",round(min_dist,5),", accuracy: ",round(accuracy,2)
#    sum_accuracy = sum_accuracy + accuracy
#    test_id = test_id + 1
#    
##print "Sum accuracy and total number: ",sum_accuracy,test_id
#print "clasification accuracy",sum_accuracy/float(test_id)
    