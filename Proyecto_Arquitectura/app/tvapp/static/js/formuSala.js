function nombreSala() {
    // Obtén el valor del input con el id 'txtSala'.
    const nombreSalaInput = document.getElementById('txtSala');
    const nombreSala = nombreSalaInput.value;

    // Verifica si se ingresó un nombre de sala.
    if (nombreSala) {
        // Almacena el nombre de la sala en el local storage.
        localStorage.setItem('nombreSala', nombreSala);
    }
}





/* document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('formAgregarSala');
    form.addEventListener('click', function (event) {
        event.preventDefault(); // Evita que el formulario se envíe de forma predeterminada.

        // Captura el valor del input.
        const inputElement = document.getElementById('txtSala');
        const nombreSala = inputElement.value;

        // Almacena el valor en el almacenamiento local.
        localStorage.setItem('nombreSala', nombreSala);

        // Luego, puedes redirigir al usuario a la página deseada, como lo hiciste anteriormente.

    });
}); */