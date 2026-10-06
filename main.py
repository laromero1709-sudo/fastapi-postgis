from fastapi import FastAPI

from database import get_connection


app = FastAPI(
    title="API GIS con FastAPI + PostgreSQL + PostGIS",
    description="API de práctica para trabajar con PostgreSQL, PostGIS y FastAPI",
    version="1.0.0"
)


@app.get("/")
def inicio():

    return {
        "mensaje": "API GIS funcionando",
        "base_de_datos": "expansion_gis",
        "postgresql": "14",
        "postgis": "activo",
        "estado": "OK"
    }


@app.get("/conexion")
def comprobar_conexion():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            current_database(),
            current_user,
            version();
    """)

    resultado = cursor.fetchone()

    cursor.close()
    connection.close()

    return {
        "base_de_datos": resultado[0],
        "usuario": resultado[1],
        "version": resultado[2],
        "conexion": "OK"
    }


@app.get("/postgis")
def comprobar_postgis():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT PostGIS_Version();
    """)

    resultado = cursor.fetchone()

    cursor.close()
    connection.close()

    return {
        "postgis_version": resultado[0],
        "postgis": "OK"
    }


@app.get("/estructura-gis")
def estructura_gis():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            f_table_schema,
            f_table_name,
            f_geometry_column,
            type,
            srid
        FROM geometry_columns
        ORDER BY f_table_schema, f_table_name;
    """)

    resultados = cursor.fetchall()

    cursor.close()
    connection.close()

    return [
        {
            "schema": fila[0],
            "tabla": fila[1],
            "columna_geometria": fila[2],
            "tipo_geometria": fila[3],
            "srid": fila[4]
        }
        for fila in resultados
    ]
