$(document).ready(function() {
    // Obtener la URL y el CSRF token desde los inputs ocultos
    const csrfToken = $('#csrf-token').val();
    const enviarPreguntaUrl = $('#enviar-pregunta-url').val();

    $('#chat-message-submit').on('click', function() {
        let mensaje = $('#chat-message-input').val();
        if ($('#predefined-questions').val()) {
            mensaje = $('#predefined-questions').val();
        }

        if (mensaje.trim() !== "") {
            $('#chat-log').append('<div><strong>Tú:</strong> ' + mensaje + '</div>');

            $.ajax({
                type: 'POST',
                url: enviarPreguntaUrl,  // Usando la URL desde el input oculto
                data: {
                    'mensaje': mensaje,
                    'csrfmiddlewaretoken': csrfToken  // Usando el CSRF token desde el input oculto
                },
                success: function(response) {
                    $('#chat-log').append('<div><strong>Respuesta:</strong> ' + response.respuesta + '</div>');
                    $('#chat-message-input').val('');
                    $('#predefined-questions').val('');
                },
                error: function(xhr, status, error) {
                    $('#chat-log').append('<div><strong>Error:</strong> No se pudo enviar la pregunta.</div>');
                }
            });
        }
    });
});
