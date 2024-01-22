function playGame(playerChoice) {
    // Array de opciones para la computadora
    const choices = ['rock', 'paper', 'scissors'];
    // Genera una elección aleatoria para la computadora
    const computerChoice = choices[Math.floor(Math.random() * 3)];

    // Determina el resultado del juego
    let result = '';
    if (playerChoice === computerChoice) {
        result = 'Empate!';
    } else if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        result = '¡Ganaste!';
    } else {
        result = '¡Perdiste!';
    }

    // Muestra el resultado en la interfaz
    document.getElementById('result').innerHTML = `Elegiste ${playerChoice}. La computadora eligió ${computerChoice}. ${result}`;
}
