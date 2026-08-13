# Entidades y sensores

La integración crea sensores asociados al dispositivo Livoltek detectado.
Los nombres exactos pueden variar según el nombre de la instalación y la
versión del portal.

| Tipo de dato | Unidad | Descripción |
| --- | --- | --- |
| Estado de batería | `%` | Nivel de carga de la batería |
| Potencia de red | `kW` | Potencia importada o exportada en el punto de red |
| Potencia fotovoltaica | `kW` | Producción solar instantánea |
| Potencia de carga | `kW` | Potencia destinada a cargar la batería |
| Potencia energética | `kW` | Dato de potencia energética comunicado por el portal |
| Energía importada | `kWh` | Energía diaria importada de la red |
| Energía exportada | `kWh` | Energía diaria vertida a la red |
| Generación solar | `kWh` | Energía solar generada durante el día |

Los sensores diarios de energía están preparados para el panel Energía de
Home Assistant. La disponibilidad depende de que el portal Livoltek entregue
datos para el dispositivo y el periodo consultado.
