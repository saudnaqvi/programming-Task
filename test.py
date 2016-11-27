# -*- coding: utf-8 -*-
"""
@author: saud

"""

import pandas as pd
import numpy as np

def match_supplier_name(supplierName, invoiceData):
    for k in range(0,len(invoiceData)):
        if supplierName == invoiceData[k].split()[1][1:-1]:
            return True            
    return False
    
# read suppliernames and invoice data 
df            = pd.read_csv('suppliernames.txt')
supplierNames = df.SupplierName

data          = pd.read_csv('invoice.txt', error_bad_lines=False, warn_bad_lines=False)
mask          = np.column_stack([data[row].str.contains(r"\bword\b", na=False) for row in data])

location      = np.where(mask[0])
invoiceData   = data.ix[:,int(location[0][0])]

wordMatches   = 0
i             = 0
# match supplier names to invoice data
while i < len(supplierNames): 
    for j in range(0,len(supplierNames[i].split())):
        if (match_supplier_name(supplierNames[i].split()[j], invoiceData) == True):
            wordMatches = wordMatches+1            
        else:
            break
    if wordMatches == len(supplierNames[i].split()):
        print "This invoice belongs to", supplierNames[i]
        break
    else:
        wordMatches = 0
        i=i+1
        #continue

        
                    
