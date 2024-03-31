function playGame(seleccionJugador) {
    // Array de opciones para la computadora
    const seleccion = ['piedra', 'papel', 'tijeras'];
    // Genera una elección aleatoria para la computadora
    const eleccionComputadora = seleccion[Math.floor(Math.random() * 3)];

    // Determina el resultado del juego
    let result = '';
    if (seleccionJugador === eleccionComputadora) {
        result = 'Empate!';
    } else if (
        (seleccionJugador === 'piedra' && eleccionComputadora === 'tijeras') ||
        (seleccionJugador === 'papel' && eleccionComputadora === 'piedra') ||
        (seleccionJugador === 'tijeras' && eleccionComputadora === 'papel')
    ) {
        result = '¡Ganaste!';
    } else {
        result = '¡Perdiste!';
    }

    // Muestra el resultado en la interfaz
    document.getElementById('result').innerHTML = `Elegiste ${seleccionJugador}. La computadora eligió ${eleccionComputadora}. ${result}`;
}
