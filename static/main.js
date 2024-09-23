const tagsInput = document.getElementById('tagsInput')
const tagsContainer = document.querySelector('.tags-container')
tagsInput.addEventListener("keypress", e => {
    e.preventDefault()
    if (e.key === "Enter" || e.key === ","){
        const tag = tagsInput.value.trim()
        console.log(tag)
        if (tag) {
           const tagElement = document.createElement("span")
           tagElement.textContent = tag
           tagsContainer.appendChild(tagElement)
           tagsInput.value = "";

        }
    }
})