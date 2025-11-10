const header = document.querySelector("header");
const headerToggle = document.querySelector("#toggle_header");

function switchClass() {
	console.log("ayo");
	if (header.className == "green") {
		header.setAttribute("class", "red");
	} else if (header.className == "red") {
		header.setAttribute("class", "green");
	}
}

headerToggle.addEventListener("click", switchClass);
