
# Convertidor de PDF a DOCX

Una aplicación de escritorio simple para convertir archivos PDF a formato DOCX, con soporte para múltiples idiomas (Español e Inglés). Utiliza PyQt5 para la interfaz gráfica y `pdf2docx` para la conversión de archivos.

## Tabla de Contenidos
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Generar Ejecutables](#generar-ejecutables)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Características
- Interfaz gráfica intuitiva.
- Soporte para dos idiomas: Español e Inglés.
- Selección de archivos PDF y directorio de salida desde la aplicación.
- Conversión rápida y eficiente de PDF a DOCX.

---

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- `PyQt5`
- `pdf2docx`

---

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/gabrielmiguelok/pdfdocx
   cd pdfdocx
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

   Si no tienes un archivo `requirements.txt`, crea uno con este contenido:
   ```
   PyQt5
   pdf2docx
   ```

---

## Uso

1. **Ejecuta la aplicación:**
   ```bash
   python pdf.py
   ```

2. **Pasos en la interfaz:**
   - Selecciona el archivo PDF que deseas convertir.
   - Elige el directorio donde guardarás el archivo convertido.
   - Haz clic en el botón "Convertir".

---

## Capturas de Pantalla

### Pantalla Principal
![Pantalla Principal](main.png "Pantalla principal de la aplicación")

### Selector de Archivos
![Selector de Archivos](filefinder.png "Selector de archivos en la aplicación")

---

## Generar Ejecutables

Puedes generar archivos ejecutables para Linux y Windows utilizando `PyInstaller`.

1. Abre una terminal y ejecuta:
   ```bash
   pyinstaller --onefile --windowed --icon=icon.png pdf.py
   ```
2. El ejecutable se generará en el directorio `dist/`.

### Notas:
- Asegúrate de reemplazar `icon.png` o `icon.ico` con el icono que desees usar.
- En Windows, instala previamente PyInstaller con:
  ```bash
  pip install pyinstaller
  ```

---

## Contribuciones

¡Contribuciones son bienvenidas! Para colaborar:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz un commit de tus cambios (`git commit -m "Añadir nueva funcionalidad"`).
4. Sube los cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
