import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QSpinBox, QPushButton, QVBoxLayout

# Función para mostrar la información ingresada
def mostrar_info():
    nombre = entrada_nombre.text()
    edad = spinbox_edad.value()
    etiqueta_info.setText(f"Nombre: {nombre}\nEdad: {edad} años")

# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Información Personal")
ventana.setGeometry(100, 100, 300, 200)

# Layout vertical para organizar los widgets
layout = QVBoxLayout()

# Etiqueta y campo de entrada para el nombre
etiqueta_nombre = QLabel("Ingresa tu nombre:")
entrada_nombre = QLineEdit()
layout.addWidget(etiqueta_nombre)
layout.addWidget(entrada_nombre)

# Spinbox para la selección de la edad
etiqueta_edad = QLabel("Selecciona tu edad:")
spinbox_edad = QSpinBox()
spinbox_edad.setRange(1, 100)  # Rango de 1 a 100 años
layout.addWidget(etiqueta_edad)
layout.addWidget(spinbox_edad)

# Botón para mostrar la información
boton_mostrar = QPushButton("Mostrar Información")
boton_mostrar.clicked.connect(mostrar_info)
layout.addWidget(boton_mostrar)

# Etiqueta para mostrar la información ingresada
etiqueta_info = QLabel("")
layout.addWidget(etiqueta_info)

# Configurar el layout en la ventana
ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()
sys.exit(app.exec_())

#Explicacion del programa
'''
Este programa en Python, usando PyQt5, crea una interfaz gráfica sencilla 
donde un usuario puede ingresar su nombre y seleccionar su edad. Al presionar 
un botón, la información ingresada se muestra en la ventana.
'''
#Problema que resuelve
'''
El programa facilita la captura y visualización interactiva 
de datos personales básicos (nombre y edad) mediante una interfaz 
gráfica fácil de usar, ideal para aplicaciones simples de entrada 
de datos en un entorno de escritorio.
'''