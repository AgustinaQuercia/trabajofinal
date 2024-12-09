import pickle
import random

TICKET_FILE = "tickets.pkl"

try:
    with open(TICKET_FILE, "rb") as file:
        tickets = pickle.load(file)
except (FileNotFoundError, EOFError):
    tickets = {}
def guardar_tickets():
    """Guarda los tickets en un archivo usando pickle."""
    with open(TICKET_FILE, "wb") as file:
        pickle.dump(tickets, file)

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            salir()
        else:
            print("Opción inválida. Intente de nuevo.")

def alta_ticket():
    while True:
        print("\n--- ALTA DE TICKET ---")
        descripcion = input("Ingrese la descripción del ticket: ")
        nombre = input("Ingrese nombre: ")
        sector = input("Ingrese sector: ")
        asunto = input("Ingrese asunto: ")
        problema = input("Ingrese problema: ")
    
        numero_ticket = random.randint(1000, 9999)
        while numero_ticket in tickets: 
            numero_ticket = random.randint(1000, 9999)

        tickets[numero_ticket] = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema,
            "descripcion": descripcion
        }
        
        guardar_tickets() 
        
        print("\nTicket creado exitosamente.")
        print(f"Número de Ticket: {numero_ticket}")
        print("** Por favor, recuerde el número del ticket. **")
        
        otra_vez = input("\n¿Desea crear otro ticket? (s/n): ").lower()
        if otra_vez != 's':
            break

def leer_ticket():
    while True:
        print("\n--- LECTURA DE TICKET ---")
        try:
            numero_ticket = int(input("Ingrese el número del ticket: "))
            if numero_ticket in tickets:
                print("\nTicket encontrado:")
                print(f"Número de Ticket: {numero_ticket}")
                for key, value in tickets[numero_ticket].items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print("No se encontró ningún ticket con ese número.")
        except ValueError:
            print("Número de ticket inválido. Intente de nuevo.")
        
        otra_vez = input("\n¿Desea leer otro ticket? (s/n): ").lower()
        if otra_vez != 's':
            break

def salir():
    confirmacion = input("\n¿Está seguro de que desea salir? (s/n): ").lower()
    if confirmacion == 's':
        print("¡Gracias por usar el sistema! Hasta luego.")
        exit()

if __name__ == "__main__":
    menu_principal()