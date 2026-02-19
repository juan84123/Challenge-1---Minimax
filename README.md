# Challenge-1---Minimax
#¿Qué creé?#
Un motor de juego en Python que utiliza el algoritmo Minimax para la toma de decisiones. El sistema evalúa múltiples jugadas a futuro para determinar el movimiento óptimo basándose en la Distancia de Manhattan entre los personajes. Incluye:

- Tablero dinámico renderizado en consola.

- Modos de juego: Humano vs IA e IA vs IA.

- Sistema de turnos con límite de movimientos.

#¿Qué funcionó?#
Funcionó prácticamente todo... menos el Minimax al comienzo.

#El "Desastre": Minimax y Recursividad#
- Si algo fue un dolor de cabeza, fue el Minimax y la recursividad.

- El problema: Pensar a muchos pasos de profundidad fue un desastre inicial. La recursividad se volvía confusa rápidamente y ajustar la profundidad para que la IA no tardara una eternidad en "pensar", pero que tampoco fuera "tonta", fue un equilibrio muy difícil de encontrar.

- La Heurística: Al principio, la IA no sabía qué priorizar. Lograr que el valor de "victoria" fuera lo suficientemente fuerte para que el Gato realmente buscara comer al ratón y no solo acercarse, fue un proceso de ensayo y error frustrante.

#Mi mejor "¡Ajá!"#
- Mi mayor descubrimiento fue entender que lo simple suele ser mejor.
Me di cuenta de que la IA no necesita ser una calculadora perfecta, sino ser fluida. El problema de los empates no era necesario solucionarlo con matemáticas más complejas o algoritmos pesados, sino con algo tan básico como una lista y un dado (random.choice).