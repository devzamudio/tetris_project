import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
pygame.mixer.init()
pygame.font.init()
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

global background_music
background_music = pygame.mixer.Sound("menu.mp3")

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


fisica_teoremas_y_datos_curiosos = [
    # Leyes y teoremas básicos
    {"title": "Teorema", "descripcion": "Ley de la Gravedad de Newton", "informacion": "Todo lo que tiene masa atrae a otros objetos. Cuanto más grande es un objeto, más fuerte es su atracción. Por ejemplo, la Tierra atrae a las cosas, por eso caen cuando las soltamos."},
    
    {"title": "Teorema", "descripcion": "Segunda Ley de Newton", "informacion": "Si empujas algo más fuerte, acelera más rápido. Si el objeto es más pesado, necesitarás empujarlo más fuerte para que se mueva."},
    
    {"title": "Teorema", "descripcion": "Tercera Ley de Newton", "informacion": "Si empujas algo, ese algo también te empuja a ti, pero en la dirección contraria. Por ejemplo, cuando saltas, empujas al suelo y el suelo te empuja hacia arriba."},
    
    {"title": "Teorema", "descripcion": "Ley de la Conservación de la Energía", "informacion": "La energía no se pierde, solo cambia de forma. Por ejemplo, cuando una pelota cae, la energía que tenía al estar arriba se convierte en energía de movimiento."},
    
    {"title": "Teorema", "descripcion": "Ley de Coulomb", "informacion": "Si tienes dos cargas eléctricas, se atraen si son diferentes y se repelen si son iguales. Es como cuando te acercas a algo con una carga opuesta y se siente como si te pegara."},
    
    # Teoremas relacionados con el movimiento y el espacio
    {"title": "Teorema", "descripcion": "Teoría de la Relatividad Especial de Einstein", "informacion": "La luz siempre viaja a la misma velocidad, sin importar cómo te muevas. Si viajas muy rápido, el tiempo pasará más lento para ti."},
    
    {"title": "Teorema", "descripcion": "Ley de Kepler", "informacion": "Los planetas giran alrededor del Sol en trayectorias en forma de elipses. Además, se mueven más rápido cuando están cerca del Sol."},
    
    {"title": "Teorema", "descripcion": "Ley de Hubble", "informacion": "El universo se está expandiendo. Cuanto más lejos están las galaxias, más rápido se alejan de nosotros."},
    
    {"title": "Teorema", "descripcion": "Gravedad Cuántica", "informacion": "A nivel muy pequeño (como las partículas), la gravedad se comporta de una forma extraña y no entendemos bien cómo funciona."},
    
    # Datos curiosos de la física
    {"title": "Curiosidad", "descripcion": "El sonido no viaja en el espacio", "informacion": "En el espacio no hay aire, así que no podemos oír nada. El sonido necesita aire para viajar."},
    
    {"title": "Curiosidad", "descripcion": "La luz puede doblarse", "informacion": "Cuando la luz pasa cerca de un objeto muy grande, como una estrella, se curva. Esto se llama 'lente gravitacional'."},
    
    {"title": "Curiosidad", "descripcion": "Los agujeros negros no se ven", "informacion": "Los agujeros negros son tan fuertes que ni siquiera la luz puede escapar de ellos. No podemos verlos, pero sabemos que están allí porque afectan a todo lo que está cerca."},
    
    {"title": "Curiosidad", "descripcion": "Los relojes van más lento en lugares altos", "informacion": "El tiempo pasa más despacio a medida que estamos más lejos de la Tierra. Esto pasa porque la gravedad es más fuerte cerca del suelo y más débil a gran altura."},
    
    {"title": "Curiosidad", "descripcion": "La luz viaja muy rápido", "informacion": "La luz viaja a una velocidad de 299,792 km por segundo, ¡más rápido que cualquier cosa en el universo!"},

    {"title": "Curiosidad", "descripcion": "La materia oscura", "informacion": "La mayoría del universo está hecho de algo que no podemos ver ni tocar, llamado materia oscura. Sabemos que está allí porque hace que las galaxias se muevan de forma extraña."},
    
    {"title": "Curiosidad", "descripcion": "El sol hace energía con fusión nuclear", "informacion": "El sol genera su luz y calor al juntar átomos de hidrógeno para formar helio. Este proceso es lo que hace que el sol brille."},
    
    {"title": "Curiosidad", "descripcion": "El agua puede ser sólido, líquido y gas a la vez", "informacion": "En condiciones especiales, el agua puede ser hielo, agua y vapor al mismo tiempo. Esto se llama 'punto triple'."},
    
    {"title": "Curiosidad", "descripcion": "La superconductividad", "informacion": "A temperaturas muy bajas, algunos materiales pueden conducir electricidad sin perder energía. Este fenómeno se llama superconductividad."},
    
    {"title": "Curiosidad", "descripcion": "La luz blanca es una mezcla de colores", "informacion": "La luz blanca (como la del sol) está hecha de muchos colores. Si la pasas por un cristal, verás los colores del arco iris."},
    
    # Conceptos adicionales
    {"title": "Concepto", "descripcion": "Masa vs Peso", "informacion": "La masa es la cantidad de materia de un objeto y no cambia. El peso depende de la gravedad. En la Luna pesarías menos, pero tu masa seguiría igual."},
    
    {"title": "Concepto", "descripcion": "El Principio de Arquímedes", "informacion": "Cuando un objeto se mete en agua, empuja el agua hacia afuera. Si empuja suficiente agua, el objeto flota."},
    
    {"title": "Concepto", "descripcion": "Principio de Incertidumbre de Heisenberg", "informacion": "En el mundo muy pequeño de las partículas, no podemos conocer con precisión la posición y la velocidad de algo al mismo tiempo."},
    
    {"title": "Concepto", "descripcion": "Energía Cinética", "informacion": "Es la energía que tiene un objeto porque se está moviendo. Depende de qué tan rápido se mueva y de cuán pesado sea."},
    
    {"title": "Concepto", "descripcion": "Energía Potencial Gravitatoria", "informacion": "Es la energía que tiene un objeto porque está en lo alto. Cuando cae, esa energía se convierte en energía de movimiento."}
]

# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3


def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False

    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    global shapes, shape_colors

    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines


def clear_rows(grid, locked):
    # need to see if row is clear the shift every other row above down one

    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Proxima pieza', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))


def draw_window(surface):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)

    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    # pygame.display.update()

def draw_button(surface, text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(surface, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(surface, inactive_color, (x, y, width, height))

    text_surf, text_rect = text_objects(text, pygame.font.SysFont('comicsans', 30))
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    surface.blit(text_surf, text_rect)


def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def main(speed):
    global grid

    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    fall_speed = 0.8 / speed  # Ajusta la velocidad inicial según la elección del usuario
    score = 0
    global background_music
    background_music.stop() 
    background_music = pygame.mixer.Sound("tetris.mp3")
    background_music.play(loops=-1)
    
    while run:

        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005
            

        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

                '''if event.key == pygame.K_SPACE:
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                    current_piece.y -= 1
                    print(convert_shape_format(current_piece))'''  # todo fix

        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

            # call four times to check for multiple clear rows
            if clear_rows(grid, locked_positions):
                score += 10

        draw_window(win)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if check_lost(locked_positions):
            run = False

    game_over()


def game_intro():
    intro = True
    global background_music
    background_music.stop() 
    background_music = pygame.mixer.Sound("menu.mp3")
    background_music.play(loops=-1)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0,0,0))
        largeText = pygame.font.SysFont('comicsans',115)
        TextSurf, TextRect = text_objects("TETRIS", largeText)
        TextRect.center = ((s_width/2),(s_height/2 - 100))
        win.blit(TextSurf, TextRect)

        draw_button(win, "Jugar", 150, 450, 100, 50, (0,200,0), (0,255,0), game_options) # Llama a game_options en lugar de main
        draw_button(win, "Salir", 550, 450, 100, 50, (200,0,0), (255,0,0), pygame.quit)

        pygame.display.update()
        clock.tick(15)

def game_over():
    global background_music
    background_music.stop() 
    background_music = pygame.mixer.Sound("game_over.mp3")
    background_music.play()  # Reproduce el sonido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))
        draw_text_middle("Perdiste, tonoto XD", 40, (255, 255, 255), win)

        # Botón "Continuar" en verde
        draw_button(win, "Continuar", 300, 450, 200, 50, (0, 200, 0), (0, 255, 0), show_fact) 

        pygame.display.update()
        clock.tick(15)

