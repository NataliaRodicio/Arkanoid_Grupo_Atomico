import pygame
import json
import os
from config import *
from colores import *

pygame.init()

# Cargar y guardar puntuaciones por jugador
def cargar_jugadores() -> dict:
    """
    Carga el archivo JSON de jugadores, si existe, y retorna un diccionario.

    Retorna:
        dict: Diccionario con los jugadores y sus puntuaciones.
    """
    if os.path.exists(ARCHIVO_JUGADORES):
        with open(ARCHIVO_JUGADORES, "r") as archivo:
            return json.load(archivo)
    return {}

def guardar_jugadores(jugadores: dict):
    """
    Guarda los datos de los jugadores en el archivo JSON.

    Argumentos:
        jugadores (dict): Diccionario con los datos de los jugadores y sus puntuaciones.
    """
    with open(ARCHIVO_JUGADORES, "w") as archivo:
        json.dump(jugadores, archivo)

# Mostrar puntuaciones
def mostrar_puntuaciones(jugadores: dict):
    """
    Muestra las puntuaciones de todos los jugadores guardados en el archivo JSON.

    Argumentos:
        jugadores (dict): Diccionario con los jugadores y sus puntuaciones.
    """
    fuente = pygame.font.Font(None, 36)
    while True:
        PANTALLA.fill(NEGRO)
        texto_titulo = fuente.render("Puntuaciones", True, BLANCO)
        PANTALLA.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, 50))

        y = 150
        for jugador, datos in jugadores.items():
            texto = fuente.render(f"{jugador}: {datos['puntuacion']} puntos", True, BLANCO)
            PANTALLA.blit(texto, (100, y))
            y += 50

        texto_volver = fuente.render("Presiona ESC para volver", True, BLANCO)
        PANTALLA.blit(texto_volver, (100, ALTO - 50))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return