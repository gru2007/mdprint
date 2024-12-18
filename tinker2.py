import tkinter as tk 
import random
# Создаем главное окно
root = tk.Tk()
root.title("Избегай блоки")
# Устанавливаем размеры окна и канваса
WIDTH, HEIGHT = 400, 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
# Игрок
player = canvas.create_rectangle(175, 350, 225, 375, fill="blue")
# Переменные для управления
player_speed = 20
game_over = False
# Список для хранения падающих блоков
blocks = []
# Функции для управления игроком
def move_left(event):
     if not game_over:
        canvas.move ( player, -player_speed, 0)
def move_right(event): 
    print('right')
    if not game_over:
        canvas.move(player, player_speed, 0)
# Функция для создания падающих блоков с меньшей вероятностью
def create_block():
    if not game_over and random.random() < 0.02: # 2% шанс появления блока
        x= random.randint(0, WIDTH - 30)
        block = canvas.create_rectangle(x, 0, x + 30, 20, fill="red")
        blocks.append(block)
# Функция для обновления игры
def update_game():
    global game_over
    if game_over:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Игра окончена", font=("Arial", 20), fill="black")
        return
    
    # Двигаем падающие блоки
    blocks_to_remove = [] # Список для блоков, которые надо удалить
    for block in blocks:
        canvas.move(block, 0, 5) # Каждый блок падает вниз на 5 пикселей if canvas.coords(block)[3] > HEIGHT: # Если блок выходит за экран blocks_to_remove.append(block) # Отмечаем блок на удаление
        
        # Проверка на столкновение
        if canvas.coords(block)[3] > HEIGHT:
            blocks_to_remove.append(block)
        else:
            if canvas.coords(block)[1] >= canvas.coords(player)[1] and \
            canvas.coords(block)[2] >= canvas.coords(player)[0] and \
            canvas.coords(block)[0] <= canvas.coords(player)[2]:
                game_over = True
        # удаляем блоки, которые вышли за экран или столкнулись с игроком
        for block in blocks_to_remove:
            canvas.delete(block)
            blocks.remove(block)

 # Пытаемся создать новый блок с вероятностью 2% 
    create_block()
    root.after (50, update_game) # Обновление игры каждые 50 миллисекунд

# Привязываем клавиши для управления
root.bind("<Left>", move_left) 
root.bind("<Right>", move_right)
# Начинаем обновление игры
update_game()
# Запуск игры
root.mainloop()
