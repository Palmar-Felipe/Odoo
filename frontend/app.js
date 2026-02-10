

const API = "http://localhost:5000/products";

function load() {
  fetch(API)
    .then(r => r.json())
    .then(data => {
      const list = document.getElementById("list");
      list.innerHTML = "";
      data.forEach(p => {
        list.innerHTML += `<li>
          ${p.name} - ${p.price}
          <button onclick="del(${p.id})">X</button>
        </li>`;
      });
    });
}

function create() {
  fetch(API, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      name: document.getElementById("name").value,
      price: document.getElementById("price").value,
      description: ""
    })
  }).then(load);
}

function del(id) {
  fetch(`${API}/${id}`, { method: "DELETE" })
    .then(load);
}

load();
