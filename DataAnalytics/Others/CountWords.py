from collections import Counter

texto_longo =
'''
'''

pontos = ['.',',','!','?',';']

for p in pontos:
 texto_longo = texto_longo.replace(p, '')

acentos = ['á','é','í','ó','ú','à','è','ì','ò','ù',
     'ã','ẽ','ĩ','õ','ũ','â','ê','î','ô','û']
s_acentos = ['a','e','i','o','u','a','e','i','o','u',
    'a','e','i','o','u','a','e','i','o','u']

for i in range(0, len(acentos)):
 texto_longo = texto_longo.replace(acentos[i], s_acentos[i])

palavras = texto_longo.replace('\n',' ').replace('\t','').split(' ')
contador = Counter(palavras)

for i in contador.items():
    print(i)
