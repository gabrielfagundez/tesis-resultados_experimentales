from tabulate import tabulate
import numpy

def generar(res_greedy, res_tiempo):
  arreglo_final = []
  
  for tamano in ['chicas', 'medianas', 'grandes', 'montevideo']:
    for ev in ['Mejora Greedy', 'Tiempo']:
      for op in [1, 2, 3]:
        s_op = operacion(ev, op)
        val_clei = res(ev, op, [0], res_tiempo[tamano]['clei'])
        val_alio = res(ev, op, [0], res_tiempo[tamano]['alio'])
        
        arr = [tamano, ev, s_op, val_clei, val_alio]
        arreglo_final.append(arr)


  header = ['', '', '', 'CLEI', 'ALIO']
  print tabulate(arreglo_final, header, tablefmt="fancy_grid")

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