
const modalBtn = document.querySelector('.modal-btn');
if (modalBtn) {
  modalBtn.addEventListener('click', function(event) {
    if(!confirm('Czy na pewno chcesz usunąć notatkę ?')) {
      event.preventDefault()
    }
  })
}