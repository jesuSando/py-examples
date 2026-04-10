def cantidad_libros(cantidad):
    personas = []
    
    for i in range(1, cantidad + 1):
        nombre = str(input(f"ingrese el nombre de la persona {i}: "))
        libros = int(input(f"ingrese la cantidad de libros para {nombre}: "))
        
        persona = {
            "id": i,
            "nombre": nombre,
            "libros": libros
        }
        
        personas.append(persona)
        
    for persona in personas:
        if persona["libros"] < 5: 
            print(f"no hay descuento para {persona['nombre']} con {persona['libros']} libros")
        elif persona["libros"] >= 5 and persona["libros"] < 10:
            print(f"{persona['nombre']} tiene un descuento del 10% con {persona['libros']} libros")
        elif persona["libros"] >= 10:
            print(f"{persona['nombre']} tiene un descuento del 15% con {persona['libros']} libros")

cantidad_libros(int(input("Ingrese la cantidad de personas: ")))