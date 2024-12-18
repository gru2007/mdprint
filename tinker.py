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
	def __init__(self, x1, Y1, X2, Y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
	def draw(self, canvas):
		# Рисуем прямоугольник
		canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="red")
		
	class ShapeDrawingApp: 1 usage def -_init__(self, root):
self.root = root
self.root. title("Полиморфизм в Tkinter")
# Создаем канвас для рисования
self.canvas = tk.Canvas(self.root, width=500, height=500)
self.canvas.pack
# Кнопки для выбора фигуры
self.circle_button = tk.Button(self.root, text="Нарисовать круг"
, command=self.draw_circle)
self.circle_button.pack(side=tk.LEFT)
self.rectangle_button = tk.Button(self.root, text="Нарисовать прямоугольник", command=self.draw_rectangle)
self.rectangle_button.pack(side=tk.LEFT)
self.triangle_button = tk.Button(self.root, text="Нарисовать треугольник", command=self.draw_triangle)
self.triangle_button.pack(side=tk.LEFT)
# Очистить канвас
self.clear_button = tk.Button(self.root, text="Очистить"
, command=self.clear_canvas)
self.clear_button.pack(side=tk.LEFT)
def draw_circle(self): 1 usage
# Создаем объект Circle и рисуем его.
circle = Circle( x: 250, y: 250, radius: 50)
circle.draw(self.canvas)
def draw_rectangle(self): 1 usage
# Создаем объект Rectangle и рисуем его
rectangle = Rectangle( x1: 100, yl: 100, x2: 400, y2: 300)
rectangle.draw(self.canvas)
def draw_triangle(self): 1 usage
# Создаем объект Triangle и pucye его.
triangle = Triangle( x1: 100, y1: 400, x2: 250, y2: 100, x3: 400, y3: 400)
triangle.draw(self.canvas)
def clear_canvas(self): 1 usage
* Очищаем канвас
self.canvas.delete("all")
# Создаем окно приложения
root = tk.TkO
app = ShapeDrawingApp(root)
root.mainloop