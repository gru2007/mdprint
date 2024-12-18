import tkinter as tk 
from tkinter import messagebox

class Shape:
	def draw(self, canvas):
		pass # Метод будет переопределен в дочерних классах
class Circle(Shape): 
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius
	def draw(self, canvas): 
		# Рисцем круг
		canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill="blue")
class Rectangle(Shape): 
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
	def draw(self, canvas):
		# Рисуем прямоугольник
		canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="red")
class Triangle(Shape): 
	def __init__(self, x1, y1, x2, y2, x3, y3):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
	def draw(self, canvas):
		# Рисуем прямоугольник
		canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill="green")
		
class ShapeDrawingApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Полиморфизм в Tkinter")
		# Создаем канвас для рисования
		self.canvas = tk.Canvas(self.root, width=500, height=500)
		self.canvas.pack()
		# Кнопки для выбора фигуры
		self.circle_button = tk.Button(self.root, text="Нарисовать круг", command=self.draw_circle)
		self.circle_button.pack(side=tk.LEFT)
		self.rectangle_button = tk.Button(self.root, text="Нарисовать прямоугольник", command=self.draw_rectangle)
		self.rectangle_button.pack(side=tk.LEFT)
		self.triangle_button = tk.Button(self.root, text="Нарисовать треугольник", command=self.draw_triangle)
		self.triangle_button.pack(side=tk.LEFT)
		# Очистить канвас
		self.clear_button = tk.Button(self.root, text="Очистить", command=self.clear_canvas)
		self.clear_button.pack(side=tk.LEFT)
	def draw_circle(self):
		# Создаем объект Circle и рисуем его.
		circle = Circle( 250, 250, 50)
		circle.draw(self.canvas)
	def draw_rectangle(self):
		# Создаем объект Rectangle и рисуем его
		rectangle = Rectangle( 100, 100,  400, 300)
		rectangle.draw(self.canvas)
	def draw_triangle(self):
		# Создаем объект Triangle и pucye его.
		triangle = Triangle(  100,  400, 250,  100, 400,  400)
		triangle.draw(self.canvas)
	def clear_canvas(self):
		# Очищаем канвас
		self.canvas.delete("all")
# Создаем окно приложения
root = tk.Tk()
app = ShapeDrawingApp(root)
root.mainloop()
