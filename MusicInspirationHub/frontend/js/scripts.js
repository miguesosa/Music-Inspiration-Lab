// URL base de la API
const API_BASE_URL = 'http://127.0.0.1:5000';

// Función para registrar un nuevo usuario
async function registerUser(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto

    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    const contraseña = document.getElementById('contraseña').value;

    const response = await fetch(`${API_BASE_URL}/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre, email, contraseña }),
    });

    const data = await response.json();
    alert(data.msg); // Mostrar mensaje de respuesta
}

// Función para iniciar sesión
async function loginUser(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto

    const email = document.getElementById('email').value;
    const contraseña = document.getElementById('contraseña').value;

    const response = await fetch(`${API_BASE_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, contraseña }),
    });

    const data = await response.json();
    if (response.ok) {
        localStorage.setItem('access_token', data.access_token); // Guardar el token
        alert("Inicio de sesión exitoso!");
    } else {
        alert(data.msg); // Mostrar mensaje de error
    }
}

// Función para acceder a la ruta protegida
async function accessProtectedRoute() {
    const token = localStorage.getItem('access_token'); // Obtener el token

    const response = await fetch(`${API_BASE_URL}/protegido`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
        },
    });

    const data = await response.json();
    alert(data.msg); // Mostrar mensaje de la ruta protegida
}

// Agregar eventos a los formularios
document.getElementById('registerForm').addEventListener('submit', registerUser);
document.getElementById('loginForm').addEventListener('submit', loginUser);
document.getElementById('accessProtectedRouteButton').addEventListener('click', accessProtectedRoute);
