# EcoAprende (Flask)

## Pasos para crear el proyecto desde cero
1. Crear carpeta del proyecto y un entorno virtual.
2. Instalar Flask.
3. Crear la estructura de carpetas con `templates/` y `static/`.
4. Definir rutas en `app.py`.
5. Agregar vistas HTML con Bootstrap y migas de pan.
6. Agregar estilos e imágenes en `static/`.

## Estructura del proyecto
```
backend-ambiente/
  app.py
  requirements.txt
  templates/
    base.html
    index.html
    importancia.html
    sga.html
    futuro.html
    tres-r.html
  static/
    css/
      styles.css
    images/
      hero.svg
      overview.svg
      importancia.svg
      sga.svg
      futuro.svg
      tres-r.svg
```

## Cómo ejecutar
1. Crear entorno virtual y activarlo.
2. Instalar dependencias:
   - `pip install -r requirements.txt`
3. Ejecutar la app:
   - `python app.py`
4. Abrir `http://127.0.0.1:5000` en el navegador.
