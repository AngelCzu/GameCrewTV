function updateChat() {
    var salaId = "{{ sala_id }}"; // Obtén el ID de la sala desde el contexto de Django
    var url = "/get_messages/" + salaId + "/";

    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            var chatDiv = $('#chat');
            chatDiv.empty(); // Limpia el contenido actual del chat

            // Agrega los nuevos mensajes al chat
            data.mensajes.forEach(function (mensaje) {
                var mensajeHTML = '<p>' + mensaje.usuario + ' (' + mensaje.timestamp + '): ' + mensaje.mensaje + '</p>';
                chatDiv.append(mensajeHTML);
            });
        },
        error: function (error) {
            console.log('Error al obtener mensajes: ' + error);
        },
        complete: function () {
            // Establece un temporizador para la próxima actualización después de 1000 ms (1 segundo)
            setTimeout(updateChat, 1000);
        }
    });
}

// Llama a la función inicialmente para iniciar el proceso de actualización
updateChat();
