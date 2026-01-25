const BASE_URL = "http://127.0.0.1:8001";

function register() {
  fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: name.value,
      email: email.value,
      password: password.value
    })
  })
  .then(res => res.json())
  .then(data => {
    alert("Registered successfully");
    window.location.href = "login.html";
  })
  .catch(err => alert("Error"));
}

function login() {
  fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      email: email.value,
      password: password.value
    })
  })
  .then(res => res.json())
  .then(data => {
    localStorage.setItem("token", data.access_token);
    window.location.href = "dashboard.html";
  })
  .catch(err => alert("Login failed"));
}

function getProfile() {
  fetch(`${BASE_URL}/api/profile`, {
    headers: {
      "Authorization": "Bearer " + localStorage.getItem("token")
    }
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText =
      JSON.stringify(data, null, 2);
  });
}

function logout() {
  localStorage.removeItem("token");
  window.location.href = "login.html";
}
