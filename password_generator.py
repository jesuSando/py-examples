import random
import string

def generate_password(cant=0, sim=0, may=0, min=0, num=0):
    password = []

    password += [random.choice(string.punctuation) for _ in range(sim)]
    password += [random.choice(string.ascii_uppercase) for _ in range(may)]
    password += [random.choice(string.ascii_lowercase) for _ in range(min)]
    password += [random.choice(string.digits) for _ in range(num)]

    faltan = cant - len(password)
    if faltan > 0:
        chars = string.ascii_letters + string.digits + string.punctuation
        password += [random.choice(chars) for _ in range(faltan)]

    random.shuffle(password)

    return ''.join(password)

def instrucciones():
    cant = int(input("Ingrese la cantidad de caracteres para la contraseña: "))
    sim = int(input("Ingrese la cantidad de caracteres especiales: "))
    may = int(input("Ingrese la cantidad de letras mayúsculas: "))
    min = int(input("Ingrese la cantidad de letras minúsculas: "))
    num = int(input("Ingrese la cantidad de números: "))
    return cant, sim, may, min, num


while True: 
    if input("¿Desea generar una contraseña? (s/n): ").lower() == 's':
        cant, sim, may, min, num = instrucciones()
        print("Contraseña generada:", generate_password(cant, sim, may, min, num))
    else:
        print("¡Hasta luego!")
        break
