import pygame
from config import *
from colores import *
from interfaz_juego import crear_ladrillos, mostrar_pausa, esperar_respuesta, mostrar_mensaje
from puntuaciones import guardar_jugadores

pygame.init()

# Jugar
def jugar(jugador: str, jugadores: dict):
    """
    Inicia el juego con un fondo en movimiento. El jugador controla la barra y la pelota,
    destruye ladrillos, y gestiona vidas.

    Argumentos:
        jugador (str): Nombre del jugador.
        jugadores (dict): Diccionario con los jugadores y sus puntuaciones.
    """
    global pelota_vel_x, pelota_vel_y

    # Cargar el fondo en movimiento
    fondo_juego = pygame.image.load("assets/imagenes/fondo4.png")
    fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))

    # Posiciones para el movimiento del fondo
    fondo_1_x = 0
    fondo_2_x = ANCHO
    velocidad_fondo = 2

    jugadores.setdefault(jugador, {"puntuacion": 0, "vidas": vidas_iniciales})
    puntuacion = jugadores[jugador]["puntuacion"]
    vidas = jugadores[jugador]["vidas"]

    barra_x = (ANCHO - barra_ancho) // 2
    barra_y = ALTO - 40
    pelota_x = ANCHO // 2
    pelota_y = ALTO // 2

    ladrillos = crear_ladrillos(5, 8)
    reloj = pygame.time.Clock()

    global pausa
    pausa = False

    while True:
        # Actualizar el fondo
        fondo_1_x -= velocidad_fondo
        fondo_2_x -= velocidad_fondo

        # Si un fondo sale de la pantalla, lo reposicionamos
        if fondo_1_x <= -ANCHO:
            fondo_1_x = ANCHO
        if fondo_2_x <= -ANCHO:
            fondo_2_x = ANCHO

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pausa = True  # Cambiar el estado de pausa
        
        if pausa:
            mostrar_pausa()
            continue  # Si el juego está en pausa, no 

        # Movimiento de la barra
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and barra_x > 0:
            barra_x -= barra_velocidad
        if teclas[pygame.K_RIGHT] and barra_x < ANCHO - barra_ancho:
            barra_x += barra_velocidad

        # Movimiento de la pelota
        pelota_x += pelota_vel_x
        pelota_y += pelota_vel_y

        # Rebote de la pelota
        if pelota_x <= 0 or pelota_x >= ANCHO:
            pelota_vel_x *= -1
        if pelota_y <= 0:
            pelota_vel_y *= -1
        if pelota_y > ALTO:
            vidas -= 1
            sonido_perder_vida.play()
            if vidas == 0:
                pygame.mixer.music.stop()
                game_over.play()
                mostrar_mensaje("¡Game Over!", "¿Quieres intentarlo de nuevo o salir?", True)
                respuesta = esperar_respuesta()
                if respuesta == 'reiniciar':
                    pygame.mixer.music.play(-1)
                    jugadores[jugador]["puntuacion"] = 0
                    jugadores[jugador]["vidas"] = vidas_iniciales
                    guardar_jugadores(jugadores)
                    return jugar(jugador, jugadores)
                else:
                    pygame.mixer.music.play(-1)
                    jugadores[jugador]["puntuacion"] = puntuacion
                    guardar_jugadores(jugadores)
                    from menu import menu_principal
                    return menu_principal()
            pelota_x, pelota_y = ANCHO // 2, ALTO // 2

        # Rebote en la barra
        if barra_y <= pelota_y + pelota_radio <= barra_y + barra_alto and barra_x <= pelota_x <= barra_x + barra_ancho:
            pelota_vel_y *= -1
            sonido_golpe.play()

        # Colisiones con ladrillos
        for ladrillo in ladrillos[:]:
            if ladrillo.collidepoint(pelota_x, pelota_y):
                ladrillos.remove(ladrillo)
                puntuacion += 10
                pelota_vel_y *= -1
                sonido_golpe.play()
                break

        # Dibujar fondo en movimiento
        PANTALLA.blit(fondo_juego, (fondo_1_x, 0))
        PANTALLA.blit(fondo_juego, (fondo_2_x, 0))

        # Dibujar elementos del juego
        PANTALLA.blit(sprite_barra, (barra_x, barra_y))
        pygame.draw.circle(PANTALLA, ROJO, (pelota_x, pelota_y), pelota_radio)

        for ladrillo in ladrillos:
            PANTALLA.blit(sprite_ladrillo, (ladrillo.x, ladrillo.y))

        # Mostrar puntuación y vidas
        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
        texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
        PANTALLA.blit(texto_puntuacion, (10, 10))
        PANTALLA.blit(texto_vidas, (ANCHO - texto_vidas.get_width() - 10, 10))

        pygame.display.flip()
        reloj.tick(60)  # Limitar los FPS a 60

        # Verificar si el jugador ha ganado (todos los ladrillos eliminados)
        if not ladrillos:
            jugadores[jugador]["puntuacion"] = puntuacion
            jugadores[jugador]["vidas"] = vidas
            guardar_jugadores(jugadores)
            mostrar_mensaje("¡Ganaste!", "Presiona cualquier tecla para volver al menú...", False)
            return