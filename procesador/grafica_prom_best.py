import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import numpy

def generar(data):
  for tamano in ['chicas', 'medianas', 'grandes']:
    for paper in ['clei', 'alio']:
      # Columna de mejores obtenidos
      bests = []
      for inst in ['1', '2', '3', '4', '5', '6']:
        bests.append(numpy.max(data[tamano][inst][paper]['greedy']))
      ind = [1, 2, 3, 4, 5, 6]
      plt1 = plt.bar(ind, bests, 0.3, color='#1abc9c')
      
      # Columna de promedios obtenidos
      proms = []
      for inst in ['1', '2', '3', '4', '5', '6']:
        proms.append(numpy.mean(data[tamano][inst][paper]['greedy']))
      ind = numpy.arange(6)+1
      plt2 = plt.bar(ind+0.3, proms, 0.3, color='#3498db')

      # Variables de la grafica
      plt.title('Fitness promedio y mejor encontrado')
      plt.ylabel('Fitness')
      plt.xlabel('Instancia')
      ind = numpy.arange(6) + 1.3
      plt.xticks(ind, ('#1', '#2', '#3', '#4', '#5', '#6'))

      plt.legend([plt1, plt2], ['Fitness Maximo', 'Fitness Promedio'])
          
      # Guardo una imagen
      name = "grafica_prom_best/{0}-{1}.pdf".format(tamano, paper)
      pylab.savefig(name)
      
      # Limpio la grafica
      plt.clf()

  return 0

def generar_montevideo(data):
  for tamano in ['montevideo']:
    for paper in ['clei', 'alio']:
      # Columna de mejores obtenidos
      bests = []
      for inst in ['1', '2', '3', '4']:
        bests.append(numpy.max(data[tamano][inst][paper]['greedy']))
      ind = [1, 2, 3, 4]
      plt1 = plt.bar(ind, bests, 0.3, color='#1abc9c')
      
      # Columna de promedios obtenidos
      proms = []
      for inst in ['1', '2', '3', '4']:
        proms.append(numpy.mean(data[tamano][inst][paper]['greedy']))
      ind = numpy.arange(4)+1
      plt2 = plt.bar(ind+0.3, proms, 0.3, color='#3498db')

      # Variables de la grafica
      plt.title('Fitness promedio y mejor encontrado')
      plt.ylabel('Fitness')
      plt.xlabel('Instancia')
      ind = numpy.arange(4) + 1.3
      plt.xticks(ind, ('#1', '#2', '#3', '#4'))

      plt.legend([plt1, plt2], ['Fitness Maximo', 'Fitness Promedio'])
          
      # Guardo una imagen
      name = "grafica_prom_best/{0}-{1}.pdf".format(tamano, paper)
      pylab.savefig(name)
      
      # Limpio la grafica
      plt.clf()

  return 0