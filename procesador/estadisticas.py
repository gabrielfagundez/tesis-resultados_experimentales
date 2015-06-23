def mejor_mejora_greedy(data, tamano, paper, instancia, ejecucion):
  val_greedy = data[tamano]["%d"%instancia][paper]['fitness'][ejecucion][0]
  val_final = data[tamano]["%d"%instancia][paper]['fitness'][ejecucion][-1]
  diferencia = val_greedy - val_final

  mejoraGreedy = (diferencia / val_final) * 100.0

  return mejoraGreedy


def mejor_ejecucion(data, tamano, paper, instancia):
  mejor_fit = 999999999.9
  mejor = 0
  index = 1
  
  for ejec in range(1, 31):
    val_final = float(data[tamano]["%d"%instancia][paper]['fitness']["%d"%ejec][-1])
    if val_final < mejor_fit:
      mejor_fit = val_final
      mejor = index
    index = index + 1  

  return "%d"%mejor
