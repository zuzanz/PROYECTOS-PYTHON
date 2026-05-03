# Actividad Big Data - SmartCity Analytics

# Lista de activos
activos = [
    {"nombre": "Pagos transporte", "fuente": "Base de datos", "descripcion": "Pagos transporte", "tipo_dato": "Estructurado", "area": "Transporte", "almacenamiento": "Data Warehouse"},
    {"nombre": "Archivos XML monitoreo", "fuente": "Dispositivos", "descripcion": "XML monitoreo", "tipo_dato": "Semiestructurado", "area": "Tecnología", "almacenamiento": "NoSQL"},
    {"nombre": "Redes sociales tránsito", "fuente": "Redes sociales", "descripcion": "Opiniones", "tipo_dato": "No estructurado", "area": "Social", "almacenamiento": "Data Lake"},
    {"nombre": "Correos municipales", "fuente": "Email", "descripcion": "Mensajes", "tipo_dato": "No estructurado", "area": "Atención", "almacenamiento": "Data Lake"},
    {"nombre": "Sensores aire", "fuente": "Sensores", "descripcion": "Calidad aire", "tipo_dato": "Estructurado", "area": "Medioambiente", "almacenamiento": "Data Warehouse"},
    {"nombre": "Cámaras urbanas", "fuente": "CCTV", "descripcion": "Imágenes", "tipo_dato": "No estructurado", "area": "Seguridad", "almacenamiento": "Data Lake"},
    {"nombre": "Formularios reclamos", "fuente": "Web", "descripcion": "Datos usuarios", "tipo_dato": "Semiestructurado", "area": "Atención", "almacenamiento": "NoSQL"},
    {"nombre": "Consumo energético CSV", "fuente": "Archivo CSV", "descripcion": "Consumo", "tipo_dato": "Estructurado", "area": "Energía", "almacenamiento": "Base de datos relacional"}
]

# FUNCIÓN PARA AGREGAR DATOS
def agregar_activo(activos):
    print("\n=== AGREGAR NUEVO ACTIVO ===")
    nombre = input("Nombre: ")
    fuente = input("Fuente: ")
    descripcion = input("Descripción: ")
    tipo = input("Tipo (Estructurado / Semiestructurado / No estructurado): ")
    area = input("Área: ")
    almacenamiento = input("Almacenamiento: ")

    nuevo = {
        "nombre": nombre,
        "fuente": fuente,
        "descripcion": descripcion,
        "tipo_dato": tipo,
        "area": area,
        "almacenamiento": almacenamiento
    }

    activos.append(nuevo)
    print("✅ Activo agregado correctamente")


# MENÚ PRINCIPAL
while True:
    print("\n=== MENÚ ===")
    print("1. Mostrar activos")
    print("2. Buscar por tipo")
    print("3. Agregar activo")
    print("4. Eliminar activo")
    print("5. Modificar activo")
    print("6. Ver conteo")
    print("7. Mostrar por tipo de dato")
    print("8. Buscar por fuente (mejora)")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    # MOSTRAR
    if opcion == "1":
        for i, a in enumerate(activos):
            print(f"{i} - {a['nombre']} | {a['tipo_dato']} | {a['area']}")

    # BUSCAR POR TIPO
    elif opcion == "2":
        buscar = input("Ingrese tipo de dato: ")
        for a in activos:
            if a["tipo_dato"].lower() == buscar.lower():
                print(a["nombre"])

    # AGREGAR
    elif opcion == "3":
        agregar_activo(activos)

    # ELIMINAR
    elif opcion == "4":
        for i, a in enumerate(activos):
            print(f"{i} - {a['nombre']}")
        eliminar = int(input("Número: "))
        if 0 <= eliminar < len(activos):
            activos.pop(eliminar)

    # MODIFICAR
    elif opcion == "5":
        for i, a in enumerate(activos):
            print(f"{i} - {a['nombre']}")
        idx = int(input("Índice: "))
        campo = input("Campo: ")
        if campo in activos[idx]:
            activos[idx][campo] = input("Nuevo valor: ")

    # CONTEO
    elif opcion == "6":
        # conteo por tipo
        conteo = {"Estructurado": 0, "Semiestructurado": 0, "No estructurado": 0}
        for a in activos:
            conteo[a["tipo_dato"]] += 1

        print("\n=== CONTEO POR TIPO ===")
        for tipo, cantidad in conteo.items():
            print(f"{tipo}: {cantidad}")

        # tipo más frecuente
        mayor = max(conteo, key=conteo.get)
        print(f"Tipo más frecuente: {mayor}")

        # conteo por área
        conteo_area = {}
        for a in activos:
            area = a["area"]
            if area in conteo_area:
                conteo_area[area] += 1
            else:
                conteo_area[area] = 1

        print("\n=== CONTEO POR ÁREA ===")
        for area, cantidad in conteo_area.items():
            print(f"{area}: {cantidad}")

    # MOSTRAR POR TIPO
    elif opcion == "7":
        print("\nEstructurados:")
        for a in activos:
            if a["tipo_dato"] == "Estructurado":
                print(a["nombre"])

        print("\nSemiestructurados:")
        for a in activos:
            if a["tipo_dato"] == "Semiestructurado":
                print(a["nombre"])

        print("\nNo estructurados:")
        for a in activos:
            if a["tipo_dato"] == "No estructurado":
                print(a["nombre"])

    # MEJORA EXTRA
    elif opcion == "8":
        fuente = input("Fuente: ")
        for a in activos:
            if a["fuente"].lower() == fuente.lower():
                print(a["nombre"])

    # SALIR
    elif opcion == "9":
        print("\nConclusión:")
        print("Los datos estructurados son más fáciles de analizar.")
        print("Los no estructurados requieren más procesamiento.")
        print("El uso de Python facilita la organización de datos.")
        break