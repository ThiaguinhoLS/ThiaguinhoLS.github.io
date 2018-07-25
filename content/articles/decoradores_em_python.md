Title: Decoradores em Python
Author: ThiaguinhoLS
Date: 2018-07-24 01:06
Category: Python
Tags: python

## O que são decoradores? ##

Um _decorador_ nada mais é do que uma função/método ou qualquer objeto _Callable_ que recebe como argumento um objeto que também seja um _Callable_ acrescentando ao mesmo alguma funcionalidade, fazendo alguma verificação, ou qualquer coisa que você ache que deva fazer antes de realmente chamar a função em si. Vamos ver um pouco de código.

```python
def add(a, b):
	return a + b

def sub(a, b):
	return a - b
```

Digamos que queremos implementar um sistema de log nessas funções faríamos assim:

```python
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def add(a, b):
	logger.debug('Função add chamada')
	return a + b

def sub(a, b):
	logger.debug('Função sub chamada')
	return a - b

```

Acrescentamos log somente a nível de depuração nas duas funções até aí nada de mais mas e se criamos as funções _div_, _mul_, ou outras? Teríamos duplicação de código em todas elas, então qual seria a melhor abordagem aqui? Se você respondeu decoradores acertou em cheio. Com o uso de decoradores podemos extrair a funcionalidade comum e deixá-la a cargo do decorador, enquanto a parte variante inplementamos na própria função.

```python
import logging

logger = logging.getLogger()

def decorator(func):
	def wrapper(a, b):
		logger.debug('Função {} chamada'.format(func.__name__))
	return wrapper

@decorator
def add(a, b):
	return a + b

@decorator
def sub(a, b):
	return a - b
``` 

Agora não importa quantas funções eu queira adicionar a funcionalidade do log, somente preciso utilizar meu decorador e pronto, a mesma agora possui essa funcionalidade.

Vamos fazer algumas verificações nesse código.
```python
>>> add
<function decorator.<locals>.wrapper at 0x7f259e64d9d8>
>>> add.__name__
'wrapper'

```
Pelo que podemos ver a função decorada perdeu digamos assim sua _"identidade"_, mas se olharmos novamente nosso código poderemos rapidamente descobrir o motivo não é mesmo? O motivo é que quando decoramos a função estamos chamando o decorador e passando como argumento essa função da seguinte forma:

```python
add = decorator(add) # O mesmo que utilizar @decorator acima da definição da função

```

A função _decorator_ está sendo executada com o parâmetro _func_ sendo a função _add_, depois o decorador define um função aninhada(interna) chamada _wrapper_, e retorna a mesma, ou seja, a função retornada não é a mesma que foi decorada mas sim um invólucro. Um meio de contornar a perda desses atributos, caso você necessite deles para realizar introspecção, ou qualquer que seja o motivo é utilizar a função _[wraps](https://docs.python.org/3/library/functools.html#functools.wraps){:target="_blank"}_ que acreditem ou não é um decorador.

```python
from functools import wraps

def decorator(func):
	@wraps(func)
	def wrapper(a, b):
		return func(a, b)
	return wrapper

```

Agora se fizermos:

```python
>>> add = decorator(add)
>>> add
<function add at 0x7f125611dae8>
>>> add.__name__
'add'

```

Espero ter ajudado nem mesmo que seja um pouco no seu entendimento sobre decoradores, qualquer dúvida deixe nos comentários que tentarei responde-lá da melhor forma possível.

