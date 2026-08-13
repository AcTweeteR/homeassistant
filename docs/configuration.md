# Configuración de Livoltek

La configuración se realiza desde la interfaz de Home Assistant. No es
necesario editar `configuration.yaml`.

## Datos necesarios

El portal de Livoltek debe proporcionar:

| Campo | Uso |
| --- | --- |
| API key | Autenticación de la API cloud |
| `secuid` | Identificador de usuario o sesión del portal |
| User token | Token asociado a la cuenta |
| Site ID | Identificador de la instalación que se consultará |

En **Configuración > Dispositivos y servicios**, añade la integración Livoltek
y completa los campos solicitados. La integración crea un dispositivo por
instalación y consulta sus datos periódicamente.

## Comportamiento esperado

- La consulta utiliza cloud polling con un intervalo aproximado de 2 minutos y
  30 segundos.
- Si el portal devuelve una respuesta vacía durante la noche o mientras el
  inversor está apagado, se conserva el último valor válido cuando es posible.
- Si la sesión cloud caduca y el portal devuelve listas vacías repetidas, se
  intenta renovar el token antes de marcar el dispositivo como no disponible.
- Los sensores de energía diaria se publican como `total_increasing` para que
  Home Assistant pueda utilizarlos en el panel Energía.
