# SEL0337 - Projetos em Sistemas Embarcados

Este repositório é destinado às práticas referentes à matéria SEL0337 - Projetos em Sistemas Embarcados

## Este Repositório apresenta arquivos referentes à Prática 1 (SEL0337) e à Prática 5

O foco desse documento é explicar de maneira mais detalhada a Prática 5 presente nesse repositório.

### Resumo do Funcionamento:
O projeto consiste em criar um serviço que inicia um programa .py quando a Raspberry Pi está ligando, ou seja, durante o boot da rasp sem a necessidade de realizá-lo manualmente.

### Implementação:

Foi criado o blink.service, um serviço que consistia em fazer o led piscar quando a Raspberry Pi fosse iniciada e rodasse o código de pwm.py quando fosse pedido para parar a execução do serviço. 
O vídeo abaixo mostra o funcionamento do serviço, inicialmente, foi testado de forma "manual" e não apenas quando a Raspberry Pi fosse ligada, de forma a garantir funcionamento do serviço e após isso, foi feito como descrito acima.

https://github.com/user-attachments/assets/2b9dd03a-411f-44b5-bf97-735945dac54b

