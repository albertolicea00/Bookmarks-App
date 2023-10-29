// En un formulario de registro, por ejemplo:
import React, { useState } from 'react';

function RegistrationForm() {
    const [formValues, setFormValues] = useState({ username: '', email: '', password: '' });
    const [errors, setErrors] = useState({});

    const handleSubmit = () => {
    // Validación de los datos del formulario

        if (/* error de validación */) {
            setErrors({ /* Detalles de los errores */ });
            return;
        }

    // Envío del formulario
    }

    return (
        <div>
        <h2>Registro</h2>
            {errors.username && <p className="error">{errors.username}</p>}
            {errors.email && <p className="error">{errors.email}</p>}
            {errors.password && <p className="error">{errors.password}</p>}
            {/* Resto del formulario */}
        </div>
    );
}
