#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os 
import pandas as pd

path_0 = "/tank1/iorio/TEwoc/SEVN_simulations_new/"
metallicity=[0.01, 0.014, 0.016, 0.02]
alfa=[0.5, 1, 3]
for i in metallicity :
    for j in alfa :
        file = "sevn_output_Z" + "{}".format(i) +"A" + "{}".format(j) + "L1"
        #os.mkdir('/home/martemucci/Filtering/F_data/F_'+ file)
        exec(open("/home/martemucci/Filtering/LOOP_FIL.py").read())
        
        
        
        #Organising the Sevn folders:
        dest = "/home/martemucci/Filtering/F_data/F_"+file+'/'
        f_file = os.listdir(dest)
        for f in f_file:
            globals()[f]=pd.read_csv(dest+f)
        k =0
        while k<29:
            globals()['Filtered_output_{}.csv'.format(k+1)] = pd.merge(globals()['Filtered_output_{}.csv'.format(k)], globals()['Filtered_output_{}.csv'.format(k+1)], how = 'outer')
            k= k+1
        finall_dataset= 'FZ{}A{}.csv'.format(i, j)
        globals()['Filtered_output_29.csv'].to_csv(dest + finall_dataset)
        for f in f_file:
            if f.startswith('Filtered_output'):
                os.remove(dest+f)
        
        
        

