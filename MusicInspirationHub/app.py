from app import create_app  # Importamos la función create_app desde el módulo app

# Creamos una instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    # Ejecutamos la aplicación en modo de depuración
    app.run(debug=True)
