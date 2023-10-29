import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL;

// Función para obtener todos los marcadores
export const getBookmarks = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/bookmarks`);
        return response.data;
    } catch (error) {
        throw error;
    }
};

// Función para agregar un nuevo marcador
export const addBookmark = async (bookmarkData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/bookmarks`, bookmarkData);
        return response.data;
    } catch (error) {
        throw error;
    }
};

// Función para actualizar un marcador existente
export const updateBookmark = async (bookmarkId, updatedData) => {
    try {
        const response = await axios.put(`${API_BASE_URL}/bookmarks/${bookmarkId}`, updatedData);
        return response.data;
    } catch (error) {
        throw error;
    }
};

// Función para eliminar un marcador
export const deleteBookmark = async (bookmarkId) => {
    try {
        await axios.delete(`${API_BASE_URL}/bookmarks/${bookmarkId}`);
    } catch (error) {
        throw error;
    }
};
