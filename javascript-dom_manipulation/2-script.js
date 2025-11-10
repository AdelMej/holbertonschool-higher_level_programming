const redHeader = document.querySelector("#red_header");

function addClassHeader() {
	redHeader.setAttribute("class", "red");
}

redHeader.addEventListener("click", addClassHeader);
