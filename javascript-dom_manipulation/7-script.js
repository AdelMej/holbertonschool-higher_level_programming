const list = document.querySelector("#list_movies")

fetch("https://swapi-api.hbtn.io/api/films/?")
	.then(response => response.json())
	.then(data => {
		data.results.forEach(film => {
			let li = document.createElement("li")
			li.textContent = film.title;
			list.appendChild(li);
		})
	})
	.catch(error => console.error('Error', error));
