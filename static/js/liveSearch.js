
let titlesArr = Array.from(document.querySelectorAll('.note-title'));
let titles = titlesArr.map(title => title.textContent);

const searchBar = document.getElementById('searchBar');

searchBar.addEventListener('keyup', function(event) {
  let inputValue = searchBar.value
  let filteredData = titlesArr.filter(title => {
    let filterElement = title.textContent
      .toLowerCase()
      .includes(inputValue.toLowerCase());

    const note = title.parentElement.parentElement.parentElement.parentElement
    if (!filterElement) {
      note.style.display = 'none'
    } else {
      note.style.display = 'block'
    }
    return title.textContent.toLowerCase().includes(inputValue.toLowerCase())
  })
  
})
