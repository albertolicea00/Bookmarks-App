import React, { useState } from 'react';

function Login() {
    const [error, setError] = useState('');

    const handleLogin = () => {

        if (/* error de autenticación */) {
            setError('Credenciales incorrectas. Por favor, inténtalo de nuevo.');
        }
    }

    return (
        <div>
            <h2>Iniciar Sesión</h2>
                {error && <p className="error">{error}</p>}
                {/* Resto del formulario */}
        </div>
    );
}
