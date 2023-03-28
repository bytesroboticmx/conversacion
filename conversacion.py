import random

preguntas_y_respuestas = {
    "¿Cómo estás?": ["Bien, gracias. ¿Y tú?", "Más o menos. ¿Tú?"],
    "¿Qué has hecho hoy?": ["He trabajado todo el día. ¿Y tú?", "He estado en casa todo el día. ¿Tú?"],
    "¿Cuál es tu película favorita?": ["Me gusta mucho El Padrino. ¿Y tú?", "Me encanta La La Land. ¿Tú?"],
    "¿Qué planes tienes para el fin de semana?": ["Tengo una reunión con amigos el sábado. ¿Y tú?", "Todavía no lo he decidido. ¿Tú?"],
    "¿Qué opinas del cambio climático?": ["Creo que es una amenaza real para el planeta. ¿Y tú?", "Creo que es un problema importante, pero no estoy seguro de cuál es la mejor manera de abordarlo. ¿Tú?"]
}

def conversacion():
    while True:
        entrada = input("Tú: ")
        if entrada.lower() in ("bye", "adios"):
            print("Bot: ¡Hasta luego!")
            break
        else:
            if entrada in preguntas_y_respuestas:
                respuesta = random.choice(preguntas_y_respuestas[entrada])
                print("Bot: " + respuesta)
            else:
                print("Bot: Lo siento, no entiendo lo que quieres decir.")

if __name__ == '__main__':
    print("Bienvenido al Test de Turing. Por favor, introduce una frase y el Bot intentará mantener una conversación contigo.")
    conversacion()
