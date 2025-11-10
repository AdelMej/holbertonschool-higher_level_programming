const redHeader = document.querySelector("#red_header");

function changeToRed() {
	redHeader.style.color = "#FF0000";
}

document.querySelector("#red_header").addEventListener("click", changeToRed);
