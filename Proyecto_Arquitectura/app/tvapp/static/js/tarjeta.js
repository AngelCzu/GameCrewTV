function validarFormulario() {
    // Obtener los valores de los campos del formulario
    var numeroTarjeta = document.getElementById("numero_tarjeta").value;

    // Aquí puedes agregar tu propia lógica de validación
    // Por ejemplo, podrías realizar una solicitud AJAX para verificar la tarjeta en el servidor
    // y mostrar una alerta en función de la respuesta del servidor.

    // Este es solo un ejemplo simple de validación
    if (numeroTarjeta.length !== 16) {
        alert("Número de tarjeta no válido. Debe tener 16 dígitos.");
        return;
    }

    // Si la validación es exitosa, puedes continuar con el envío del formulario
    document.getElementById("compraSolespeForm").submit();
}