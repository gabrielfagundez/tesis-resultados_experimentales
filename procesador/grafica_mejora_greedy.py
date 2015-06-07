import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy

legend = [
  False, False, False, False, False, False, False, False, False, False, 
  False, False, False, False, False, False, False, False, False, False
]
charts = []
colors = [
  '#1abc9c', '#3498db', '#9b59b6', '#34495e', '#27ae60', '#e74c3c', '#95a5a6', '#f39c12', '#2ecc71', '#bdc3c7',
  # Mas colores
  'b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k','b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k','b', 'g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k'
]

def generar(data, ejecucion):
  bottom = [0, 0, 0, 0, 0, 0]
  for tamano in ['chicas', 'medianas', 'grandes']:
    for paper in ['clei']:
      for percentaje in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        # Dibujo la grafica
        superacion_greedy = []

        data1 = data[tamano]['1'][paper]['tiempo'][ejecucion[tamano]['1']]
        if len(data1) > (percentaje-1):
          superacion_greedy.append(data1[percentaje-1] - bottom[0])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        data2 = data[tamano]['2'][paper]['tiempo'][ejecucion[tamano]['2']]
        if len(data2) > (percentaje-1):
          superacion_greedy.append(data2[percentaje-1] - bottom[1])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)
        
        data3 = data[tamano]['3'][paper]['tiempo'][ejecucion[tamano]['3']]
        if len(data3) > (percentaje-1):
          superacion_greedy.append(data3[percentaje-1] - bottom[2])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        data4 = data[tamano]['4'][paper]['tiempo'][ejecucion[tamano]['4']]
        if len(data4) > (percentaje-1):
          superacion_greedy.append(data4[percentaje-1] - bottom[3])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        data5 = data[tamano]['5'][paper]['tiempo'][ejecucion[tamano]['5']]
        if len(data5) > (percentaje-1):
          superacion_greedy.append(data5[percentaje-1] - bottom[4])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        data6 = data[tamano]['6'][paper]['tiempo'][ejecucion[tamano]['6']]
        if len(data6) > (percentaje-1):  
          superacion_greedy.append(data6[percentaje-1] - bottom[5])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        ind = [1, 2, 3, 4, 5, 6]
        plot = plt.bar(ind, superacion_greedy, 0.6, bottom=bottom, color=colors[percentaje-1])
        charts.append(plot)
        for i in [0, 1, 2, 3, 4, 5]:
          bottom[i] = bottom[i] + superacion_greedy[i]


    plt.title('Mejora a greedy sobre el tiempo')
    plt.ylabel('Tiempo(s)')
    plt.xlabel('Instancia')
    ind = numpy.arange(6) + 1.3
    plt.xticks(ind, ('#1', '#2', '#3', '#4', '#5', '#6'))

    legend_names = []
    for idx, val in enumerate(legend):
      name = "Supera {0}%".format(idx*5)
      if val and idx != 0:
        legend_names.append(name)
      
    plt.legend(charts, legend_names)
          
    # Guardo una imagen
    name = "grafica_mejora_greedy/{0}.pdf".format(tamano)
    pylab.savefig(name)

    # Limpio la figura
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
      legend[i] = False

    for j in [0, 1, 2, 3, 4, 5]:
      bottom[j] = 0
    
    plots = []  
    plt.clf()

  return 0


def generar_montevideo(data, ejecucion):
  bottom = [0, 0, 0, 0]
  for tamano in ['montevideo']:
    for paper in ['clei']:
      for percentaje in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        # Dibujo la grafica
        superacion_greedy = []

        data1 = data[tamano]['1'][paper]['tiempo'][ejecucion[tamano]['1']]
        if len(data1) > (percentaje-1):
          superacion_greedy.append(data1[percentaje-1] - bottom[0])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        data2 = data[tamano]['2'][paper]['tiempo'][ejecucion[tamano]['2']]
        if len(data2) > (percentaje-1):
          superacion_greedy.append(data2[percentaje-1] - bottom[1])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)
        
        data3 = data[tamano]['3'][paper]['tiempo'][ejecucion[tamano]['3']]
        if len(data3) > (percentaje-1):
          superacion_greedy.append(data3[percentaje-1] - bottom[2])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        data4 = data[tamano]['4'][paper]['tiempo'][ejecucion[tamano]['4']]
        if len(data4) > (percentaje-1):
          superacion_greedy.append(data4[percentaje-1] - bottom[3])
          legend[percentaje-1] = True
        else:
          superacion_greedy.append(0)

        ind = [1, 2, 3, 4]
        plot = plt.bar(ind, superacion_greedy, 0.6, bottom=bottom, color=colors[percentaje-1])
        charts.append(plot)
        for i in [0, 1, 2, 3]:
          bottom[i] = bottom[i] + superacion_greedy[i]


    plt.title('Mejora a greedy sobre el tiempo')
    plt.ylabel('Tiempo(s)')
    plt.xlabel('Instancia')
    ind = numpy.arange(4) + 1.3
    plt.xticks(ind, ('#1', '#2', '#3', '#4'))

    legend_names = []
    for idx, val in enumerate(legend):
      name = "Supera {0}%".format(idx*5)
      if val and idx != 0:
        legend_names.append(name)
      
    plt.legend(charts, legend_names)
          
    # Guardo una imagen
    name = "grafica_mejora_greedy/{0}.pdf".format(tamano)
    pylab.savefig(name)

    # Limpio la figura
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
      legend[i] = False

    for j in [0, 1, 2, 3]:
      bottom[j] = 0
    
    plots = []  
    plt.clf()

  return 0