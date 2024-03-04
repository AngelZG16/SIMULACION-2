from math import *
from scipy.stats import chi2_contingency
import numpy as np


tab_data = [[203,150,190,305],[195,170,250,400]]


print("Valor P =",chi2_contingency(tab_data)[1])

print("Estadistico de prueba ",chi2_contingency(tab_data)[0])
print("grados de libertad ",chi2_contingency(tab_data)[2])



