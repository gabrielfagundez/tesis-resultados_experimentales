import estadisticas
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy
from collections import OrderedDict

legend = [
  False, False, False, False, False, False, False, False, False, False, 
  False, False, False, False, False, False, False, False, False, False
]
colors = ["#F7FF00","#DEF800","#C6F200","#AEEB00","#95E500","#7DDF00","#65D800","#4CD200","#34CB00","#1CC500","#04BF00"]
width = 1


def generar(data, ejecucion, tamano, paper, label_location, data_estadisticas):

  # Limpio la grafica
  plt.clf()

  if tamano == "montevideo":
    cantidad_instancias = 4
  else:
    cantidad_instancias = 6

  labels_x = []
  indice_x = 0

  for num_instancia in range(1, cantidad_instancias + 1):

    # Dibujo instancias
    label_instancia = "%d"%(num_instancia)
    labels_x.append(label_instancia)
    
    # Obtengo mejores valores y mejor ejecucion
    greedy_costo    = 'greedy_costo'
    greedy_demora   = 'greedy_demora'
    mejor_ejecucion = estadisticas.mejor_ejecucion(data_estadisticas, tamano, paper, num_instancia)
    mejora_final    = estadisticas.mejor_mejora_greedy(data_estadisticas, tamano, paper, num_instancia, mejor_ejecucion)
    bottom = 0.0

    for ind_porcentaje_sup_greedy in range(0, len(data[tamano][label_instancia][paper]['tiempo'][mejor_ejecucion])):
      porcentaje_sup_greedy = ind_porcentaje_sup_greedy * 5
      tiempo_superacion_greedy = data[tamano][label_instancia][paper]['tiempo'][mejor_ejecucion][ind_porcentaje_sup_greedy] - bottom
      
      # Dibujo la grafica
      plt.bar(indice_x, tiempo_superacion_greedy, width, bottom=bottom, color=colors[ind_porcentaje_sup_greedy], align='center', label="%d%%"%porcentaje_sup_greedy)

      # Actualizo el piso
      bottom = bottom + tiempo_superacion_greedy

    # Dibujo texto superior
    plt.text(indice_x, bottom, "%.1f%%"%(mejora_final), ha='center', va='bottom', rotation=90)

    # Paso a siguiente instancia
    indice_x+=1   

  
  plt.xticks(range(0,indice_x), labels_x,  ha='center',rotation=90)
  plt.tick_params(axis='x', which='major', width=0)
  plt.xlabel ("instancia")
  plt.ylabel ("tiempo (s)")
  plt.xlim([-0.5,indice_x-0.5])

  handles, labels = plt.gca().get_legend_handles_labels()
  handles         = [y for (x,y) in sorted(zip(labels, handles),key = lambda a: float(a[0][:-1]))]
  labels          = sorted(labels, key = lambda a: float(a[:-1]))
  hand_lab_dict   = OrderedDict(zip(labels,handles))
  plt.legend(hand_lab_dict.values(), hand_lab_dict.keys(), loc=0, ncol=3, prop={ 'size': 8 })

  # Guardo una imagen
  name = "grafica_mejora_greedy/{0}_{1}.pdf".format(tamano, paper)
  pylab.savefig(name)


