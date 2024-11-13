import os

import numpy as np

#%%
workfolder="\\image_folder\\" #change this to the actual location of the photos
labs=[]
labs2=np.zeros((12,17)) #the size of the results should be changed according to the actual experiment conditions
source_root=workfolder+"\\labels\\"
txt_list=os.listdir(source_root)
ii=0
for isub in range(12):

    for i in range(17):
        
        file_name=source_root+txt_list[ii]
        labs.append(np.genfromtxt(file_name,delimiter=' '))
        lab=np.genfromtxt(file_name,delimiter=' ')
        
        if np.shape(lab)[0]==6:
            labs2[isub,i]=lab[0]
        if np.shape(lab)[0]>=2 and np.shape(lab)[0]<6:
            
            maxindx=np.argmax(lab[:,5])
            labs2[isub,i]=lab[maxindx,0]

        if np.shape(lab)[0]==3: print("three detected objects",np.shape(lab)[0])
        if np.shape(lab)[0]==4: print("four detected objects",np.shape(lab)[0])
        ii+=1

labs3=np.copy(labs2)
labs3[labs2==3]=2
labs3[labs2==2]=3 #this is the final result table
