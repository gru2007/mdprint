import tkinter as tk import random
# Создаем главное окно
root = tk.Tk()
root. title("Избегай блоки")
# Устанавливаем размеры окна и канваса
WIDTH, HEIGHT = 400, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack
# Игрок
player = canvas.create_rectangle(175, 350, 225, 375, fill="blue")
# Переменные для управления
player_speed = 20
game_over = False
# Список для хранения падающих блоков
blocks = []
# Функции для управления игроком
def move_left(event): 1 usage if not game_over:
canvas. move *args: player, -player_speed, 0)
def move_right(event): 1 usage if not game_over:
canvas.move *args: player, player_speed, 0)
# Функция для создания падающих блоков с меньшей вероятностью
def create_block(: 1 usage
if not game_over and random.random() < 0.02: # 2% шанс появления блока
x= random.randint( a: 0, WIDTH - 30)
block = canvas.create_rectangle(x, 0, x + 30, 20, fill="red")
blocks.append (block)
# Функция для обновления игры
def update_game: 2 usages
global game_over
if game_over:
return
canvas.create_text(wIDTH // 2, HEIGHT // 2, text="Игра окончена", font=("Arial", 20), fill="black")
# Двигаем падающие блоки
blocks_to_remove = [] # Список для блоков, которые надо удалить
for block in blocks:
canvas.move( *args: block, 0, 5) # Каждый блок падает вниз на 5 пикселей if canvas.coords(block)[3] > HEIGHT: # Если блок выходит за экран blocks_to_remove.append(block) # Отмечаем блок на удаление
else:
# Проверка на столкновение
if canvas.coords(block)[1] >= canvas.coords(player)[1] and \ canvas.coords(block)[2] >= canvas.coords(player)[0] and \ canvas.coords(block)[0] <= canvas.coords(player)[2]:
game_over = True
* удаляем блоки, которые вышли за экран или столкнулись с игроком
for block in blocks_to_remove:
canvas.delete(block)
blocks.remove(block)
def update_game(: 2 usages
# Проверка на столкновение
if canvas.coords(block)[1] >= canvas.coords(player)[1] and \ canvas.coords(block)[2] >= canvas.coords(player)[0] and \ canvas.coords(block)[0] <= canvas.coords(player)[2]:
game_over = True
# Удаляем блоки, которые вышли за экран или столкнулись с игроком
for block in blocks_to_remove:
canvas.delete(block)
blocks.remove(block)
create_block() # Пытаемся создать новый блок с вероятностью 2% root.after (ms: 50, update_game) # Обновление игры каждые 50 миллисекунд
# Привязываем клавиши для управления
root.bind("<Left>", move_left) root.bind("<Right>", move_right)
# Начинаем обновление игры
update_game
# Запуск игры
root.mainloop
