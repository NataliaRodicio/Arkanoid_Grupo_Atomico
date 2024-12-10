import pygame
from colores import *
from interfaz_juego import ingresar_nombre
from config import *
from puntuaciones import cargar_jugadores, mostrar_puntuaciones

pygame.init()

# Menú principal
def menu_principal():
    """
    Muestra el menú principal donde el jugador puede elegir jugar, ver puntuaciones o salir.
    Permite que el jugador seleccione con el mouse.
    """
    fuente = pygame.font.Font(None, 48)
    jugadores = cargar_jugadores()
    
    # Configuración de animación de fondo
    fondo_1_x = 0
    fondo_2_x = ANCHO
    velocidad_fondo = 2
    
    reloj = pygame.time.Clock()  # Para controlar los FPS

    while True:
        # Limitar los FPS
        reloj.tick(60)

        # Mover los fondos
        fondo_1_x -= velocidad_fondo
        fondo_2_x -= velocidad_fondo

        # Si un fondo sale de la pantalla, lo movemos al final
        if fondo_1_x <= -ANCHO:
            fondo_1_x = ANCHO
        if fondo_2_x <= -ANCHO:
            fondo_2_x = ANCHO

        # Fondo animado (con la imagen de fondo)
        PANTALLA.blit(fondo_imagen, (fondo_1_x, 0))
        PANTALLA.blit(fondo_imagen, (fondo_2_x, 0))

        # Texto del menú
        texto_titulo = fuente.render("BIENVENIDOS A ARKANOID", True, BLANCO)
        texto_jugar = fuente.render("Jugar", True, BLANCO)
        texto_puntuaciones = fuente.render("Puntuaciones", True, BLANCO)
        texto_salir = fuente.render("Salir", True, BLANCO)

        PANTALLA.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, 125))
        PANTALLA.blit(texto_jugar, (ANCHO // 2 - texto_jugar.get_width() // 2, 225))
        PANTALLA.blit(texto_puntuaciones, (ANCHO // 2 - texto_puntuaciones.get_width() // 2, 325))
        PANTALLA.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, 425))

        rect_jugar = pygame.Rect(ANCHO // 2 - texto_jugar.get_width() // 2, 225, texto_jugar.get_width(), texto_jugar.get_height())
        rect_puntuaciones = pygame.Rect(ANCHO // 2 - texto_puntuaciones.get_width() // 2, 325, texto_puntuaciones.get_width(), texto_puntuaciones.get_height())
        rect_salir = pygame.Rect(ANCHO // 2 - texto_salir.get_width() // 2, 425, texto_salir.get_width(), texto_salir.get_height())

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = pygame.mouse.get_pos()
                if rect_jugar.collidepoint(pos):
                    jugador = ingresar_nombre()
                    from jugar import jugar
                    jugar(jugador, jugadores)
                elif rect_puntuaciones.collidepoint(pos):
                    mostrar_puntuaciones(jugadores)
                elif rect_salir.collidepoint(pos):
                    pygame.quit()
                    exit()