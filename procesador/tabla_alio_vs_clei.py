from tabulate import tabulate
import numpy
import scipy.stats

def generar(res_final):
  arreglo_final = [
    ['Instancia', 'Instancia', 'CLEI (prom +- de)', 'ALIO (prom +- de)', 'pv']
  ]

  for tamano in ['chicas', 'medianas', 'grandes', 'montevideo']:
    for ins in ['1', '2', '3', '4', '5', '6']:
      if not(tamano == 'montevideo' and ins == '5' or tamano == 'montevideo' and ins == '6'):
        # best_greedy_clei    = numpy.max(res_final[tamano][ins]['clei']['greedy'])
        # best_aleatorio_clei = numpy.max(res_final[tamano][ins]['clei']['aleatorio'])
        # best_greedy_alio    = numpy.max(res_final[tamano][ins]['alio']['greedy'])
        # best_aleatorio_alio = numpy.max(res_final[tamano][ins]['alio']['aleatorio'])

        avg_greedy_clei    = numpy.mean(res_final[tamano][ins]['clei']['greedy'])
        avg_aleatorio_clei = numpy.mean(res_final[tamano][ins]['clei']['aleatorio'])
        avg_greedy_alio    = numpy.mean(res_final[tamano][ins]['alio']['greedy'])
        avg_aleatorio_alio = numpy.mean(res_final[tamano][ins]['alio']['aleatorio'])

        de_greedy_clei    = numpy.std(res_final[tamano][ins]['clei']['greedy'])
        de_aleatorio_clei = numpy.std(res_final[tamano][ins]['clei']['aleatorio'])
        de_greedy_alio    = numpy.std(res_final[tamano][ins]['alio']['greedy'])
        de_aleatorio_alio = numpy.std(res_final[tamano][ins]['alio']['aleatorio'])

        if res_final[tamano][ins]['clei']['greedy'] == res_final[tamano][ins]['alio']['greedy']:
          kruskal = 1.0
        else:
          kruskal = scipy.stats.kruskal(res_final[tamano][ins]['clei']['greedy'], res_final[tamano][ins]['alio']['greedy'])[1]

        arr = [tamano, ins, 
                "{0} +- {1}".format(avg_greedy_clei, de_greedy_clei), 
                "{0} +- {1}".format(avg_greedy_alio, de_greedy_alio),
                kruskal
        ]
        arreglo_final.append(arr)

  print tabulate(arreglo_final, tablefmt="fancy_grid")

  return 0;
  