import pygame
from config import *
from colores import *
from puntuaciones import cargar_jugadores

pygame.init()

# Crear ladrillos con la imagen
def crear_ladrillos(filas: int, columnas: int) -> list:
    """
    Crea una lista de ladrillos (rectángulos) a partir de filas y columnas.

    Argumentos:
        filas (int): Número de filas de ladrillos.
        columnas (int): Número de columnas de ladrillos.

    Retorna:
        list: Lista de objetos rectángulos (pygame.Rect) que representan los ladrillos.
    """
    ladrillos = []
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * ladrillo_ancho
            y = fila * ladrillo_alto
            rect_ladrillo = pygame.Rect(x, y, ladrillo_ancho, ladrillo_alto)
            ladrillos.append(rect_ladrillo)
    return ladrillos

# Ingresar nombre del jugador
def ingresar_nombre() -> str:
    """
    Permite al jugador ingresar su nombre.

    Retorna:
        str: El nombre del jugador ingresado.
    """
    jugadores = cargar_jugadores()
    fuente = pygame.font.Font(None, 36)
    nombre = ""

    while True:
        PANTALLA.fill(NEGRO)
        texto_ingresar = fuente.render("Ingresa tu nombre:", True, BLANCO)
        texto_nombre = fuente.render(nombre, True, BLANCO)

        PANTALLA.blit(texto_ingresar, (100, 200))
        PANTALLA.blit(texto_nombre, (100, 300))

        if nombre in jugadores:
            texto_error = fuente.render("El nombre ya está registrado.", True, ROJO)
            PANTALLA.blit(texto_error, (100, 350))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if nombre and nombre not in jugadores:
                        return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif evento.unicode.isalnum():
                    nombre += evento.unicode

def mostrar_mensaje(mensaje: str, submensaje: str, opciones: bool = False):

    """
    Muestra un mensaje y un submensaje en la pantalla centralizada, en un fondo negro.
    El mensaje permanece en pantalla hasta que el jugador presione una tecla.

    Argumentos:
        mensaje (str): El mensaje principal que se muestra en la pantalla.
        submensaje (str): El submensaje que se muestra debajo del mensaje principal.
    """
    
    fuente = pygame.font.Font(None, 48)
    texto_mensaje = fuente.render(mensaje, True, BLANCO)
    texto_submensaje = fuente.render(submensaje, True, BLANCO)

    PANTALLA.fill(NEGRO)
    PANTALLA.blit(texto_mensaje, (ANCHO // 2 - texto_mensaje.get_width() // 2, ALTO // 2 - 50))
    PANTALLA.blit(texto_submensaje, (ANCHO // 2 - texto_submensaje.get_width() // 2, ALTO // 2 + 10))

    if opciones:
        texto_reiniciar = fuente.render("Reiniciar", True, BLANCO)
        texto_salir = fuente.render("Salir", True, BLANCO)
        PANTALLA.blit(texto_reiniciar, (ANCHO // 2 - texto_reiniciar.get_width() // 2, ALTO // 2 + 70))
        PANTALLA.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, ALTO // 2 + 120))

    pygame.display.flip()

def esperar_respuesta() -> str:
    """
    Espera que el jugador ingrese una respuesta (S/N) para reiniciar el juego o salir al menú.

    Retorna:
        str: La respuesta del jugador (S o N).
    """
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Verifica si se hizo clic izquierdo
                    pos = pygame.mouse.get_pos()
                    if ANCHO // 2 - 100 <= pos[0] <= ANCHO // 2 + 100:
                        if ALTO // 2 + 70 <= pos[1] <= ALTO // 2 + 120:
                            return 'reiniciar'
                        elif ALTO // 2 + 120 <= pos[1] <= ALTO // 2 + 170:
                            return 'salir'
                        
def mostrar_pausa():
    """
    Muestra la pantalla de pausa cuando el juego está pausado.
    """
    from menu import menu_principal
    import jugar

    fuente = pygame.font.Font(None, 48)
    texto_pausa = fuente.render("¡PAUSA!", True, BLANCO)
    texto_reanudar = fuente.render("Presiona ESPACIO para reanudar", True, BLANCO)
    texto_salir = fuente.render("Presiona ESC para salir", True, BLANCO)

    PANTALLA.fill(NEGRO)
    PANTALLA.blit(texto_pausa, (ANCHO // 2 - texto_pausa.get_width() // 2, ALTO // 2 - 50))
    PANTALLA.blit(texto_reanudar, (ANCHO // 2 - texto_reanudar.get_width() // 2, ALTO // 2 + 10))
    PANTALLA.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, ALTO // 2 + 70))

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                menu_principal()
            if evento.key == pygame.K_SPACE:
                jugar.pausa
                jugar.pausa = False