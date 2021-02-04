#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Wei Zhou
# DATE CREATED:  30/01/2021                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # creates empty dict, determine the number of items in the dict
    results_dic = dict()
    items_in_dic = len(results_dic)
    
    # read filenames from a folder
    filenames = listdir(image_dir)
    pet_labels = 'dognames.txt'
    
    # pet image file format for label matching
    filename_list = ''
    
    for filename in filenames:
        if filename not in results_dic and not filename.startswith('.'):
            filename_split = filename.lower().split('_')
            # remove the digits and trailling white space
            pet_name = ' '.join([word for word in filename_split if word.isalpha()])
            pet_name = pet_name.strip()
            # add new entry to the result_dic with the extracted filename
            results_dic[filename] = [pet_name]
        else:
            print("** Warning: Duplicate files exist in directory:", 
                  filename) 

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
