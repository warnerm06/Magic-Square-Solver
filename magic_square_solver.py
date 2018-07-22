
# coding: utf-8

# In[180]:


import itertools 
import collections
import numpy as np
import time

start_time = time.time()
myArray=[1,2,3]
endpoint=50

def incArray():#Increases minimum array value by 1 
    global myArray
    index_min=np.argmin(myArray)
    if index_min< endpoint:
        myArray[index_min] +=1
    print(myArray)
    
def iterate():
    for item in itertools.combinations_with_replacement(myArray,3):
        print(item)
    
    
#generate list of unique values (numbers occur only twice or less)

#Itertools.combinations.... 
#Check if valid
iterate()

print("--- %s seconds ---" % (time.time() - start_time))


# In[179]:


import itertools
arr= [1,2,3]

for item in itertools.combinations_with_replacement(arr,3):
    print(item)
    


# In[129]:


import collections
c=collections.Counter([1,2,3,5,6,5,5])

c


# In[147]:


import numpy as np
mylist = [9,3,4,5,6,7]
index_min=np.argmin(mylist)
print(index_min)


# In[168]:


import time
start_time = time.time()

for i in range(0,362880):
    if i//2 == 0:
        2-1
print("--- %s seconds ---" % (time.time() - start_time))

