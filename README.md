# SabadoTwitterBot

Hola buenas! En este documento se explicará como funciona este bot de Twitter que quita un retweet, publica un citado y vuelve a retweetear un tweet específico en una fecha y hora determinada.

## Requerimientos y Plataforma
Primero que nada se necesita una cuenta de desarrollador en Twitter y tus respectivas claves de api. No voy a desarrollar esto porque es medio extenso, pero la documentación y pasos a seguir se puede encontrar [acá](https://developer.x.com/en) 

Este bot puede funcionar de dos maneras (que yo sepa), ejecutandolo directamente en el terminal del sistema o usando un host para que esté activo 24/7 sin necesidad de ojearlo, yo opté por el host [railway.app](railway.app) que permite hacerlo de manera gratuita

Después de hacer lo necesario ahí y linkear el repositorio correspondiente Railway necesitará dos archivos, el archivo `requirements.txt` le dice a Railway que librerías debe instalar para hacer que el código funcione, y el archivo `Procfile` le dice cual es el archivo que va a ejecutar.

Si hiciste todo correctamente, en la consola de tu aplicación en Railway debería mostrar los distintos mensajes que hay dentro del código fuente y el bot se está ejecutando sin problemas. Si tienes dudas de como funciona el flujo de la aplicación revisa el código fuente, el flujo está comentado con cada cosa que hace paso por paso. ¡Feliz Sábado!

