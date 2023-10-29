import React from 'react';
import Bookmark from './Bookmark';

function BookmarkList({ bookmarks, onDeleteBookmark }) {
    return (
        <div className="bookmark-list">
        <h2>Tus Marcadores</h2>
            {bookmarks.map((bookmark) => (
                <Bookmark key={bookmark.id} bookmark={bookmark} onDeleteBookmark={onDeleteBookmark} />
            ))}
        </div>
    );
}

export default BookmarkList;
        