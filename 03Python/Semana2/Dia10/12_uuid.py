# Importamos el módulo 'uuid' que proporciona funciones para la generación de identificadores únicos universales (UUID).

import uuid

# Generamos un UUID (identificador único universal) utilizando la función uuid4() del módulo uuid.
# Un UUID es un identificador único de 128 bits, garantizado para ser único en el espacio y tiempo.
# La función uuid4() genera un UUID aleatorio.

codigo_uuid = uuid.uuid4()

# Convertimos el UUID a una cadena (string) utilizando la función str() de Python.
# Esto nos permite representar el UUID en un formato legible de texto.

codigo_str = str(codigo_uuid)

# Imprimimos el UUID generado y su tipo de datos utilizando la función type().
# También imprimimos la cadena que representa el UUID y su tipo de datos.

print(codigo_uuid, type(codigo_uuid))
print(codigo_str, type(codigo_str))
