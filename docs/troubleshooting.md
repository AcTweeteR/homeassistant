# Diagnóstico y solución de problemas

## El dispositivo aparece como no disponible

1. Comprueba que Home Assistant tiene acceso a Internet.
2. Verifica que la API key, el `secuid`, el user token y el Site ID siguen
   vigentes en el portal Livoltek.
3. Abre **Configuración > Dispositivos y servicios > Livoltek** y revisa los
   diagnósticos o vuelve a configurar la entrada.
4. Revisa los registros de Home Assistant buscando `custom_components.livoltek`
   y `pylivoltek`.

## Hay datos durante el día, pero no por la noche

Es normal que algunos inversores o portales dejen de entregar datos cuando el
inversor está apagado. Esta adaptación conserva el último dato válido y evita
tratar una respuesta vacía temporal como una pérdida definitiva de datos.

## El token parece haber caducado

La integración intenta renovar la sesión después de respuestas vacías
repetidas. Si el problema persiste, genera un nuevo token desde el portal y
actualiza la configuración de la integración.

## Qué adjuntar en un informe

- versión de Home Assistant;
- versión de Livoltek;
- modelo del inversor;
- fecha y hora aproximadas del fallo;
- diagnóstico descargado desde la integración;
- fragmento relevante del registro sin credenciales.

Nunca publiques API keys, tokens, contraseñas, `secuid` completos ni capturas
que los contengan.
