import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QVBoxLayout, QPushButton, QButtonGroup

# Función para validar y mostrar la clave ingresada según el tipo seleccionado
def mostrar_clave():
    clave_ingresada = entrada_clave.text()
    tipo_clave = grupo_tipos.checkedButton().text()

    if tipo_clave == "Solo numérica" and not clave_ingresada.isdigit():
        etiqueta_info.setText("Error: Solo se permiten números.")
    elif tipo_clave == "Solo texto" and not clave_ingresada.isalpha():
        etiqueta_info.setText("Error: Solo se permiten letras.")
    elif tipo_clave == "Letras y números" and not clave_ingresada.isalnum():
        etiqueta_info.setText("Error: Solo se permiten letras y números.")
    else:
        etiqueta_info.setText(f"Clave ingresada: {clave_ingresada}")

# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Ingreso de Clave Secreta")
ventana.setGeometry(100, 100, 300, 250)

# Layout para organizar los widgets
layout = QVBoxLayout()

# Etiqueta y campo de entrada para la clave secreta
etiqueta_clave = QLabel("Ingresa tu clave secreta:")
entrada_clave = QLineEdit()
entrada_clave.setEchoMode(QLineEdit.Password)  # Ocultar los caracteres
layout.addWidget(etiqueta_clave)
layout.addWidget(entrada_clave)

# Etiqueta y botones de radio para elegir el tipo de clave
etiqueta_tipo = QLabel("Elige el tipo de clave:")
layout.addWidget(etiqueta_tipo)

# Crear grupo de botones de radiobox
grupo_tipos = QButtonGroup()

radio_numerica = QRadioButton("Solo numérica")
radio_texto = QRadioButton("Solo texto")
radio_ambas = QRadioButton("Letras y números")
radio_ambas.setChecked(True)  # Valor predeterminado

grupo_tipos.addButton(radio_numerica)
grupo_tipos.addButton(radio_texto)
grupo_tipos.addButton(radio_ambas)

layout.addWidget(radio_numerica)
layout.addWidget(radio_texto)
layout.addWidget(radio_ambas)

# Botón para mostrar la clave ingresada
boton_mostrar = QPushButton("Mostrar Clave")
boton_mostrar.clicked.connect(mostrar_clave)
layout.addWidget(boton_mostrar)

# Etiqueta para mostrar la clave ingresada o los errores
etiqueta_info = QLabel("")
layout.addWidget(etiqueta_info)

# Configurar el layout y mostrar la ventana
ventana.setLayout(layout)
ventana.show()

# Ejecutar la aplicación
sys.exit(app.exec_())


#Explicacion del programa

'''
Este programa en PyQt5 crea una interfaz gráfica para ingresar una "clave secreta".
El usuario puede elegir entre tres tipos de clave: solo numérica, solo texto, o letras 
y números. Al ingresar la clave, el programa valida el tipo de caracteres permitidos 
según la opción seleccionada y muestra un mensaje de error o la clave ingresada.
'''

#Problema que resuelve 

'''
Este programa ayuda a validar la entrada de claves secretas según diferentes criterios, 
asegurando que el formato de la clave cumpla con las restricciones seleccionadas por el usuario 
(números, letras o ambos), lo que es útil en situaciones que requieren control sobre los tipos 
de datos ingresados, como en sistemas de seguridad o formularios.
'''