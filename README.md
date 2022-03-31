# Ejemplo de examen POO
Este es un ejemplo de como será el examen de POO, usando python y evaluado con pytest

### El ejercicio
Desarrolle una clase llamada PruebaExamen, dentro del archivo PruebaExamen.py
debe tener los siguientes atributos

+nombre
-apellido

y los siguientes métodos

\_\_init\_\_ que recibe nombre y apellido como parámetros 

getApellido que retorna el apellido

\_\_str\_\_ que retorna el nombre completo concatenado

PD> CUIDE QUE LOS NOMBRES DE LAS CLASES, METODOs, ATRIBUTOS Y ARCHIVOS SEAN TAL CUAL SE INSTRUYEN

### Setup command
`sudo -H pip3 install pytest`

### Run command
`pytest`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
