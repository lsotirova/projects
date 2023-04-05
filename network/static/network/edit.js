function getCookie(name) {
    const value = `; ${document.cookie}`;
    const escapedName = `; ${encodeURIComponent(name)}=`;
    return value.includes(escapedName) ? decodeURIComponent(value.split(escapedName).pop().split(';').shift()) : null;
}


function editPost(post_id) {
    document.getElementById(`content_${post_id}`).style.display = 'none';
    document.getElementById(`editPost_${post_id}`).style.display = 'block';
}

function savePost(post_id) {
    const textArea = document.getElementById(`textarea_${post_id}`).value;
    fetch(`edit/${post_id}/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            content: textArea
        })
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById(`content_${post_id}`).innerHTML = result.data;
        document.getElementById(`content_${post_id}`).style.display = 'block';
        document.getElementById(`editPost_${post_id}`).style.display = 'none';
    })
}

function cancelEdit(post_id) {
    document.getElementById(`content_${post_id}`).style.display = 'block';
    document.getElementById(`editPost_${post_id}`).style.display = 'none';
}

