function likeFunction(id, post_liked_ids, like_count) {
    const btnLike = document.getElementById(`${id}`);
    let liked = post_liked_ids.includes(id);
  
    fetch(`/toggle_like/${id}`)
      .then(response => response.json())
      .then(result => {
        post_liked_ids = result.post_liked_ids;
        liked = post_liked_ids.includes(id);
  
        if (liked) {
          btnLike.classList.remove("far", "fa-heart");
          btnLike.classList.add("fas", "fa-heart", "text-danger");
          like_count++;
        } else {
          btnLike.classList.remove("fas", "fa-heart", "text-danger");
          btnLike.classList.add("far", "fa-heart");
          like_count--;
        }
  
        document.getElementById(`likes-count-${id}`).textContent = result.likes_count + (result.likes_count == 1 ? " like" : " likes");
      });
  } 