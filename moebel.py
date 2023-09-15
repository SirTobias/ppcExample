# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy.optimize import linprog

#Zielfunktion
obj = [-35, -45, -65] #%x_s: Stühle, x_t: Tische, x_b: Bänke

#Nebenbedingungen (linke Seite)
lhs_ineq = [[ 3.5,  6,  8],  # Arbeitszeit Maschine 1
            [   4,  5,  6],  # Arbeitszeit Maschine 2
            [  11, 15, 20],  # Arbeitszeit Personal
            [  -1,  -1, 1]]  # Produktkonfiguration

#Nebenbedingungen (rechte Seite)
rhs_ineq = [120,  # max. Laufzeit Maschine 1
            100,  # max. Laufzeit Maschine 2
            280,  # max. Arbeitszeit
              0]  # Beschränkung max. Hälfte der Tische von Gesamtprod.

#Gleichheitsbeschränkungen (nicht nötig)
#lhs_eq = [[-1, 5]]  # Green constraint left side
#rhs_eq = [15] 

bnd = [(0, None),  # Wertemenge x_s
       (0, None),  # Wertemenge x_t
       (0, None)]  # Wertemenge s_b



opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              bounds=bnd)

print (opt.fun)
formattedList = ["%.2f" % member for member in opt.x]
print (f"Decision Variables: {formattedList}")
#print (opt.x)
print (opt.message)

