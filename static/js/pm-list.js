
const userSearch = document.querySelector('.search-user');
const userSearchForm = document.querySelector('.user-search-form')
const requestUser_id = JSON.parse(document.querySelector('#json-requestusername').textContent);


userSearch.addEventListener('keyup', (e) => {
  e.preventDefault();
  let userSearchValue = userSearch.value;
  const hostname = window.location.hostname;
  const url = `https://${hostname}/api/users/?q=${userSearchValue}`;
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      const chatListContainer = document.querySelector('.chat-list-div');
      chatListContainer.innerHTML = ''
      const link = document.createElement('a');
      link.classList.add('text-decoration-none');
      link.href = `https://djangochatapp-tt0x.onrender.com/private-message/${requestUser_id}/${data[0].id}/`


      const chatListItem = document.createElement('div');
      chatListItem.classList.add('chat-list');

      const paragraph = document.createElement('p');
      paragraph.classList.add('fw-bolder', 'lead', 'text-captilize', 'ms-2', 'mt-1' ,'text-start', 'd-inline');
      paragraph.textContent = data[0].username;

      // Append the paragraph to the chat list item
      chatListItem.appendChild(paragraph);

      // Append the chat list item to the link
      link.appendChild(chatListItem);
      // Append the link to the container
      chatListContainer.appendChild(link);
    });
});
