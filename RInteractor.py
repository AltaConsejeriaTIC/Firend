#!/usr/bin/env python

import rpy2.robjects as robjects


robjects.r('''                         
source('R_Firend/Firend.R')
''')

focos = robjects.globalenv['focos']

print focos