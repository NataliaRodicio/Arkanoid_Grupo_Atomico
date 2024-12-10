import pygame

pygame.init()

# Archivos para guardar datos
ARCHIVO_JUGADORES = "jugadores.json"

# Cargar efectos de sonido y música
sonido_golpe = pygame.mixer.Sound("assets/sonidos/golpe.mp3")
sonido_perder_vida = pygame.mixer.Sound("assets/sonidos/perder_vida.mp3")
game_over = pygame.mixer.Sound("assets/sonidos/gameover.mp3")
game_over.set_volume(0.2)
sonido_golpe.set_volume(0.2)
sonido_perder_vida.set_volume(0.2)
pygame.mixer.music.load("assets/sonidos/musica.mp3")
pygame.mixer.music.set_volume(0.1)  # Ajustar el volumen de la música
pygame.mixer.music.play(-1)  # Reproducir en bucle infinito

# Configuración de pantalla
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Arkanoid por GRUPO ATOMICO")

# Cargar la imagen del fondo
fondo_imagen = pygame.image.load("assets/imagenes/fondo.jpg")
fondo_imagen = pygame.transform.scale(fondo_imagen, (ANCHO, ALTO))  # Escalar la imagen para que cubra toda la pantalla

# Configuración inicial
barra_ancho = 100
barra_alto = 20
barra_velocidad = 10
sprite_barra = pygame.image.load("assets/imagenes/barra2.png")
sprite_barra = pygame.transform.scale(sprite_barra, (barra_ancho, barra_alto))

pelota_radio = 10
pelota_vel_x = 5
pelota_vel_y = -5

vidas_iniciales = 3

# Cargar la imagen del ladrillo
sprite_ladrillo = pygame.image.load("assets/imagenes/ladrillo.png")
ladrillo_ancho = ANCHO // 8  # 8 columnas
ladrillo_alto = 30  # Altura fija
sprite_ladrillo = pygame.transform.scale(sprite_ladrillo, (ladrillo_ancho, ladrillo_alto))