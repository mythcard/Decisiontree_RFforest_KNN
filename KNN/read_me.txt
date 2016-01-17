Programming Assignment 8: read_me.txt CSE 5360

First Name: Amith Chittane Satyanarayana
Last Name: Hegde
UTA id: 1001171930

Assignment completed in platform: Python 2.7.10

Files submitted in the zip file:
1. knnclassify.py
2. readme.txt
3. All other input files


Python code:
knnclassify.py

Please traansfer all datasets and the above python code to current working directory

How to run:
python <filename> <training_file_name> <test_file_name> <option> 
for example for pendigits with Knn =5:knnclassify pendigits_training.txt pendigits_test.txt 5

python hist_gaussian_mixx.py pendigits_training.txt pendigits_test.txt gaussians

Explanation on code:
1. Normalisation of both test and training file is implemented by the function get_normalised_val
2. calculate_distance function calaculates the L2 distance
3. Classification is carried out by the functions generate_class_dict and check_pred_class_match
4. Correct implementation is performed by proper coordination of above 3 functionalities which is implemented in the code

Accuracy Results for various datasets for various runs:

For pendigits:
for knn = 1,accracy: 0.973127501429
for knn = 5,accracy: 0.799056603774

For satellite:
for knn = 1,accracy: 0.892
for knn = 5,accracy: 0.87875

For yeast:

for knn = 1,accracy: 0.487603305785
for knn = 5,accracy: 0.394214876033