***

`## DIA TEAM MEMBER NOTES (DELETE THIS CELL ON CHECKING POINTS BELOW):`

`### Text changes required if using different dataset to Online Retail:`

- `Change dataset text in "1. Introduction"`
- `Change text in "2. Data Exploration"`

***

# Association Rule Mining

## 1. Introduction

The purpose of this notebook is to demonstrate association rule mining, a *Natural Language Processing (NLP)* technique. This procedure aims to observe frequently occurring patterns, correlations or associations within large datasets.

An example transnational [dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail#) which contains all 541,909 transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail has been used in this notebook.

### 1.1 Import Libraries

The cell immediately below houses the import statements for this script. Please run the cell and continue to scroll to the next cell where the tutorial will continue.

# Data Analysis
import pandas as pd 

# Association Rule Mining
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules

## 2. Data Exploration

The cell below explores the sample dataset being used in this demonstration including the pre-processing of the text and one-hot encoding. Each row corresponds to one item ordered with a corresponding InvoiceNo and CustomerID.

Some pre-processing has to be done:
- remove spaces in 'Description' column
- drop rows that don't have InvoiceNo

One-hot encoding refers to splitting the 'Description' column, which contains categorical data, to many columns depending on the number of categories present in that column. Each column contains a "0" or "1" corresponding to which column it has been placed.  

# Step 1: Read in Excel file
df = pd.read_excel('online-retail-ee.xlsx')

# Step 2: Display first 5 records of dataset
# display(df.head())

# Step 3: Pre-processing of data
df['Description'] = df['Description'].str.strip()
df.dropna(axis = 0, subset = ['InvoiceNo'], inplace = True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')

# Step 4: Display first 5 records of pre-processed dataset
display(df.head())

# Step 5: One-hot encoding function
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

## 3. Association Rule Mining

To conduct association rule mining, the *Apriori* algorithm is used. There are three main components that comprise the algorithm:
- *Support*: how frequently a product appears in the dataset
- *Confidence*: the likelihood that a purchasing order contains product X and product Y together. If the confidence value is 1, then the algorithm detected that both products are purchased together all of the time
- *Lift*: the increase in the ratio of the purchasing order of product X when product Y is also purchased. If the lift value is less than 1, it entails that the purchasing order is unlikely to contain both items together. The greater the value, the better the combination of the products. For example, a lift value of 5 infers that the likelihood of a client having the suggestion of claiming child benefit and lowering their mortgage payments together is five times more than that of suggesting claiming child benefit alone.

### 3.1 Example 1

The cell below conducts association rule mining on the example dataset. The association rules displayed are limited to having a support value of at least 7%, life value of at least 6 and a confidence larger than 0.8.

# Step 1: Create basket containing all French orders
basket = (df[df['Country'] == "France"]
            .groupby(['InvoiceNo', 'Description'])['Quantity']
            .sum().unstack().reset_index().fillna(0)
            .set_index('InvoiceNo'))

# Step 2: One-hot encoding
basket_sets = basket.applymap(encode_units)

# Step 3: Generate frequent itemsets with a support of at least 7%
frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames = True)

# Step 4: Generate association rules
rules = association_rules(frequent_itemsets, metric = "lift", min_threshold=1)

# Step 5: Display association rules with a lift higher or equal to 6 and a confidence higher than or equal to 0.8
display(rules[(rules['lift'] >= 6) &
    (rules['confidence'] >= 0.8)])

### 3.2 Example 2

The following cell generates association rules for all orders in the UK with a minimum support of 5%, a lift higher than 8 and a confidence value of at least 0.5.

# Step 1: Create basket containing all UK orders
basket2 = (df[df['Country'] == "United Kingdom"]
            .groupby(['InvoiceNo', 'Description'])['Quantity']
            .sum().unstack().reset_index().fillna(0)
            .set_index('InvoiceNo'))

# Step 2: One-hot encoding
basket_sets2 = basket2.applymap(encode_units)

# Step 3: Generate frequent itemsets with a support of at least 5%
frequeny_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames = True)

# Step 4: Generate association rules
rules2 = association_rules(frequeny_itemsets2, metric = "lift", min_threshold=1)

# Step 5: Display association rules with a lift higher or equal to 8 and a confidence higher than or equal to 0.5
display(rules[(rules['lift'] >= 8) &
    (rules['confidence'] >= 0.5)])

