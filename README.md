# CUENTAS
Desarrollar un programa que conste de una clase padre **Cuenta** y dos subclases **PlazoFijo** y **CajaAhorro**.
Definir los atributos *titular* y *cantidad* que seran recibidos en el metodo \_\_init\_\_, y el método para imprimir los datos en la clase **Cuenta** (\_\_str\_\_) La salida debe ser: "Titular de la cuenta: Pedro. Cantidad: 100.0"

La clase **CajaAhorro** tendrá un método llamado **porcentajeAhorro** que recibe un monto original y devuelve el porcentaje ahorrado. ej. Si la cuenta tiene 100 de monto y el metodo recibe 500 el método debe retornar la cadena "20.0%"

La clase **PlazoFijo** tendrá dos atributos propios, *plazo* e *interés*. Tendrá un método para *obtener_importe_interes* (*cantidad* * interes / 100)
y otro método para mostrar la información (\_\_str\_\_), datos del titular, plazo, interés y total de interés. ej. "Titular: Adan. Plazo: 1mes. Interés: 0.15. Total de interés: 15"
plazo es str y interes es float

PD> CUIDE QUE LOS NOMBRES DE LAS CLASES, METODOs, ATRIBUTOS Y ARCHIVOS SEAN TAL CUAL SE INSTRUYEN, RECUERDE CLASE POR ARCHIVO, Y EL ARCHIVO NOMBRADO COMO LA CLASE

### Setup command
`sudo -H pip3 install pytest`

### Run command
Este Ejercicio tiene mas de una prueba si quieres probar por archivo especificalo en el comando
`pytest test_[el que quieras probar] ` 
