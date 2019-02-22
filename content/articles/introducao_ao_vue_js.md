Title: Introdução ao Vue.js
Author: ThiaguinhoLS
Date: 2019-02-22 15:12
Category: Framework
Tags: Vue

## O que é Vue.js ##

O Vue.js é um framework progressivo desenvolvido para auxiliar o desenvolvedor
na criação de interfaces de usuário, isso mesmo Vue.js é um framework logo
existem situações onde o mesmo deve e não ser usado.

Vamos a um exemplo básico, mas que demonstra um pouco do poder desse framework:

```html

<div id="app">
  {{ message  }}
</div>

````


```javascript

const app = new Vue({
  el: '#app',
  data: {
    message: 'Hello World with Vue.js'
  }
});

```


