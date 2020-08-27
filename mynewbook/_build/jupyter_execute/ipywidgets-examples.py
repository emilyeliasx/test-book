# ipywidgets

## 1. Introduction

Widgets are eventful python objects that have a representation in the browser, often as a control like a slider, textbox, etc.

https://towardsdatascience.com/bring-your-jupyter-notebook-to-life-with-interactive-widgets-bc12e03f0916

### 1.1 Import Libraries

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

import pandas as pd
import numpy as np
df_london = pd.read_csv("international-visitors-london-raw.csv", encoding = "ISO-8859-1")

display(df_london.head())

ALL = 'ALL'

def unique_sorted_values_append_ALL(array):
    unique = array.unique().tolist()
    unique.sort()  
    unique.insert(0, ALL)
    return unique

output = widgets.Output()

dropdown_year = widgets.Dropdown(options = unique_sorted_values_append_ALL(df_london.year))
dropdown_purpose = widgets.Dropdown(options = unique_sorted_values_append_ALL(df_london.purpose))

def common_filtering(year, purpose):
    output.clear_output()
    
    if (year == ALL) & (purpose == ALL):
        common_filter = df_london
    elif (year == ALL):
        common_filter = df_london[df_london.purpose == purpose]
    elif (purpose == ALL):
        common_filter = df_london[df_london.year == year]
    else:
        common_filter = df_london[(df_london.year == year) & (df_london.purpose == purpose)]
        
    with output:
        display(common_filter)

def dropdown_year_eventhandler(change):
    common_filtering(change.new, dropdown_purpose.value)
            
def dropdown_purpose_eventhandler(change):
    common_filtering(dropdown_year.value, change.new)

dropdown_year.observe(dropdown_year_eventhandler, names ='value')
dropdown_purpose.observe(dropdown_purpose_eventhandler, names = 'value')

display(dropdown_year)
display(dropdown_purpose)


display(output)

