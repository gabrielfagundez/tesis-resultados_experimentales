# Imports
import file_handler
import structures
import tabla_por_instancia
import tabla_por_tamano
import tabla_comparacion_greedy
import fitness_over_time
import grafica_prom_best
import grafica_mejora_greedy
import tabla_alio_vs_clei

# Librerias
import argparse
import numpy

# Variables
fst_lev_fld = ['pmEA-ALIO', 'seqEA-CLEI']
snd_lev_fld = ['greedy', 'aleatorio']
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

# Resultados para tablas
res_fitness = structures.res_structure()
res_tiempo_maximo_por_instancia = structures.estructura_tiempo_maximo_por_instancia()
res_tiempo_maximo_por_tamano    = structures.estructura_tiempo_maximo_por_tamano()
res_greedy_maximo_por_instancia = structures.estructura_tiempo_maximo_por_instancia()
res_greedy_maximo_por_tamano    = structures.estructura_tiempo_maximo_por_tamano()

# Resultados para graficas
chart_fitness_over_time = structures.chart_fitness_over_time()
chart_mejora_greedy     = structures.chart_fitness_over_time()

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
          val_greedy = 0
          val_final = 0

          if file != []:
            chart_encontre_tiempo_final = False

            for num, line in enumerate(file, 1):
              if pref_generacion in line:
                # Formato: ['GEN', '10000', '404.130000']
                splitted_line = line.split('\n')[0].split(' ')
                if splitted_line[1] == '0':
                  val_greedy = float(splitted_line[2])



              # ========================= TIEMPO =========================
              if pref_generacion in line:
                # Formato: ['GEN', '0', '655.870000']
                splitted_line = line.split('\n')[0].split(' ')
                generacion  = int(splitted_line[1])
                fitness     = float(splitted_line[2])
                
                if inicializacion == 'greedy':
                  variable = file_name.split('.')[0].split('salida_')[1]
                  
                  if generacion == 0:
                    chart_fitness_over_time[tamano][instancia][paper]['fitness'][variable] = []
                    chart_fitness_over_time[tamano][instancia][paper]['fitness'][variable].append(fitness)
                  if generacion == 10000:
                    if len(chart_fitness_over_time[tamano][instancia][paper]['fitness'][variable]) == 1:
                      chart_fitness_over_time[tamano][instancia][paper]['fitness'][variable].append(fitness)
                    else:
                      if fitness < chart_fitness_over_time[tamano][instancia][paper]['fitness'][variable][-1]:
                        chart_fitness_over_time[tamano][instancia][paper]['fitness'][variable][-1] = fitness

              

              # ========================= GREEDY =========================
              if pref_greedy in line:
                # Formato: ['GREEDY', '15', '0.277533']
                splitted_line = line.split('\n')[0].split(' ')
                variable = file_name.split('.')[0].split('salida_')[1]

                if inicializacion == 'greedy' and paper == 'clei':
                  chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable].append(float(splitted_line[1]))
                  chart_mejora_greedy[tamano][instancia][paper]['tiempo'][variable].append(float(splitted_line[2]))

                if inicializacion == 'greedy' and paper == 'alio':
                  if chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable] == []:
                    chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable].append(float(splitted_line[1]))
                    chart_mejora_greedy[tamano][instancia][paper]['tiempo'][variable].append(float(splitted_line[2]))
                  else:
                    encontre = False
                    indice_encontre = 0
                    # Chequeo si ya agregue el greedy
                    while not encontre and (indice_encontre < len(chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable])):
                      if chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable][indice_encontre] == float(splitted_line[1]):
                        encontre = True
                      indice_encontre += 1
                    indice_encontre -= 1  


                    if not encontre:
                      # Nuevo entero encontrado
                      chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable].append(float(splitted_line[1]))
                      chart_mejora_greedy[tamano][instancia][paper]['tiempo'][variable].append(float(splitted_line[2]))
                    else:
                      a = 0
                      # Entero ya encontrado
                      if chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable][indice_encontre] > float(splitted_line[1]):
                        chart_mejora_greedy[tamano][instancia][paper]['fitness'][variable][indice_encontre] = float(splitted_line[1])
                      

            # Agrego valores para tabla comparativa
            res_fitness[tamano][instancia][paper][inicializacion].append(val_final)
              

# Genero grafica de mejora de greedy
grafica_mejora_greedy.generar(chart_mejora_greedy, 'chicas', 'clei', 1, chart_fitness_over_time)
grafica_mejora_greedy.generar(chart_mejora_greedy, 'medianas', 'clei', 1, chart_fitness_over_time)
grafica_mejora_greedy.generar(chart_mejora_greedy, 'grandes', 'clei', 1, chart_fitness_over_time)
grafica_mejora_greedy.generar(chart_mejora_greedy, 'montevideo', 'clei', 2, chart_fitness_over_time)

grafica_mejora_greedy.generar(chart_mejora_greedy, 'chicas', 'alio', 1, chart_fitness_over_time)
grafica_mejora_greedy.generar(chart_mejora_greedy, 'medianas', 'alio', 1, chart_fitness_over_time)
grafica_mejora_greedy.generar(chart_mejora_greedy, 'grandes', 'alio', 2, chart_fitness_over_time)
grafica_mejora_greedy.generar(chart_mejora_greedy, 'montevideo', 'alio', 1, chart_fitness_over_time)




