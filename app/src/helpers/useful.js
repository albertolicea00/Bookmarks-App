// Función para generar un ID único
export function generateUniqueId() {
    // Intentar obtener el contador del almacenamiento local
    let counter = localStorage.getItem('uniqueIdCounter');
    
    // Si no se encuentra el contador, inicializarlo a 1
    if (counter === null)  counter = 1;
    else counter = parseInt(counter, 10) + 1;
    
    // Almacenar el nuevo valor del contador en el almacenamiento local
    localStorage.setItem('uniqueIdCounter', counter.toString());
    
    // Combinar la fecha actual y el contador para generar un ID único
    const timestamp = new Date().getTime();
    return `${timestamp}-${counter}`;
}


// Función para formatear una fecha en un formato legible
export function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString(undefined, options);
}

// Función para limitar la longitud de un texto y agregar puntos suspensivos si es demasiado largo
export function truncateText(text, maxLength) {
    if (text.length > maxLength) {
        return text.substring(0, maxLength) + '...';
    }
    return text;
}
