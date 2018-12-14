import pandas as pd
from collections import defaultdict

# Read data from csv file 
data = pd.read_csv("C:\\Users\\Ajibola Vincent\\Documents\\Udacity\\ay.csv")

# Function to compare two elements of a list 
def compare(a, b):
        return (a > b) - (a < b)

# Convert the relevant columns to list for easy handling 
#accts = data['account_nbr'].tolist()
acct_ids = data['account_id'].unique().tolist()

# create an empty dictionary 
my_dict = {}
# process items in both lists to create dictionary of keys and values
for item in acct_ids:
    mylist  = data[data['account_id'] == item]['account_nbr']
    my_dict.setdefault(item, []).extend(mylist.tolist())


# Function that does x,y,z
def groups(x):
        tools = []
        # Initialize counter to determine number of violations
        # Loop through the items in the list 
        for values in x.values():
                for e in values:
                        if compare(values[0],e) != 0:
                                tools.append(e)
        return tools


def fd(alist):
        for i in  data[data['account_nbr'].isin(alist)].index.get_values():
                print("Violation at index", i, "dataframe")
                
                

if __name__ == "__main__":
    fd(groups(my_dict))

