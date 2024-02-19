from uuid import getnode


def obtener_direccion_mac():
    mac = hex(getnode())
    mac = mac.replace("0x", "").upper()
    mac = mac.zfill(12)
    direccion_mac = ":".join(mac[i: i+2] for i in range(0, 11, 2))
    return direccion_mac


direccion_mac = obtener_direccion_mac()
print(direccion_mac)
