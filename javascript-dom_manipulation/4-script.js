const list = document.querySelector(".my_list");
const addItem = document.querySelector("#add_item");

function addingItem() {
	let newItem = document.createElement("li");
	newItem.textContent = "Item";
	list.appendChild(newItem);
}

addItem.addEventListener("click", addingItem);
