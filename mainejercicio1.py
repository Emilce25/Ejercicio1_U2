from claseEmail import Email
@staticmethod
    
def crearCuenta(direccionCorreo):
        cuenta = Email()
        cuenta.idCuenta, _, dominio_tipo = direccionCorreo.partition("@")
        cuenta.dominio, _, cuenta.tipoDominio = dominio_tipo.partition(".")
        return cuenta


def mensaje_saludo(persona, cuenta):
      print(f"Estimado {persona}, te enviaremos tus mensajes a la dirección {cuenta.retornaEmail()}.")


def crear_cuentas_desde_archivo(nombre_archivo):
    cuentas_validas = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            direccion = linea.strip()
            cuenta = Email.crearCuenta(direccion)
            if cuenta.idCuenta and cuenta.dominio and cuenta.tipoDominio:
                cuentas_validas.append(cuenta)
            else:
                print(f"La dirección de correo electrónico {direccion} es inválida.")
    return cuentas_validas


def contar_cuentas_por_dominio(lista_cuentas, dominio):
    contador = 0
    for cuenta in lista_cuentas:
        if cuenta.dominio == dominio:
            contador += 1
    return contador

if __name__=="__main__":
 cuenta1 = Email()
 print("La dirección de correo electrónico creada es:", cuenta1.retornaEmail())
 print("El dominio de la cuenta es:", cuenta1.getDominio())
 cuenta1.cambiarPassword()
 nombre = input("Ingrese su nombre: ")
 direccion = input("Ingrese su dirección de correo electrónico: ")
 cuenta2 = Email.crearCuenta(direccion)
 mensaje_saludo(nombre, cuenta2)
 cuentas_archivo = crear_cuentas_desde_archivo("direcciones_correo.txt")
 print("Las cuentas válidas creadas son:")
 for cuenta in cuentas_archivo:
     print(cuenta.retornaEmail())
 dominio = input("Ingrese el dominio a buscar: ")
 contador_cuentas = contar_cuentas_por_dominio(cuentas_archivo, dominio)
 print(f"Se encontraron {contador_cuentas} cuentas con el dominio {dominio}.")