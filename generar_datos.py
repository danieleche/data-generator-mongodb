import json
import random
from datetime import datetime, timedelta

cursos = ["Bases de Datos II", "Ingeniería de Software", "Matemática Discreta", "Estructuras de Datos", "Sistemas Operativos"]
docentes = ["Dra. Pérez", "Prof. Gómez", "Ing. Rodríguez", "Lic. Martínez", "Dr. Fernández"]
fortalezas_opt = ["pensamiento crítico", "trabajo en equipo", "liderazgo", "proactividad", "comunicación", "análisis de datos"]
debilidades_opt = ["gestión del tiempo", "distracción", "falta de participación", "nerviosismo en exposiciones", "redacción técnica"]
etiquetas_opt = ["participación", "rendimiento alto", "rezago", "mejora continua", "excelencia", "riesgo de abandono"]
tipos_intervencion = ["tutoría", "asesoría psicológica", "plan de nivelación", "citación representante"]
resultados_inter = ["mejora sostenida", "en proceso", "sin cambios", "excelente avance"]
estilos_aprend = ["visual", "auditivo", "kinestésico", "lectura/escritura", "multimodal"]

def generar_fecha():
    inicio = datetime(2025, 1, 1)
    fin = datetime(2026, 6, 1)
    fecha_aleatoria = inicio + timedelta(days=random.randint(0, (fin - inicio).days))
    return fecha_aleatoria.strftime("%Y-%m-%d")

colecciones = {
    "Registro_desempeño_detallado": [],
    "Retroalimentacion_cualitativa": [],
    "Historial_intervenciones": [],
    "Evidencias_aprendizaje": [],
    "Perfil_academico_dinamico": []
}

for i in range(1, 201):
    id_est = random.randint(1, 220) 

    colecciones["Registro_desempeño_detallado"].append({
        "_id": f"RD-{i}", 
        "id_estudiante": id_est,
        "periodo": random.choice(["2025-1", "2025-2", "2026-1"]),
        "indicadores": {
            "promedio_general": round(random.uniform(2.5, 5.0), 1),
            "nivel_riesgo": random.choice(["bajo", "medio", "alto"]),
            "asistencia": random.randint(60, 100)
        },
        "fortalezas": random.sample(fortalezas_opt, random.randint(1, 3)),
        "debilidades": random.sample(debilidades_opt, random.randint(1, 2)),
        "observaciones": [{
            "docente": random.choice(docentes),
            "comentario": "Muestra evolución en su rendimiento." if random.random() > 0.5 else "Debe mejorar su enfoque.",
            "fecha": generar_fecha()
        }]
    })

    colecciones["Retroalimentacion_cualitativa"].append({
        "_id": f"RC-{i}",
        "id_estudiante": id_est,
        "curso": random.choice(cursos),
        "tipo": random.choice(["docente", "compañero", "autoevaluación"]),
        "comentarios": [{
            "autor": random.choice(docentes),
            "mensaje": "Gran aporte durante las sesiones prácticas.",
            "fecha": generar_fecha()
        }],
        "etiquetas": random.sample(etiquetas_opt, random.randint(1, 3))
    })

    colecciones["Historial_intervenciones"].append({
        "_id": f"HI-{i}",
        "id_estudiante": id_est,
        "intervenciones": [{
            "tipo": random.choice(tipos_intervencion),
            "motivo": random.choice(["riesgo académico", "inasistencias", "problemas de conducta", "solicitud propia"]),
            "resultado": random.choice(resultados_inter),
            "fecha": generar_fecha()
        }],
        "responsable": "Coordinación académica"
    })

    colecciones["Evidencias_aprendizaje"].append({
        "_id": f"EA-{i}",
        "id_estudiante": id_est,
        "curso": random.choice(cursos),
        "evidencias": [{
            "tipo": random.choice(["proyecto", "ensayo", "repositorio_codigo", "presentacion"]),
            "titulo": f"Trabajo final de {random.choice(cursos)}",
            "url": f"https://repositorio.edu/evidencia/{id_est}/{i}",
            "calificacion": round(random.uniform(3.0, 5.0), 1)
        }],
        "fecha_registro": generar_fecha()
    })

    colecciones["Perfil_academico_dinamico"].append({
        "_id": f"PA-{i}",
        "id_estudiante": id_est,
        "estilo_aprendizaje": random.choice(estilos_aprend),
        "competencias_destacadas": random.sample(fortalezas_opt, random.randint(1, 3)),
        "nivel_autonomia": random.choice(["bajo", "medio", "alto"]),
        "recomendaciones": random.sample([
            "participar en proyectos de investigación",
            "optar por cursos avanzados",
            "unirse a grupos de estudio",
            "mejorar control de tiempos de entrega"
        ], 2),
        "ultima_actualizacion": generar_fecha()
    })

for nombre_coleccion, datos in colecciones.items():
    nombre_archivo = f"{nombre_coleccion}.json"
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
