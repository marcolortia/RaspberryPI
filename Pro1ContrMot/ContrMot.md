#Controlador de motores a distancia

Básicamente el proyecto consiste en la elaboración de un circuito que pueda manipular un par de motores RF370C15370 a través de un Puente Doble L298, todas las instrucciones se montan sobre la Raspberry y el control remoto controlado desde un sistema con soporte de JAVA.

No es necesario que el control remoto este programado en JAVA, puede estar elaborado en cualquier otro lenguaje e incluso trabajarlo dentro de la misma Raspberry y usar el escritorio remoto en el otro dispositivo, pero se pretende que el lector identifique la forma en que se trabaja con socket, que funciona con una conexión mediante las ip de los dispositivos.  

Es bastante evidente que el lector identifique la estructura del modelo con un carro a control remoto. El uso de motores, su disposición dentro del diagrama y la interfaz del control en JAVA se pueden asociar a que la construcción de cierto vehı́culo es el objetivo principal, sin embargo el lector puede usar dicho proyecto con diversos usos. Por tanto no se mencionara acerca de algún tipo de montaje de llantas o de alguna carcasa protectora.

####Requerimientos de hardaware y librerias

	*RF370C15370 Mabuchi Original DC Motor x2
	*Controlador de motores doble puente H - L298
	*Libreria net para python
	*Libreria net para java