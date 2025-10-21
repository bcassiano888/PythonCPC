def cpc(f):
    def tokenizador(f):
        import nltk
        nltk.download('punkt_tab', quiet=True)
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

    def formato(f):
        import re
        import nltk
        from nltk.corpus import stopwords
        nltk.download('stopwords')
        stop_words = stopwords.words('portuguese')
        stop_words.append('apenas')

        frase = subOperador(f)
        op = ['^', 'v', '⭢', '~']
        blocos = re.split(r'\s*(\^|⭢|\bv\b)\s*', frase)
        cap = []
        for i in blocos:
            i = i.strip()
            if not i:
                continue
            if i in op:
                cap.append(i)
            else:
                elemento = i.split()
                if '~' in elemento:
                    if elemento[-1] in stop_words:
                        cap.append('~' + elemento[-2][0].upper())
                    else:
                        cap.append('~' + elemento[-1][0].upper())
                else:
                    if elemento[-1] in stop_words:
                        cap.append(elemento[-2][0].upper())
                    else:
                        cap.append(elemento[-1][0].upper())
        fm = []
        cont = 0
        for i in cap:
            if cont == 0 and i == '⭢':
                None
            elif i == '⭢' and cap[cont - 1] in ['^', 'v']:
                None
            else:
                fm.append(i)
            cont += 1
        final = ' '.join(fm)
        return final

    # Check for the occurrence of "se" and absence of "então" or "entao"
    if f.count("se") == 1 and "então" not in f and "entao" not in f:
        # Split the sentence into two parts
        parts = f.split("se")
        p1 = parts[0].strip()
        p2 = parts[1].strip()
        # Invert the propositions
        inverted = f"{p2} se {p1}"
        z = formato(inverted)
    else:
        z = formato(f)

    fr = '\nfrase: ' + f
    return z + fr

a = input("Enter a sentence: ")
print(cpc(a))
