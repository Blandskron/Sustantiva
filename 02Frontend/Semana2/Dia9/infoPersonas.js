// Definición de la clase Futbolista
function Futbolista(name, team, position) {
    // Atributos de la clase
    this.name = name;
    this.team = team;
    this.position = position;
    this.isCaptain = false; // Inicialmente, no son capitanes

    // Método para mostrar información del futbolista
    this.displayInfo = function () {
        console.log(`Futbolista Information:
         Name: ${this.name}
         Team: ${this.team}
         Position: ${this.position}
         ${this.isCaptain ? 'Captain: Yes' : 'Captain: No'}
        `);
    };

    // Método para convertirse en capitán
    this.becomeCaptain = function () {
        this.isCaptain = true;
        console.log(`${this.name} has become the captain of the team!`);
    };
}

// Creación de instancias de futbolistas
const messi = new Futbolista('Lionel Messi', 'Paris Saint-Germain', 'Forward');
const ronaldo = new Futbolista('Cristiano Ronaldo', 'Manchester United', 'Forward');
const neymar = new Futbolista('Neymar Jr.', 'Paris Saint-Germain', 'Forward');

// Mostrar información inicial de los futbolistas
messi.displayInfo();
ronaldo.displayInfo();
neymar.displayInfo();

// Messi se convierte en capitán
messi.becomeCaptain();

// Mostrar información actualizada después de que Messi se convierte en capitán
messi.displayInfo();
ronaldo.displayInfo();
neymar.displayInfo();
