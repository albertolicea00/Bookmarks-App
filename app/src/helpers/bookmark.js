// Función para ordenar una lista de marcadores por fecha de creación
export function sortBookmarksByDate(bookmarks) {
    return bookmarks.slice().sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
}