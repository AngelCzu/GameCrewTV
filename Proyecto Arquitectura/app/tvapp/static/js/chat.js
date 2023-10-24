const messages = [
    "Usuario1: Hola, ¿cómo están?",
    "Usuario2: ¡Hola! Estamos bien, gracias.",
    "Usuario1: ¿Alguien ha visto esa nueva película?",
];

// Función para mostrar la cantidad de puntos en el elemento "puntos"
function mostrarPuntos() {
    const puntosSpan = document.getElementById("puntos");
    const puntosActuales = parseInt(localStorage.getItem('puntos')) || 0;
    puntosSpan.textContent = puntosActuales;
}

function displayMessages() {
    const chatDiv = document.getElementById("chat");
    chatDiv.innerHTML = messages.join("<br>");
}

function sendMessage() {
const input = document.getElementById("input");
const message = input.value;
const destacarCheckbox = document.getElementById("destacar");
const stickerDropdown = document.getElementById("sticker-dropdown");

const selectedSticker = stickerDropdown.value;

if (message.trim() === "" && !selectedSticker) {
// Si no se ha ingresado un mensaje ni seleccionado un sticker, no hacer nada.
return;
}

if (selectedSticker) {
// Si se ha seleccionado un sticker, envíalo junto con el mensaje
const stickerHTML = `<img src="/app/tvapp/static/img/${selectedSticker}.png" alt="${selectedSticker}" />`;
const messageWithSticker = message + ' ' + stickerHTML;

if (destacarCheckbox.checked) {
    // Si el checkbox está marcado, destaca el mensaje y la imagen
    messages.push(`<div class="user-message">Tú: ${messageWithSticker}</div>`);
    destacarCheckbox.checked = false; // Restablecer el estado del checkbox
    guardarPuntos(-100); // Descontar 100 puntos al destacar un mensaje
} else {
    messages.push(`<div>Tú: ${messageWithSticker}</div>`);
}

stickerDropdown.selectedIndex = 0; // Restablecer la selección del dropdown
} else if (message.trim() !== "") {
if (destacarCheckbox.checked) {
    // Si el checkbox está marcado, destaca solo el mensaje de texto
    messages.push(`<div class="user-message">Tú: ${message}</div>`);
    destacarCheckbox.checked = false; // Restablecer el estado del checkbox
    guardarPuntos(-100); // Descontar 100 puntos al destacar un mensaje
} else {
    messages.push(`<div>Tú: ${message}</div>`);
}
}

input.value = "";
displayMessages();
}

function guardarPuntos(cantidad) {
// Obtener la cantidad de puntos actual del Local Storage o establecerla en 0 si es la primera vez
let puntosActuales = parseInt(localStorage.getItem('puntos')) || 0;

// Calcular la nueva cantidad de puntos
const nuevaCantidad = puntosActuales + cantidad;

if (nuevaCantidad < 100) {
// Si no hay suficientes puntos, deshabilitar la casilla de verificación
document.getElementById('destacar').disabled = true;
}

if (nuevaCantidad >= 0) {
// Guardar la nueva cantidad de puntos (evitando valores negativos)
localStorage.setItem('puntos', nuevaCantidad.toString());
mostrarPuntos(); // Actualizar la visualización de los puntos
}
}


// Función para manejar el clic del botón "Seguir"
function seguirUsuario() {
    // Guardar 300 puntos al seguir al usuario
    guardarPuntos(300);
}

// Agregar un evento de clic al botón "Seguir" para llamar a la función
const seguirBtn = document.getElementById('seguir-btn');
seguirBtn.addEventListener('click', seguirUsuario);

// Verificar la cantidad de puntos al cargar la página
mostrarPuntos();

// Bloquear la casilla de verificación si es necesario
if (parseInt(localStorage.getItem('puntos')) < 100) {
    document.getElementById('destacar').disabled = true;
}

displayMessages();