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
a = 'eu nao vou a praia e amanha chove'

def formato(f):
  import re
  frase = subOperador(f)
  blocos = re.split(r'\s*(\^|⭢|\bv\b)\s*', frase)
  cap = []
  for i in blocos:
    elemento = i.split()
    for j in elemento:
      passou = False
      if j == "~":
        cap.append(j+(elemento[-1][0]))
        passou = True
      if j in ['^','v','⭢']:
        cap.append(j)
        passou = True
      
      
  return cap

print(formato(a))
def treinotag():
    import nltk
    from nltk.tag import UnigramTagger
    from nltk.corpus import mac_morpho
    train_data = mac_morpho.tagged_sents()[:8000]
    tagger = UnigramTagger(train_data)
    frase = "O rápido gato preto pula alegremente sobre a mesa e olha para o cachorro que dorme."
    a = tokenizador(frase)
    tags = tagger.tag(a)
    print(tags)
treinotag()
