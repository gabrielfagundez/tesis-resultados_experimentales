import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

def generar(data):
  for tamano in ['chicas', 'medianas', 'grandes', 'montevideo']:
    for ins in ['1', '2', '3', '4', '5', '6']:     
      if not(tamano == 'montevideo' and ins == '5' or tamano == 'montevideo' and ins == '6'):
        print 'D> Ploteando CLEI..'
        print data[tamano][ins]['clei']['tiempo']['1']
        print data[tamano][ins]['clei']['fitness']['1']

        print 'D> Ploteando ALIO..'
        print data[tamano][ins]['alio']['tiempo']['1']
        print data[tamano][ins]['alio']['fitness']['1']

        # Dibujo la grafica
        plt1, = plt.plot(data[tamano][ins]['clei']['tiempo']['1'], data[tamano][ins]['clei']['fitness']['1'], 'ro')
        plt.plot(data[tamano][ins]['clei']['tiempo']['1'], data[tamano][ins]['clei']['fitness']['1'], 'k--')
        
        plt2, = plt.plot(data[tamano][ins]['alio']['tiempo']['1'], data[tamano][ins]['alio']['fitness']['1'], 'bo')
        plt.plot(data[tamano][ins]['alio']['tiempo']['1'], data[tamano][ins]['alio']['fitness']['1'], 'k--')

        plt.ylabel('fitness')
        plt.xlabel('tiempo (s)')
        plt.legend([plt1, plt2], ['seqEA', u'p\u03bcEA'])

        # Guardo una imagen
        name = "fitness_over_time/{0}_{1}.pdf".format(tamano, ins)
        pylab.savefig(name)

        # Limpio la figura
        plt.clf()

  return 0