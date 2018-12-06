import pandas as pd
import numpy as np
from collections import defaultdict
import itertools
from collections import Counter

# Read data from csv file 
data = pd.read_csv("C:\\Users\\Ajibola Vincent\\Documents\\Udacity\\ay.csv")
#print(data['account_id'].value_counts())
#print(data.account_id.unique())

# Function to compare two elements of a list 
def compare(a, b):
        return (a > b) - (a < b)

# Convert the relevant columns to list for easy handling 
accts = data['account_nbr'].tolist()
acct_ids = data['account_id'].unique().tolist()

# create an empty dictionary 
my_dict = {}
group_dict=dict()
# process items in both lists to create dictionary of keys and values
for item in acct_ids:
    mylist  = data[data['account_id'] == item]['account_nbr']
    my_dict.setdefault(item, []).extend(mylist.tolist())

# Function that does x,y,z
def groups(x):
        # Initialize counter to determine number of violations
        bad=0
        baddest=[]
        for key,value in x.items():
            if len(value) != 1:
                    print("The first occurrence of account number for ", key , " is", value[0])
                    for i in value:
                            if compare(value[0],i) != 0:
                                    bad+= 1
                                    baddest.append(value.index(i))
                                    print("Violation occurred at", i, "in position", value.index(i))                            
            else:
                    print("The only occurrence of account number for ", key , " is", value[0])
        print("Number of violations", bad)
        print(baddest)
       






groups(my_dict)