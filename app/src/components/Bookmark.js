import React from 'react';

function Bookmark({ bookmark, onDeleteBookmark }) {
    const handleDelete = () => {
        onDeleteBookmark(bookmark.id);
    };
    
    return (
        <div className="bookmark">
            <h3>{bookmark.title}</h3>
            <p>
                <a href={bookmark.url} target="_blank" rel="noopener noreferrer">
                    {bookmark.url}
                </a>
            </p>
            <button onClick={handleDelete}>Eliminar</button>
        </div>
    );
}

export default Bookmark;
