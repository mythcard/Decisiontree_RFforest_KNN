Programming Assignment 5: read_me.txt CSE 5360

First Name: Amith Chittane Satyanarayana
Last Name: Hegde
UTA id: 1001171930

Assignment completed in platform: Python 2.7.10

Files submitted in the zip file:
1. test_info_gain.py
3. read_me.txt

Short description of code:
1. DTL(lstOfLst,attr1,default,node_pos1): This function implements the optimized version of decision tree
2. DTL_Random(lstOfLst,attr1,default,node_pos1): This function implements the randomised version of decision tree
3. Directing examples to left and right child is done in both the above modules and is indicated by comment "### directing left and right child"
4. Application of pruning part is specified in code using the comment "### application of pruning"
5. Classfication of decision tree done by the function : class_test(lstOfLst_tst,tree,target_lst1)
6. Classfication of decision forest done by the function : class_test_forest(lstOfLst_tst,tree_lst,target_lst1)

Python code:
test_info_gain.py

Please traansfer all datasets and the above python code to current working directory

How to run:
python <filename> <training_file_name> <test_file_name> <option> 
for example for randomised run for pendigits dataset, please run below command:

python test_info_gain.py pendigits_training.txt pendigits_test.txt randomized

Accuracy Results for various datasets for various runs:

For pendigits:
optimized : 0.8382
randomized: 0.835
forest3   : 0.8922
forest15  : 0.8888

For satellite:
optimized : 0.8205
randomized: 0.8098
forest3   : 0.842
forest15  : 0.844

For yeast:

optimized : 0.5413
randomized: 0.438
forest3   : 0.4298
forest15  : 0.5351