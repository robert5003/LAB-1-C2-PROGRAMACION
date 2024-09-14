import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QPushButton

# Función para mostrar los datos ingresados
def mostrar_datos():
    nombre_completo = entrada_nombre.text()
    identificacion = entrada_identificacion.text()
    tipo_identificacion = combo_tipo_identificacion.currentText()
    etiqueta_info.setText(f"Nombre: {nombre_completo}\n{tipo_identificacion}: {identificacion}")

# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Ingreso de Datos Personales")
ventana.setGeometry(100, 100, 350, 250)

# Layout para organizar los widgets
layout = QVBoxLayout()

# Etiqueta y campo de entrada para el nombre completo
etiqueta_nombre = QLabel("Ingresa tu nombre completo:")
entrada_nombre = QLineEdit()
entrada_nombre.setPlaceholderText("Nombre completo")
layout.addWidget(etiqueta_nombre)
layout.addWidget(entrada_nombre)

# Etiqueta y ComboBox para elegir entre cédula o pasaporte
etiqueta_tipo_identificacion = QLabel("Selecciona tipo de identificación:")
combo_tipo_identificacion = QComboBox()
combo_tipo_identificacion.addItems(["Cédula", "Pasaporte"])  # Opciones en el ComboBox
layout.addWidget(etiqueta_tipo_identificacion)
layout.addWidget(combo_tipo_identificacion)

# Campo de entrada para el número de cédula o pasaporte
entrada_identificacion = QLineEdit()
entrada_identificacion.setPlaceholderText("Número de identificación")
layout.addWidget(entrada_identificacion)

# Botón para mostrar los datos ingresados
boton_mostrar = QPushButton("Mostrar Datos")
boton_mostrar.clicked.connect(mostrar_datos)
layout.addWidget(boton_mostrar)

# Etiqueta para mostrar los datos ingresados
etiqueta_info = QLabel("")
layout.addWidget(etiqueta_info)

# Configurar el layout y mostrar la ventana
ventana.setLayout(layout)
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())

#Explicacion del programa
'''
Este programa, utilizando PyQt5, crea una ventana gráfica que permite 
a los usuarios ingresar su nombre completo, seleccionar el tipo de identificación 
(entre "Cédula" o "Pasaporte"), y proporcionar el número de identificación correspondiente.
Al presionar el botón "Mostrar Datos", la información ingresada se muestra en una etiqueta debajo.
'''

#Problema que resuelve
'''
Este programa resuelve el problema de recolección de datos personales de forma organizada 
y visual. Permite que los usuarios ingresen y validen fácilmente su información, 
seleccionando el tipo de identificación adecuado y visualizando los datos completos,
lo que puede ser útil en formularios de registro o aplicaciones que requieren la captura de datos personales.
'''