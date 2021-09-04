#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np


# In[66]:


fd = open('Record.txt','a')
fd.write("1001,Drink,45,95\n1002,Cake,300,7\n1003,Choklate,10,40")


# In[17]:


fd = open('Record.txt','r')
txt=fd.read()
fd.close()


# In[18]:


txt


# In[19]:


txt.split("\n")


# In[20]:


products = txt.split("\n")


# In[21]:


products


# In[ ]:





# In[23]:


for i in products:
    print(i.split(","))


# In[27]:


for i in products:
    prod=i.split(",")
    print(prod[0])
    print(prod[1])
    print(prod[2])
    print(prod[3],"\n")


# In[ ]:





# In[ ]:





# In[49]:


products = txt.split("\n")
ui_prod=str(input("Enter product id:"))
ui_quan=int(input("Enter quantity:"))

for i in products:
    prod=i.split(",")
    
    if(ui_prod==prod[0]):
        print("\n***********************************************")
        print("Product id ",prod[0])
        print("Product name ",prod[1])
        print("Quantity :", ui_quan)
        print("Product price ",prod[2])
        print("***********************************************")
        print("Billing Amount :", (int(prod[2]) * ui_quan))


# In[ ]:





# In[61]:


new_record=[]

for product in products:
    prod=product.split(",")
    if(ui_prod==prod[0]):
        prod[3]=str(int(prod[3])-ui_quan)
    
    new_record.append(prod[0]+","+prod[1]+","+prod[2]+","+prod[3]+"\n")
    
new_record[-1]=new_record[-1][:-1]


# In[55]:


products


# In[56]:


new_record


# In[62]:


fd=open('record.txt','w')
for i in new_record:
    fd.write(i)

fd.close()


# In[63]:


for i in products:
    print(i)


# In[ ]:




