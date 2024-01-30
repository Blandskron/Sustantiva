function playGame(playerChoice) {
    // Array de opciones para la computadora
    const choices = ['piedra', 'papel', 'tijeras'];
    // Genera una elección aleatoria para la computadora
    const computerChoice = choices[Math.floor(Math.random() * 3)];

    // Determina el resultado del juego
    let result = '';
    if (playerChoice === computerChoice) {
        result = 'Empate!';
    } else if (
        (playerChoice === 'piedra' && computerChoice === 'tijeras') ||
        (playerChoice === 'papel' && computerChoice === 'piedra') ||
        (playerChoice === 'tijeras' && computerChoice === 'papel')
    ) {
        result = '¡Ganaste!';
    } else {
        result = '¡Perdiste!';
    }

    // Muestra el resultado en la interfaz
    document.getElementById('result').innerHTML = `Elegiste ${playerChoice}. La computadora eligió ${computerChoice}. ${result}`;
}