def show_fact():
    global fisica_teoremas_y_datos_curiosos
    global shown_facts
    shown_facts = []  # Variable global para almacenar los datos mostrados

    fact = random.choice(fisica_teoremas_y_datos_curiosos)
    # Asegurar que el dato no se repita
    while fact in shown_facts:
        fact = random.choice(fisica_teoremas_y_datos_curiosos)

    shown_facts.append(fact)  # Agregar el dato a la lista de mostrados

    # Si se han mostrado todos los datos, reiniciar la lista
    if len(shown_facts) == len(fisica_teoremas_y_datos_curiosos):
        shown_facts = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))

        # Mostrar el dato curioso con formato y espacio
        font = pygame.font.SysFont('comicsans', 30)
        title_surface = font.render(fact["title"] + ": " + fact["descripcion"], 1, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(s_width / 2, s_height / 2 - 100))
        win.blit(title_surface, title_rect)

        # Dividir la información en varias líneas si es necesario
        font = pygame.font.SysFont('comicsans', 24)  # Aumentar el tamaño de la fuente a 24
        words = fact["informacion"].split()
        line_width = 0
        line = ""
        y_offset = title_rect.bottom + 20  # Empezar debajo del título
        for word in words:
            word_width, word_height = font.size(word + " ")
            line_width += word_width
            if line_width > play_width:
                text_surface = font.render(line, 1, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(s_width / 2, y_offset))
                win.blit(text_surface, text_rect)
                line = word + " "
                line_width = word_width
                y_offset += word_height  # Mover a la siguiente línea
            else:
                line += word + " "
        # Mostrar la última línea
        text_surface = font.render(line, 1, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(s_width / 2, y_offset))
        win.blit(text_surface, text_rect)

        draw_button(win, "Continuar", 300, 550, 200, 50, (0, 200, 0), (0, 255, 0), retry)
        pygame.display.update()
        clock.tick(15)

def retry():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.fill((0, 0, 0))
        draw_text_middle("¿Reintentar?", 40, (255, 255, 255), win)

        draw_button(win, "Sí, adelante", 150, 450, 200, 50, (0, 200, 0), (0, 255, 0), game_options)
        draw_button(win, "No, salir", 450, 450, 200, 50, (200, 0, 0), (255, 0, 0), pygame.quit)

        pygame.display.update()
        clock.tick(15)

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock() # Initialize clock here

def game_options():
    options = True
    selected_speed = 5
    global background_music
    background_music.stop() 
    background_music = pygame.mixer.Sound("menu.mp3")
    background_music.play(loops=-1)  # Velocidad inicial por defecto

    while options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_speed = max(1, selected_speed - 1)
                elif event.key == pygame.K_RIGHT:
                    selected_speed = min(10, selected_speed + 1)
                elif event.key == pygame.K_RETURN:
                    main(selected_speed)
                    options = False

        win.fill((0, 0, 0))
        
        # Calcula la posición del primer texto
        text1 = "Selecciona la aceleración de las piezas"
        font1 = pygame.font.SysFont('comicsans', 40)
        label1 = font1.render(text1, 1, (255, 255, 255))
        text1_rect = label1.get_rect(center=(s_width / 2, s_height / 2 - 50))  # Centrar en la pantalla, un poco más arriba
        win.blit(label1, text1_rect)

        # Calcula la posición del segundo texto (debajo del primero)
        text2 = str(selected_speed)
        font2 = pygame.font.SysFont('comicsans', 80)
        label2 = font2.render(text2, 1, (255, 255, 255))
        text2_rect = label2.get_rect(center=(s_width / 2, text1_rect.bottom + 50))  # Centrar debajo del primer texto
        win.blit(label2, text2_rect)

        # Nuevo texto que explica el comportamiento de la aceleración
        text3 = "Entre mayor sea la aceleración, más rápido caerán las piezas"
        font3 = pygame.font.SysFont('comicsans', 30)
        label3 = font3.render(text3, 1, (255, 255, 255))
        text3_rect = label3.get_rect(center=(s_width / 2, text2_rect.bottom + 40))  # Centrar debajo del contador
        win.blit(label3, text3_rect)

        pygame.display.update()
        clock.tick(15)

game_intro()  # Llama al menú de introducción
