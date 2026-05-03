# Actividad 1.3: Consulta y organización de activos de información en Python

# Lista base de activos
activos = [
    {
        "nombre": "Pagos del transporte público",
        "fuente": "Base de datos relacional",
        "descripcion": "Registro de pagos por tarjeta, fecha y recorrido",
        "tipo_dato": "Estructurado",
        "area": "Movilidad"
    },
    {
        "nombre": "Archivos XML de monitoreo",
        "fuente": "Archivo XML",
        "descripcion": "Datos de monitoreo urbano",
        "tipo_dato": "Semiestructurado",
        "area": "Infraestructura"
    },
    {
        "nombre": "Publicaciones ciudadanas",
        "fuente": "Redes sociales",
        "descripcion": "Opiniones sobre tránsito",
        "tipo_dato": "No estructurado",
        "area": "Participación ciudadana"
    },
    {
        "nombre": "Correos a atención municipal",
        "fuente": "Correo electrónico",
        "descripcion": "Consultas y reclamos",
        "tipo_dato": "Semiestructurado",
        "area": "Atención ciudadana"
    },
    {
        "nombre": "Sensores de calidad del aire",
        "fuente": "Sensores",
        "descripcion": "Mediciones ambientales",
        "tipo_dato": "Estructurado",
        "area": "Medio ambiente"
    },
    {
        "nombre": "Imágenes de cámaras urbanas",
        "fuente": "CCTV",
        "descripcion": "Monitoreo visual",
        "tipo_dato": "No estructurado",
        "area": "Seguridad"
    },
    {
        "nombre": "Formularios web de reclamos",
        "fuente": "Portal web",
        "descripcion": "Datos ingresados por usuarios",
        "tipo_dato": "Estructurado",
        "area": "Atención ciudadana"
    },
    {
        "nombre": "Consumo energético por sector",
        "fuente": "Archivo CSV",
        "descripcion": "Consumo eléctrico por zona",
        "tipo_dato": "Estructurado",
        "area": "Energía"
    }
]

# ===============================
# AGREGAR NUEVO ACTIVO
# ===============================
respuesta = input("¿Desea ingresar un nuevo activo? (si/no): ")

if respuesta.lower() == "si":
    nombre = input("Nombre: ")
    fuente = input("Fuente: ")
    descripcion = input("Descripción: ")
    tipo = input("Tipo (Estructurado / Semiestructurado / No estructurado): ")
    area = input("Área: ")

    nuevo = {
        "nombre": nombre,
        "fuente": fuente,
        "descripcion": descripcion,
        "tipo_dato": tipo,
        "area": area
    }

    activos.append(nuevo)
    print("\n✅ Activo agregado correctamente\n")
else:
    print("\nNo se agregó ningún activo\n")

# ===============================
# MOSTRAR ACTIVOS
# ===============================
print("=== ACTIVOS DE INFORMACIÓN ===")
for activo in activos:
    print(f"- {activo['nombre']} | {activo['tipo_dato']} | {activo['area']}")

# ===============================
# CONTEO POR TIPO
# ===============================
conteo = {
    "Estructurado": 0,
    "Semiestructurado": 0,
    "No estructurado": 0
}

for activo in activos:
    conteo[activo["tipo_dato"]] += 1

print("\n=== CANTIDAD POR TIPO ===")
for tipo, cantidad in conteo.items():
    print(f"{tipo}: {cantidad}")

# ===============================
# TIPO MÁS FRECUENTE (CON EMPATE)
# ===============================
maximo = max(conteo.values())
tipos_mayores = []

for tipo, cantidad in conteo.items():
    if cantidad == maximo:
        tipos_mayores.append(tipo)

if len(tipos_mayores) == 1:
    print(f"\nTipo más frecuente: {tipos_mayores[0]}")
else:
    print(f"\nEmpate entre: {', '.join(tipos_mayores)}")

# ===============================
# MOSTRAR POR CATEGORÍA
# ===============================
print("\n=== ESTRUCTURADOS ===")
for activo in activos:
    if activo["tipo_dato"] == "Estructurado":
        print("-", activo["nombre"])

print("\n=== SEMIESTRUCTURADOS ===")
for activo in activos:
    if activo["tipo_dato"] == "Semiestructurado":
        print("-", activo["nombre"])

print("\n=== NO ESTRUCTURADOS ===")
for activo in activos:
    if activo["tipo_dato"] == "No estructurado":
        print("-", activo["nombre"])

# ===============================
# BÚSQUEDA POR TIPO
# ===============================
print("\n=== BÚSQUEDA POR TIPO ===")
busqueda = input("Ingrese tipo de dato: ")

encontrado = False
for activo in activos:
    if activo["tipo_dato"].lower() == busqueda.lower():
        print("-", activo["nombre"], "|", activo["area"])
        encontrado = True

if not encontrado:
    print("No se encontraron resultados")

# ===============================
# CONTEO POR ÁREA
# ===============================
print("\n=== CONTEO POR ÁREA ===")
conteo_area = {}

for activo in activos:
    area = activo["area"]
    if area in conteo_area:
        conteo_area[area] += 1
    else:
        conteo_area[area] = 1

for area, cantidad in conteo_area.items():
    print(f"{area}: {cantidad}")

# ===============================
# MEJORA: RECOMENDACIÓN
# ===============================
print("\n=== RECOMENDACIÓN DE HERRAMIENTAS ===")

for activo in activos:
    if activo["tipo_dato"] == "Estructurado":
        herramienta = "SQL, Excel o Power BI"
    elif activo["tipo_dato"] == "Semiestructurado":
        herramienta = "Python o MongoDB"
    else:
        herramienta = "Python, NLP o análisis de imágenes"

    print(f"- {activo['nombre']} → {herramienta}")

# ===============================
# CONCLUSIÓN
# ===============================
print("\n=== CONCLUSIÓN ===")
print("El programa permite organizar, buscar y analizar activos de información.")
print("Los datos estructurados son más fáciles de analizar.")
print("Python facilita el manejo inicial de datos en Big Data.")