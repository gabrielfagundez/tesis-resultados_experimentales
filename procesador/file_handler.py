def read_file(file_ref):
  print 'D> Opening file: {0}.'.format(file_ref)
  try: 
    return open(file_ref, 'r')
  except: 
    return []