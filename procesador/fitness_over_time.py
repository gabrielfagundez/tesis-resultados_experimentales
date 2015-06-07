import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

def generar(data):
  for tamano in ['chicas', 'medianas', 'grandes', 'montevideo']:
    for ins in ['1', '2', '3', '4', '5', '6']:
      if not(tamano == 'montevideo' and ins == '5' or tamano == 'montevideo' and ins == '6'):
        # Dibujo la grafica
        plt.plot(data[tamano][ins]['clei']['tiempo']['1'], data[tamano][ins]['clei']['fitness']['1'])
        plt.ylabel('fitness')
        plt.xlabel('tiempo(s)')

        # Guardo una imagen
        name = "fitness_over_time/{0}_{1}.pdf".format(tamano, ins)
        pylab.savefig(name)

        # Limpio la figura
        plt.clf()

  return 0