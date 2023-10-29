// Función para validar una URL
export function isValidURL(url) {
    const urlPattern = /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/i;
    return urlPattern.test(url);
}

// Función para validar un título (no vacío)
export function isValidTitle(title) {
    return title.trim() !== "";
}

// Función para validar un marcador completo
export function validateBookmark(bookmark) {
    const errors = {};
    
    if (!isValidURL(bookmark.url)) {
        errors.url = "La URL no es válida";
    }
    
    if (!isValidTitle(bookmark.title)) {
        errors.title = "El título no puede estar vacío";
    }
    
    return errors;
}
