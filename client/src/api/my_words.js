export default class myWord {
    
    async get_all_words() {
        return fetch("http://127.0.0.1:8000/")
        .then(response => response.json())
        .catch(error => console.log(error));
    }

    async delete_word (title){
        return fetch(`http://127.0.0.1:8000/${title}`,{
            method: 'DELETE'
          }).then(response => response.json())
        .catch(error => console.log(error))
    }

    async add_word (word){
        return fetch("http://127.0.0.1:8000/",{
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(word)
          })
        .then(Response=>Response.json())
        .catch(error => console.log(error))
    }

}