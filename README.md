# 🎮 Arkanoid - Juego de Arcade Clásico

## 📖 Descripción del Juego

Arkanoid es un emocionante juego de arcade inspirado en el clásico título de los años 80. Controla una barra para rebotar una pelota y destruir ladrillos sin perder todas tus vidas.

## 🏗️ Estructura del Proyecto

El juego está modularizado en los siguientes componentes:

- `colores.py`: Definición de paleta de colores utilizados en el juego
- `config.py`: Configuraciones iniciales del juego
- `interfaz_usuario.py`: Funciones de interfaz gráfica
  * Crear ladrillos
  * Ingresar nombre de jugador
  * Mostrar mensajes
  * Gestionar pausas y respuestas
- `jugar.py`: Lógica principal del juego
- `main.py`: Punto de entrada del programa
- `menu.py`: Gestión del menú principal
- `puntuaciones.py`: Manejo de puntuaciones
  * Cargar jugadores
  * Guardar puntuaciones
  * Mostrar récords

## 🖥️ Requisitos de Instalación

### Dependencias
- Python 3.8 o superior
- Pygame 2.0 o superior

### Pasos de Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/[tu-usuario]/arkanoid.git
cd arkanoid
```

2. Crear un entorno virtual (opcional pero recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias
```bash
pip install pygame
```

4. Preparar assets
- Asegúrate de tener la carpeta `assets` con los siguientes archivos:
  * `barra2.png`
  * `ladrillo.png`
  * `fondo.jpg`
  * `fondo4.png`
  * `golpe.mp3`
  * `choqueladrillo.mp3`
  * `gameover.mp3`
  * `musica_final.mp3`

## 🎮 Controles del Juego

- **Flecha Izquierda (←)**: Mover barra hacia la izquierda
- **Flecha Derecha (→)**: Mover barra hacia la derecha
- **Barra Espaciadora (SPACE)**: Pausar/Reanudar juego
- **ESC**: Salir del juego o menú de pausa

## 🕹️ Cómo Jugar

1. Ejecuta el juego:
```bash
python main.py
```

2. En el menú principal, puedes:
   - Iniciar un nuevo juego
   - Ver puntuaciones
   - Salir del juego

3. Durante el juego:
   - Mueve la barra para rebotar la pelota
   - Destruye todos los ladrillos
   - Evita que la pelota caiga
   - Gana puntos destruyendo ladrillos
   - Tienes 3 vidas para completar el nivel

## 👥 Equipo

- **Desarrolladores**: Grupo Atómico
- **Diseñadores**: Stella Villalva, Juan Ignacio Turtl, Natalia Celeste Rodicio

## 🏆 Características

- Música de fondo
- Efectos de sonido
- Sistema de puntuación
- Registro de jugadores
- Menú principal interactivo
- Pantalla de pausa
- Arquitectura modular

## 📝 Créditos

- Inspirado en el clásico juego Arkanoid
- Desarrollado con Python y Pygame

**¡Diviértete jugando Arkanoid!** 🚀🎮
