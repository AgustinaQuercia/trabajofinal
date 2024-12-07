import secrets
import string

def cont_letras():
    length = int(input("¿De cuántos caracteres quieres la contraseña? "))
    alphabet = string.ascii_letters
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(f"Tu contraseña generada es: {password}")

def cont_numeros():
    length = int(input("¿De cuántos caracteres quieres la contraseña? "))
    digits = string.digits
    password = ''.join(secrets.choice(digits) for _ in range(length))
    print(f"Tu contraseña generada es: {password}")

def cont_letrasnumeros():
    length = int(input("¿De cuántos caracteres quieres la contraseña? "))
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(f"Tu contraseña generada es: {password}")

def cont_letrasnumeroscaracteres():
    length = int(input("¿De cuántos caracteres quieres la contraseña? "))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(f"Tu contraseña generada es: {password}")

def salir():
    print("Gracias por usar el generador de contraseñas.")
    exit()


def menu_principal():
    while True:
        print("\n--- BIENVENIDO AL GENERADOR DE CONTRASEÑAS: VO.1 ---")
        print("\nSeleccione una de las siguientes opciones:")
        print("\n1. Generar contraseña solo de letras.")
        print("2. Generar contraseña solo de números.")
        print("3. Generar contraseña de letras y números.")
        print("4. Generar contraseña de letras, números y caracteres.")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cont_letras()
        elif opcion == "2":
            cont_numeros()
        elif opcion == "3":
            cont_letrasnumeros()
        elif opcion == "4":
            cont_letrasnumeroscaracteres()
        elif opcion == "0":
            salir()
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()