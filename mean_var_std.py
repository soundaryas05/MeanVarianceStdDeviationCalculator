import numpy as np


def calculate(input):
  if len(input) != 9:
    raise ValueError("List must contain nine numbers.")
  a = np.array(input).reshape((3, 3))
  #print(a)
  #print(a.mean(0), a.mean(1), a.mean())

  cal = dict()
  cal['mean'] = [a.mean(0).tolist(), a.mean(1).tolist(), a.mean()]
  cal['variance'] = [a.var(0).tolist(), a.var(1).tolist(), a.var()]
  cal['standard deviation'] = [a.std(0).tolist(), a.std(1).tolist(), a.std()]
  cal['max'] = [a.max(0).tolist(), a.max(1).tolist(), a.max()]
  cal['min'] = [a.min(0).tolist(), a.min(1).tolist(), a.min()]
  cal['sum'] = [a.sum(0).tolist(), a.sum(1).tolist(), a.sum()]
  return cal
