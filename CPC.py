def tokenizador(f):
    import nltk
    nltk.download('punkt_tab')

    from nltk.tokenize import word_tokenize

    
    t = word_tokenize(f, language='portuguese')
    return t

def subOperador(f):
    operadores = {
        'e': '^',
        'ou': 'v',
        'se': '⭢',
        'então': '⭢',
        'entao': '⭢',
        'não': '~',
        'nao': '~'
    }
    frase0 = tokenizador(f)
    frase1 = []
    for t in frase0:
        if t.lower() in operadores:
            frase1.append(operadores[t.lower()])
        else:
            frase1.append(t)
    frasef = ' '.join(frase1)
    return frasef

a =  'se vou ao cinema entao nao vou a feira e se nao vai chover entao vai fazer sol'

def formato(f):
  import re
  frase = subOperador(f)
  op = ['^','v','⭢','~']
  blocos = re.split(r'\s*(\^|⭢|\bv\b)\s*', frase)
  cap = []
  for i in blocos:
    i = i.strip()
    if not i:
        continue
    if i == '^' or i == 'v' or i == '⭢':
      cap.append(i)
    else:
      elemento = i.split()
      if '~' in elemento:
        cap.append('~'+ elemento[-1][0])
      else:
        cap.append(elemento[-1][0])
  for i in range(len(cap)):
    if cap[0] == '⭢':
      cap = cap[1:]
    if i+1 < len(cap) and (cap[i] =='v' or cap == '^') and cap[i+1] == '⭢':
      cap.remove(cap[i+1])
    
  return cap

print(formato(a))

