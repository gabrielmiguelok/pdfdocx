import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QFileDialog, QMessageBox, QHBoxLayout, QVBoxLayout, QComboBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pdf2docx import Converter

class PDFtoDOCXConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.current_language = 'es'  # Idioma predeterminado: español
        self.translations = {
            'en': {
                'window_title': 'PDF to DOCX Converter',
                'pdf_file': 'PDF File:',
                'select_pdf': 'Select the PDF file',
                'browse': 'Browse',
                'output_dir': 'Output Directory:',
                'select_output_dir': 'Select the output directory',
                'convert': 'Convert',
                'warning': 'Warning',
                'error': 'Error',
                'success': 'Success',
                'select_pdf_and_output': 'Please select the PDF file and output directory.',
                'invalid_pdf': 'The selected PDF file is not valid.',
                'invalid_output_dir': 'The selected output directory is not valid.',
                'docx_created': 'DOCX file created successfully.',
                'error_converting': 'Error converting file:',
                'select_pdf_file': 'Select PDF file',
                'select_output_directory': 'Select output directory',
                'language': 'Language:',
                'spanish': 'Spanish',
                'english': 'English'
            },
            'es': {
                'window_title': 'Convertidor de PDF a DOCX',
                'pdf_file': 'Archivo PDF:',
                'select_pdf': 'Seleccione el archivo PDF',
                'browse': 'Buscar',
                'output_dir': 'Directorio de salida:',
                'select_output_dir': 'Seleccione el directorio de salida',
                'convert': 'Convertir',
                'warning': 'Advertencia',
                'error': 'Error',
                'success': 'Éxito',
                'select_pdf_and_output': 'Por favor, seleccione el archivo PDF y el directorio de salida.',
                'invalid_pdf': 'El archivo PDF seleccionado no es válido.',
                'invalid_output_dir': 'El directorio de salida seleccionado no es válido.',
                'docx_created': 'Archivo DOCX creado con éxito.',
                'error_converting': 'Error al convertir el archivo:',
                'select_pdf_file': 'Seleccionar archivo PDF',
                'select_output_directory': 'Seleccionar directorio de salida',
                'language': 'Idioma:',
                'spanish': 'Español',
                'english': 'Inglés'
            }
        }
        self.init_ui()

    def init_ui(self):
        # Selección de idioma
        self.language_combo = QComboBox()
        self.language_combo.addItem('Español', 'es')
        self.language_combo.addItem('English', 'en')
        self.language_combo.currentIndexChanged.connect(self.change_language)

        language_label = QLabel()
        self.language_label = language_label  # Guardar referencia para actualizar el texto

        # Etiquetas y campos de entrada
        self.pdf_label = QLabel()
        self.pdf_input = QLineEdit()
        self.pdf_button = QPushButton()
        self.pdf_button.clicked.connect(self.select_pdf)

        self.output_label = QLabel()
        self.output_input = QLineEdit()
        self.output_button = QPushButton()
        self.output_button.clicked.connect(self.select_output_dir)

        # Botón de conversión
        self.convert_button = QPushButton()
        self.convert_button.clicked.connect(self.convert_file)
        self.convert_button.setStyleSheet("""
            QPushButton {
                background-color: #007ACC;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005999;
            }
        """)

        # Diseño de la interfaz
        language_layout = QHBoxLayout()
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addStretch()

        pdf_layout = QHBoxLayout()
        pdf_layout.addWidget(self.pdf_label)
        pdf_layout.addWidget(self.pdf_input)
        pdf_layout.addWidget(self.pdf_button)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_input)
        output_layout.addWidget(self.output_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(language_layout)
        main_layout.addLayout(pdf_layout)
        main_layout.addLayout(output_layout)
        main_layout.addStretch()
        main_layout.addWidget(self.convert_button, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        # Aplicar traducciones iniciales
        self.update_translations()

        # Configuraciones de la ventana
        self.setFixedSize(500, 250)
        self.setWindowIcon(QIcon("icon.png"))  # Puedes agregar un ícono personalizado

    def change_language(self):
        self.current_language = self.language_combo.currentData()
        self.update_translations()

    def update_translations(self):
        t = self.translations[self.current_language]

        self.setWindowTitle(t['window_title'])
        self.language_label.setText(t['language'])
        self.pdf_label.setText(t['pdf_file'])
        self.pdf_input.setPlaceholderText(t['select_pdf'])
        self.pdf_button.setText(t['browse'])
        self.output_label.setText(t['output_dir'])
        self.output_input.setPlaceholderText(t['select_output_dir'])
        self.output_button.setText(t['browse'])
        self.convert_button.setText(t['convert'])

        # Actualizar nombres de idiomas en el combo box sin cambiar la selección actual
        index_es = self.language_combo.findData('es')
        index_en = self.language_combo.findData('en')
        self.language_combo.setItemText(index_es, t['spanish'])
        self.language_combo.setItemText(index_en, t['english'])

    def select_pdf(self):
        t = self.translations[self.current_language]
        pdf_file, _ = QFileDialog.getOpenFileName(
            self, t['select_pdf_file'], "", "PDF Files (*.pdf)" if self.current_language == 'en' else "Archivos PDF (*.pdf)"
        )
        if pdf_file:
            self.pdf_input.setText(pdf_file)

    def select_output_dir(self):
        t = self.translations[self.current_language]
        output_dir = QFileDialog.getExistingDirectory(
            self, t['select_output_directory'], ""
        )
        if output_dir:
            self.output_input.setText(output_dir)

    def convert_file(self):
        t = self.translations[self.current_language]
        pdf_path = self.pdf_input.text()
        output_dir = self.output_input.text()

        if not pdf_path or not output_dir:
            QMessageBox.warning(self, t['warning'], t['select_pdf_and_output'])
            return

        if not os.path.isfile(pdf_path):
            QMessageBox.critical(self, t['error'], t['invalid_pdf'])
            return

        if not os.path.isdir(output_dir):
            QMessageBox.critical(self, t['error'], t['invalid_output_dir'])
            return

        docx_filename = os.path.splitext(os.path.basename(pdf_path))[0] + '.docx'
        docx_path = os.path.join(output_dir, docx_filename)

        self.pdf_to_docx(pdf_path, docx_path)

    def pdf_to_docx(self, pdf_path, docx_path):
        t = self.translations[self.current_language]
        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            QMessageBox.information(self, t['success'], t['docx_created'])
        except Exception as e:
            QMessageBox.critical(self, t['error'], f"{t['error_converting']} {e}")

def main():
    app = QApplication(sys.argv)
    converter = PDFtoDOCXConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
