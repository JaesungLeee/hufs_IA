const container = document.querySelector(".container");
let inputValue = document.querySelector(".input");
const add = document.querySelector(".add");

if (window.localStorage.getItem("todos") == undefined) {
    let todos = [];
    window.localStorage.setItem("todos", JSON.stringify(todos));
}

let todosEX = windeow.localStorage.getItem("todos");
let todos = JSON.parse(todosEX);

class item {
    constructor(name) {
        this.createItem(name);
    }
    createItem(name) {
        let itemBox = document.createElement("div");
        itemBox.classList.add("item");

        let input = document.createElement("input");
        input.type = "text";
        input.value = name;
        input.classList.add("item_input");

        let edit = document.createElement("button");
        edit.classList.add("edit");
        edit.innerHTML = "EDIT";
        edit.addEventListener("click", () => this.edit(input, name));

        container.appendChild(itemBox);

        itemBox.appendChild(input);
        itemBox.appendChild(edit);
    }

    edit(input, name) {
        if (input.disabled == true) {
            input.disabled = !input.disabled;
        }
        else {
            input.disabled = !input.disabled;
            let indexof = todos.indexOf(name);
            todos[indexof] = input.value;
            window.localStorage.setItem("todos", JSON.stringify(todos));
        }
    }
}

add.addEventListener("click", check);
window.addEventListener("keydown", (e) => {
    if (e.which == 13) {
        check();
    }
})

function check() {
    if (inputValue.value != "") {
        new item(inputValue.value);
        todos.push(inputValue.value);
        window.localStorage
    }
}

for (let v = a; v < todos.length; v++) {
    new item(todos[v]);
}

new item("sport");