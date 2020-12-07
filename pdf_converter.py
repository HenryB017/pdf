#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 01:02:46 2020

@author: hboogs
"""

import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

##Creating a pdf using FPDF
pdf= FPDF()
pdf.add_page()
pdf.set_font('Helvetica', size=15)

pdf.cell(200, 10, txt= 'Arsenal vs Spurs predictions, 2-1 Arsenal, Aubameyang brace', 
         #ln=2, align='C')

pdf.cell(200, 10, txt= 'Son to  socre for Spurs', 
         #ln=2, align='C')
pdf.output('ARSvTOT.pdf')

#Dataframe to PDF
nba_dict = {'Player Name': ['Lebron', 'Jordan', 'Hakeem', 'Carmelo'], 'Team': ['Lakers', 'Bulls', 'Rockets', 'Knicks']}
df=pd.DataFrame(nba_dict, columns= ['Player Name', 'Team'])

#Creating table
fig, ax= plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
table=ax.table(cellText=df.values, colLabels=df.columns, loc='center')

#Converting to pdf
pp = PdfPages('HOF.pdf')
pp.savefig(fig, bbox_inches='tight')
pp.close()
