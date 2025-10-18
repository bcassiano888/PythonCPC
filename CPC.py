def tokenizador(f):
    import nltk

    from nltk.tokenize import word_tokenize

    
    t = word_tokenize(f, language='portuguese')
    return t

def subOperador(f):
    operadores = {
        'e': '^',
        'ou': 'v',
        'se': '-->',
        'então': '-->',
        'entao': '-->',
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

def treinotag():
    import nltk
    from nltk.tag import UnigramTagger
    from nltk.corpus import mac_morpho
    train_data = mac_morpho.tagged_sents()[:5000]  # 3000 sentenças do Mac-Morpho
    tagger = UnigramTagger(train_data)
    frase = "O rápido gato preto pula alegremente sobre a mesa e olha para o cachorro que dorme." 
    a = tokenizador(frase)
    tags = tagger.tag(a)
    print(tags)


treinotag()

