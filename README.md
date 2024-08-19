# Monitoramento-de-tanques-de-combust-vel
Monitoramento de tanques de combustível (IoT)
Código em Python para o projeto de monitoramento dos níveis de combustível em tanques, utilizando Raspberry Pi e a plataforma IoT ThingsBoard. Esse código faz a leitura de um sensor ultrassônico (que mede a distância do sensor à superfície do combustível, determinando assim o nível do tanque) e envia os dados para o ThingsBoard via protocolo HTTP.

**Pré-requisitos:**
1. Hardware Necessário:

- Raspberry Pi (com Raspbian OS).
- Sensor Ultrassônico (por exemplo, HC-SR04).
- Jumpers e protoboard para as conexões.

2. Bibliotecas Python Necessárias:

- RPi.GPIO: Para interfacear com os pinos GPIO do Raspberry Pi.
- requests: Para enviar dados via HTTP ao ThingsBoard.

Instalação

pip install RPi.GPIO requests
