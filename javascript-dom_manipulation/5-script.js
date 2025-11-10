const header = document.querySelector("header");
const updateHeader = document.querySelector("#update_header");

function header_update() {
	header.textContent = "New Header!!!";
}


updateHeader.addEventListener("click", header_update);
