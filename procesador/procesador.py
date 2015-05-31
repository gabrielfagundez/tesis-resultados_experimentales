# Imports
import file_handler

# Variables
fst_lev_fld = ['pmEA-ALIO', 'seqEA-CLEI']
snd_lev_fld = ['aleatorio', 'greedy']
trd_lev_fld = ['1-Chicas', '2-Medianas', '3-Grandes', '4-Montevideo']
fth_lev_fld = ['1/1', '2/1', '3/1', '4/1', '5/1', '6/1']
file_names  = [
                  'salida_1.txt', 'salida_11.txt', 'salida_21.txt',
                  'salida_2.txt', 'salida_12.txt', 'salida_22.txt',
                  'salida_3.txt', 'salida_13.txt', 'salida_23.txt',
                  'salida_4.txt', 'salida_14.txt', 'salida_24.txt',
                  'salida_5.txt', 'salida_15.txt', 'salida_25.txt',
                  'salida_6.txt', 'salida_16.txt', 'salida_26.txt',
                  'salida_7.txt', 'salida_17.txt', 'salida_27.txt',
                  'salida_8.txt', 'salida_18.txt', 'salida_28.txt',
                  'salida_9.txt', 'salida_19.txt', 'salida_29.txt',
                  'salida_10.txt','salida_20.txt', 'salida_30.txt'
              ]

# Prefijos
generacion  = 'GEN'
tiempo      = 'TIEMPO'
greedy      = 'GREEDY'

# Comportamiento principal
for l1 in fst_lev_fld:
  for l2 in snd_lev_fld: 
    for l3 in trd_lev_fld: 
      for l4 in fth_lev_fld:
        for file_name in file_names:
          file_ref = '../{0}/{1}/{2}/{3}/{4}'.format(l1, l2, l3, l4, file_name)
          file = file_handler.read_file(file_ref)
