Title: Decoradores em Python
Author: ThiaguinhoLS
Date: 2018-07-24 01:06
Category: Python
Tags: python

## Funções ##

Pode parecer meio idiota da minha parte começar a falar de funções, mas se não entendermos como as mesmas funcionam e interagem entre si, não poderemos tirar o máximo dos decoradores. Que tal um pouco de código para nos animarmos?

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

def add(a, b):
	return a + b
```

Sei que é uma função digamos "fácil" de se entender mas começaremos com ela e evoluiremos ao longo deste artigo, você tem minha palavra. O que essa função faz é receber dois valores e retornar a soma dos mesmos, até aí nada muito difícil de assimilarmos, mas o que temos e devemos entender é que não especifico em nenhum momento que tipo de valores essa função pode ou deverá receber podendo ser _inteiro_, _float_, _string_, _list_, _tuple_, ou seja, essa função não está nem aí para de que tipo serão esses valores mas sim no que ela deve fazer com eles, que no caso seria soma-lós. Você já deve ter ouvido algum programador falando _**"Tudo em Python é objeto"**_, mas o que seria um objeto? De acordo com o _[wikipédia](https://pt.wikipedia.org/wiki/Objeto_(ci%C3%AAncia_da_computa%C3%A7%C3%A3o))_:

> Em ciência da computação, objeto é uma referência a um local da memória que 
> possui um valor. Um objeto pode ser uma variável, função, ou estrutura de 
> dados. Com a introdução da programação orientada a objetos, a palavra objeto 
> refere-se a uma instância de uma classe.
> Em programação orientada a objetos, um objeto passa a existir a partir de um 
> "molde" (classe); a classe define o comportamento do objeto, usando 
> atributos (propriedades) e métodos (ações). 

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

def decorator(func):
	def wrapper():
		nonlocal initialize
		if not initialize:
			func()
			initialize = True
	initialize = False
	return wrapper

@decorator
def once_initialize():
	print('Função inicializada')
```