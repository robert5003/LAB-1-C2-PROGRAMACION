import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup, QMessageBox

# Función para calcular el total
def calcular_total():
    plato_seleccionado = combo_platos.currentText()
    cantidad = spinbox_cantidad.value()
    bebida_seleccionada = combo_bebidas.currentText()
    tipo_cliente = grupo_tipos.checkedButton().text()

    precios = {
        "Pizza": 8.50,
        "Hamburguesa": 6.00,
        "Ensalada": 4.50,
        "Pasta": 7.00,
        "Sopa": 3.50,
        "Agua": 1.00,
        "Refresco": 2.00,
        "Jugo": 2.50
    }

    precio_unitario_plato = precios[plato_seleccionado]
    precio_unitario_bebida = precios[bebida_seleccionada]
    total = (precio_unitario_plato + precio_unitario_bebida) * cantidad
    
    # Aplicar descuento si el cliente es VIP
    if tipo_cliente == "VIP":
        total *= 0.9  

    # Mostrar el total en un mensaje
    QMessageBox.information(ventana, "Total a Pagar", 
                            f"Plato: {plato_seleccionado}\nCantidad: {cantidad}\nBebida: {bebida_seleccionada}\nTipo de Cliente: {tipo_cliente}\nTotal a pagar: ${total:.2f}")

# Crear la aplicación y la ventana principal
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Sistema de Pedidos - Restaurante")
ventana.setGeometry(100, 100, 400, 300)

# Layout para organizar los widgets
layout = QVBoxLayout()

# Etiqueta y ComboBox para elegir el plato
etiqueta_plato = QLabel("Selecciona un plato:")
combo_platos = QComboBox()
combo_platos.addItems(["Pizza", "Hamburguesa", "Ensalada", "Pasta", "Sopa"])  
layout.addWidget(etiqueta_plato)
layout.addWidget(combo_platos)

# SpinBox para elegir la cantidad
etiqueta_cantidad = QLabel("Selecciona la cantidad:")
spinbox_cantidad = QSpinBox()
spinbox_cantidad.setRange(1, 10)  # Cantidad mínima y máxima
layout.addWidget(etiqueta_cantidad)
layout.addWidget(spinbox_cantidad)

# Etiqueta y ComboBox para elegir la bebida
etiqueta_bebida = QLabel("Selecciona una bebida:")
combo_bebidas = QComboBox()
combo_bebidas.addItems(["Agua", "Refresco", "Jugo"]) 
layout.addWidget(etiqueta_bebida)
layout.addWidget(combo_bebidas)

# Etiqueta y botones de radio para elegir el tipo de cliente
etiqueta_tipo_cliente = QLabel("Selecciona el tipo de cliente:")
layout.addWidget(etiqueta_tipo_cliente)

grupo_tipos = QButtonGroup()
radio_regular = QRadioButton("Regular")
radio_vip = QRadioButton("VIP")
radio_regular.setChecked(True)  

grupo_tipos.addButton(radio_regular)
grupo_tipos.addButton(radio_vip)

layout.addWidget(radio_regular)
layout.addWidget(radio_vip)

# Botón para calcular el total
boton_calcular = QPushButton("Calcular Total")
boton_calcular.clicked.connect(calcular_total)
layout.addWidget(boton_calcular)

# Configurar el layout en la ventana
ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()
sys.exit(app.exec_())

#Explicación del programa

'''
Este programa en PyQt5 crea una interfaz gráfica para un sistema de pedidos de un restaurante.
El usuario puede seleccionar un plato, elegir la cantidad y el tipo de cliente (regular o VIP).
Al presionar el botón "Calcular Total", se calcula el total a pagar y se muestra un mensaje con la información.
Si el cliente es VIP, se aplica un descuento del 10% al total.
'''

# Problema que resuelve

'''
Este programa facilita la gestión de pedidos de un restaurante, permitiendo a los clientes elegir el plato,
cantidad, bebida y el tipo de cliente.
Con esta interfaz, se facilita la visualización y el control de los pedidos, 
además de aplicar el descuento si el cliente es VIP.
'''