# A.2 - OTTO-MQTT

## Robot Otto

### Acerca del Proyecto
El proyecto propuesto consiste en implementar una interfaz web basada en Python Flask que permita al usuario controlar el robot Otto DIY mediante botones, esto involucra el desarrollo de software y hardware relacionado al movimiento del robot, pero además necesita de la implementación de un mecanismo efectivo de comunicación
entre ambas soluciones (interfaz-robot). Haciendo énfasis en éste último punto, se decidió para este proyecto implementar una comunicación bajo el protocolo MQTT utilizando el broker Mosquitto, explorando las capacidades de securización del mismo y midiendo el tiempo de respuesta que presenta al funcionar en conjunto con el broker Kafka.

El Robot Otto DIY consta de 4 motores servo y un microcontrolador NodeMCU v0.9 con integrado ESP8266.

### Bitácora del proyecto
La bitácora del proyecto se encuentra disponible en la [Wiki](https://github.com/tpII/2022-A.2-OTTO-MQTT/wiki/Bit%C3%A1cora)

### Instrucciones
* Construir la imagen de flask desde el directorio docker/flask con el comando `docker build -t compose-flask .`
* Ejecutar `docker-compose up -d` desde el directorio Docker para levantar el broker mosquitto, el servidor flask y el broker kafka
* Ingresar por consola al broker kafka y crear el topic para enviar mensajes a Otto `kafka-topics --bootstrap-server broker:9092 --create --topic otto-kafka`
