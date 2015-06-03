# Imports
import file_handler
import structures
import tabla_por_instancia
import tabla_por_tamano

# Librerias
import argparse
import numpy

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
pref_generacion  = 'GEN'
pref_tiempo      = 'TIEMPO'
pref_greedy      = 'GREEDY'

# Resultados
res_generaciones  = structures.res_structure()
res_tiempo        = structures.res_structure()
res_greedy        = structures.res_structure()

res_tiempo_maximo_por_instancia = structures.estructura_tiempo_maximo_por_instancia()
res_tiempo_maximo_por_tamano    = structures.estructura_tiempo_maximo_por_tamano()


# Comportamiento principal
for l1 in fst_lev_fld:
  
  # Defino alio / clei
  paper = 'clei'
  if 'ALIO' in l1:
    paper = 'alio'

  for l2 in snd_lev_fld: 

    # Defino aleatorio / greedy
    inicializacion = 'aleatorio'
    if 'greedy' in l2:
      inicializacion = 'greedy'

    for l3 in trd_lev_fld: 
      
      # Defino tamano
      tamano = 'chicas'
      if 'Medianas' in l3:
        tamano = 'medianas'
      if 'Grandes' in l3:
        tamano = 'grandes'
      if 'Montevide' in l3:
        tamano = 'montevideo'

      for l4 in fth_lev_fld:

        # Defino numero de instancia
        instancia = '1'
        if '2/1' in l4:
          instancia = '2'
        if '3/1' in l4:
          instancia = '3'
        if '4/1' in l4:
          instancia = '4'
        if '5/1' in l4:
          instancia = '5'
        if '6/1' in l4:
          instancia = '6'

        for file_name in file_names:
          file_ref = '../{0}/{1}/{2}/{3}/{4}'.format(l1, l2, l3, l4, file_name)
          file = file_handler.read_file(file_ref)

          # Variables: paper, inicializacion, tamano & instancia
          ultimo_tiempo = ''

          if file != []:
            for num, line in enumerate(file, 1):
              if pref_generacion in line:
                # Formato: ['GEN', '10000', '404.130000']
                splitted_line = line.split('\n')[0].split(' ')

                # Agrego al arreglo
                res_generaciones[tamano][instancia][paper][inicializacion].append([splitted_line[1], splitted_line[2]])

              if pref_tiempo in line:
                # Formato: ['TIEMPO', '0', '655.870000']
                splitted_line = line.split('\n')[0].split(' ')
                ultimo_tiempo = splitted_line[1]

                # Agrego al arreglo
                res_tiempo[tamano][instancia][paper][inicializacion].append([splitted_line[1], splitted_line[2]])

              if pref_greedy in line:
                # Formato: ['GREEDY', '15', '0.277533']
                splitted_line = line.split('\n')[0].split(' ')

                # Agrego al arreglo
                res_greedy[tamano][instancia][paper][inicializacion].append([splitted_line[1], splitted_line[2]])
            
            # Agrego ultimo tiempo
            if inicializacion == 'greedy':
              res_tiempo_maximo_por_tamano[tamano][paper].append(float(ultimo_tiempo))
              

# Genero tabla por instancia
tabla_por_tamano.generar(res_greedy, res_tiempo_maximo_por_tamano)



