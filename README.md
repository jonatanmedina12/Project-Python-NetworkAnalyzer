# Escáner de Red

Este proyecto es un escáner de red simple pero potente escrito en Python. Permite a los usuarios escanear una red especificada en busca de hosts activos en puertos específicos.

## Características

- Escaneo de redes IPv4
- Escaneo de puertos múltiples
- Visualización de progreso con barras de progreso
- Resultados formateados en una tabla legible

## Requisitos

- Python 3.6+
- Bibliotecas requeridas:
  - `socket`
  - `ipaddress`
  - `concurrent.futures`
  - `tqdm`
  - `rich`

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/jonatanmedina12/Project-Python-NetworkAnalyzer.git
   ```
2. Navega al directorio del proyecto:
   ```
   cd Project-Python-NetworkAnalyzer
   ```
3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para usar el escáner de red, ejecuta el script `main.py`:

```
python main.py
```

Por defecto, el script escaneará la red 192.168.1.0/24 en los puertos 80 (HTTP) y 443 (HTTPS). Puedes modificar estos valores en el script según tus necesidades.

## Advertencia

El uso de este escáner de red debe cumplir con todas las leyes y regulaciones aplicables. Asegúrate de tener permiso antes de escanear cualquier red que no sea de tu propiedad.

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos antes de hacer un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.