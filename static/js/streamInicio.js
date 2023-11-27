const cards = document.querySelectorAll('.card');
        cards.forEach(card => {
            card.addEventListener('click', function() {
                const nombreSala = this.querySelector('.card-text').getAttribute('data-nombre-sala');
                console.log('Nombre de la sala seleccionada: ' + nombreSala);
                // Puedes hacer lo que necesites con el valor de nombreSala aquí

                localStorage.setItem('nombreSalaSeleccionada', nombreSala);
            });
        });
        