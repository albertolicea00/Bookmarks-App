// URL de la API
const API_URL = "http://127.0.0.1:8000/bookmarklet/api/bookmarks/";

// Función para obtener todos los marcadores
export async function getBookmarks() {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error("Error al obtener marcadores");
        }
        return await response.json();
    } catch (error) {
        throw error;
    }
}

// Función para agregar un nuevo marcador
export async function addBookmark(newBookmark) {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(newBookmark),
        });
        
        if (!response.ok) {
            throw new Error("Error al agregar un marcador");
        }
        
        return await response.json();
    } catch (error) {
        throw error;
    }
}

// Función para eliminar un marcador por su ID
export async function deleteBookmark(bookmarkId) {
    try {
        const response = await fetch(`${API_URL}/${bookmarkId}`, {
            method: "DELETE",
        });
        
        if (!response.ok) {
            throw new Error("Error al eliminar el marcador");
        }
        
        return await response.json();
    } catch (error) {
        throw error;
    }
}
