import React, { useState } from "react";

function AddBookmarkForm({ onAddBookmark }) {
    const [title, setTitle] = useState("");
    const [url, setUrl] = useState("");
    
    const handleTitleChange = (e) => {
        setTitle(e.target.value);
    };
    
    const handleUrlChange = (e) => {
        setUrl(e.target.value);
    };
    
    const handleSubmit = (e) => {
        e.preventDefault();
        
        // Validar los datos antes de agregar el marcador
        if (!title || !url) {
            alert("Por favor, ingresa un título y una URL válida.");
            return;
        }
        
        // Crear un nuevo objeto de marcador
        const newBookmark = {
            id: "", // Puedes utilizar la función de generación de ID único aquí
            title,
            url,
            createdAt: new Date().toISOString(),
        };
        
        // Llamar a la función de callback para agregar el marcador
        onAddBookmark(newBookmark);
        
        // Limpiar los campos del formulario
        setTitle("");
        setUrl("");
    };
    
    return (
        <div>
            <h2>Agregar Nuevo Marcador</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Título:</label>
                    <input type="text" value={title} onChange={handleTitleChange} />
                </div>
                <div>
                    <label>URL:</label>
                    <input type="text" value={url} onChange={handleUrlChange} />
                </div>
                <button type="submit">Agregar Marcador</button>
            </form>
        </div>
    );
}
    
export default AddBookmarkForm;
    