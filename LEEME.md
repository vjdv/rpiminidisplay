# Mini Display para Raspberry Pi

Muestra información útil en un pequeño display OLED de 128x64 conectado a una Raspberry Pi sin periféricos conectados.

## El problema a solucionar

Estoy usando una Raspberry Pi 4 como servidor de desarrollo el cual llevo de la casa al trabajo o incluso durante viajes. La conecto a diferentes redes y no siempre obtengo la misma IP. Si no sé qué IP tengo, entonces: ¿Cómo me conecto a ella? Solución: Conecta una mini pantalla OLED donde puedas ver la IP asignada.

¡Bien! Pero tampoco me gusta apagarla solo desconectando el cable de alimentación. Solución: agrega un botón físico que te permita apagarla (o conéctate por SSH a ella y ejecuta el comando adecuado, pero es más tedioso).

## Características

- Conoce tu IP asignada
- Apagado limpio

## Extras

- Muestra estadísticas del sistema (CPU, RAM, temperatura)
- Hora actual

## Instrucciones

Conecta un minidisplay OLED a tu Raspberry Pi y ejecuta los siguientes comandos:

```bash
#clona el repo
git clone https://github.com/vjdv/rpiminidisplay.git
#entra al directorio descargado
cd rpiminidisplay
#Ejecuta el script para instalar dependencias
./install.sh
#Ejecuta
python3 display.py
```
