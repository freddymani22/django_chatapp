const userSearchBtn = document.querySelector('.btn-primary');
const userSearch = document.querySelector('.search-user');
const userSearchForm = document.querySelector('.user-search-form')
const requestUser_id = JSON.parse(document.querySelector('#json-requestusername').textContent);

userSearchForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const userSearchValue = userSearch.value;

  fetch(`${window.location.host}/api/users/?q=${userSearchValue}`)
    .then((res) => res.json())
    .then((data) => {
      const chatListContainer = document.querySelector('.chat-list');
      const link = document.createElement('a');
      link.classList.add('text-decoration-none');
      link.href = `${window.location.host}/private-message/${requestUser_id}/${data[0].id}/`


      const chatListItem = document.createElement('div');
      chatListItem.classList.add('chat-list');

      const paragraph = document.createElement('p');
      paragraph.classList.add('chat-content');
      paragraph.textContent = data[0].username;

      // Append the paragraph to the chat list item
      chatListItem.appendChild(paragraph);

      // Append the chat list item to the link
      link.appendChild(chatListItem);
      // Append the link to the container
      chatListContainer.appendChild(link);
    });
});
