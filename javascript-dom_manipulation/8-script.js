const disp = document.querySelector("#hello");

fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
	.then(response => response.json())
	.then(data => {
		disp.textContent = data.hello
	})
	.catch(error => console.error("Error", error));
