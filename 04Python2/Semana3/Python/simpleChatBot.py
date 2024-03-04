class SimpleChatbot:
    def __init__(self):
        self.context = None

    def get_response(self, user_input):
        user_input = user_input.lower()

        if 'salir' in user_input:
            return "Hasta luego!", True
        elif 'hola' in user_input:
            return "¡Hola! ¿Cómo estás?", False
        elif 'cómo estás' in user_input:
            return "Estoy bien, gracias por preguntar. ¿Y tú?", False
        elif 'bien' in user_input and 'cómo estás' in self.context:
            return "Me alegra escuchar eso. ¿En qué más puedo ayudarte?", False
        elif 'ayuda' in user_input:
            return "Claro, ¿en qué puedo ayudarte?", False
        elif 'clima' in user_input:
            return "No tengo acceso a datos actuales del clima, pero puedes buscarlo en internet.", False
        else:
            return "No estoy seguro de cómo responder a eso.", False

    def update_context(self, user_input):
        self.context = user_input

    def run(self):
        print("Hola, soy tu chatbot avanzado. Escribe 'salir' para terminar la conversación.")
        
        while True:
            user_input = input("Tú: ")
            response, exit_chat = self.get_response(user_input)
            print("Chatbot:", response)

            if exit_chat:
                break

            self.update_context(user_input)

chatbot = SimpleChatbot()
chatbot.run()
