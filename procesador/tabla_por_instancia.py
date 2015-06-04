from tabulate import tabulate
import numpy

def generar(res_greedy, res_tiempo):
  arreglo_final_chicas = []
  arreglo_final_medianas = []
  arreglo_final_grandes = []
  arreglo_final_montevideo = []
  
  for tamano in ['chicas', 'medianas', 'grandes', 'montevideo']:
    for ins in ['1', '2', '3', '4', '5', '6']:
      for ev in ['Mejora Greedy', 'Tiempo']:
        for op in [1, 2, 3]:
          if not(tamano == 'montevideo' and ins == '5' or tamano == 'montevideo' and ins == '6'):
            s_op = operacion(ev, op)
            val_clei = res(ev, op, res_greedy[tamano][ins]['alio'], res_tiempo[tamano][ins]['clei'])
            val_alio = res(ev, op, res_greedy[tamano][ins]['alio'], res_tiempo[tamano][ins]['alio'])
            
            arr = [tamano, ins, ev, s_op, val_clei, val_alio]
            if tamano == 'chicas':
              arreglo_final_chicas.append(arr)
            if tamano == 'medianas':
              arreglo_final_medianas.append(arr)
            if tamano == 'grandes':
              arreglo_final_grandes.append(arr)
            if tamano == 'montevideo':  
              arreglo_final_montevideo.append(arr)


  header = ['Chicas', 'Instancia', '', '', 'CLEI', 'ALIO']
  print tabulate(arreglo_final_chicas, header, tablefmt="latex")
  
  header = ['Medianas', 'Instancia', '', '', 'CLEI', 'ALIO']
  print tabulate(arreglo_final_medianas, header, tablefmt="latex")
  
  header = ['Grandes', 'Instancia', '', '', 'CLEI', 'ALIO']
  print tabulate(arreglo_final_grandes, header, tablefmt="latex")
  
  header = ['Montevideo', 'Instancia', '', '', 'CLEI', 'ALIO']
  print tabulate(arreglo_final_montevideo, header, tablefmt="latex")

  return ''


def operacion(ev, index):
  if ev == 'Mejora Greedy':
    if index == 1:
      return 'Maxima Mejora'
    if index == 2:
      return 'Mejora Promedio'
    if index == 3:
      return 'Desviacion Estandar'
  if ev == 'Tiempo':
    if index == 1:
      return 'Minimo'
    if index == 2:
      return 'Promedio'
    if index == 3:
      return 'Desviacion Estandar'

def res(ev, index, arrGreedy, arrTiempo):
  if ev == 'Mejora Greedy':
    if index == 1:
      return numpy.max(arrGreedy)
    if index == 2:
      return numpy.mean(arrGreedy)
    if index == 3:
      return numpy.std(arrGreedy)
  if ev == 'Tiempo':
    if index == 1:
      return numpy.min(arrTiempo)
    if index == 2:
      return numpy.mean(arrTiempo)
    if index == 3:
      return numpy.std(arrTiempo)