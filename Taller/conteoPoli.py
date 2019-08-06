

def conteoPoli(polinomio,valorX):
  res = polinomio[0];
  i = 1
  mult = 0
  for i in range(len(polinomio)):
    res = res * valorX + polinomio[i]
    mult = mult + 1
  #endfor

  return mult
#enddef

polinomio = [2,0,-3,3,-4]
valorX = -2
multiplicaciones = conteoPoli(polinomio,valorX)

print("La cantidad minima de multiplicaciones fue: ",multiplicaciones)
