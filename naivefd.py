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
        violation = 0
        # Loop through the items in the list 
        for value in x.values():
            for i, e in enumerate(value):
                if compare(value[0],e) != 0:
                    violation += 1
                    print("Violation occurred at", int(e) , "in position", i)                        
            
        print("Number of violations",violation)


if __name__ == "__main__":
    groups(my_dict)
   
