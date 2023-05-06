class Email:
    __idCuenta= ""
    __dominio= ""
    __tipoDominio=""
    __contraseña=""
    def __init__(self):
        self.idCuenta = input("Ingrese su ID de cuenta: ")
        self.dominio = input("Ingrese el dominio: ")
        self.tipoDominio = input("Ingrese el tipo de dominio: ")
        self.password = input("Ingrese su contraseña: ")
    
    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDominio}"
    
    def getDominio(self):
        return self.dominio
    
    def cambiarPassword(self):
        password_actual = input("Ingrese la contraseña actual: ")
        if password_actual != self.password:
            print("Contraseña incorrecta")
            return
        nueva_password = input("Ingrese la nueva contraseña: ")
        self.password = nueva_password
        print("Contraseña modificada con éxito")