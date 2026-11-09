"""Лабораторная работа. Вариант 9. Часть 1 (Tkinter).

Реализованы задания:
- Средняя сложность 1: Окно с кнопкой «Привет».
- Средняя сложность 6: Прогрессбар.
- Средняя сложность 9: Цветная панель.
- Повышенная сложность 2: Рисование фигур мышью.
"""

import random
import time
import tkinter as tk
from tkinter import ttk


def task1_greet():
    """Открывает окно с кнопкой, выводящей приветствие."""
    greeting_window = tk.Toplevel(root)
    greeting_window.title("Задание 1: Привет")
    greeting_window.geometry("250x120")

    def show_hello():
        """Выводит текст приветствия в окно."""
        label = tk.Label(
            greeting_window,
            text="Привет, мир!",
            font=("Arial", 14)
        )
        label.pack(pady=10)

    btn = tk.Button(
        greeting_window,
        text="Нажми меня",
        command=show_hello
    )
    btn.pack(pady=20)


def task6_progress():
    """Открывает окно с прогрессбаром, заполняющимся по кнопке."""
    progress_window = tk.Toplevel(root)
    progress_window.title("Задание 6: Прогрессбар")
    progress_window.geometry("300x150")

    progress = ttk.Progressbar(
        progress_window,
        orient="horizontal",
        length=200,
        mode="determinate"
    )
    progress.pack(pady=20)

    def start_progress():
        """Анимирует заполнение прогрессбара от 0 до 100%."""
        progress['value'] = 0
        for i in range(1, 101):
            progress['value'] = i
            # Принудительно обновляем интерфейс
            progress_window.update()
            # Небольшая задержка для видимости анимации
            time.sleep(0.02)

    btn = tk.Button(
        progress_window,
        text="Запустить",
        command=start_progress
    )
    btn.pack()


def task9_color_panel():
    """Открывает окно с цветной панелью, меняющей цвет по кнопке."""
    color_window = tk.Toplevel(root)
    color_window.title("Задание 9: Цветная панель")
    color_window.geometry("300x200")

    colors = [
        "red", "green", "blue",
        "yellow", "purple", "orange"
    ]

    panel = tk.Frame(
        color_window,
        bg="grey",
        width=200,
        height=100
    )
    panel.pack(pady=20)

    def change_color():
        """Меняет цвет панели на случайный из списка."""
        new_color = random.choice(colors)
        panel.config(bg=new_color)

    btn = tk.Button(
        color_window,
        text="Сменить цвет",
        command=change_color
    )
    btn.pack()


def task_high2_draw():
    """Открывает окно для рисования фигур мышью."""
    draw_window = tk.Toplevel(root)
    draw_window.title("Задание Повыш. 2: Рисование мышью")
    draw_window.geometry("500x400")

    canvas = tk.Canvas(
        draw_window,
        bg="white",
        width=480,
        height=350
    )
    canvas.pack(pady=10)

    # Переменные для хранения координат начала рисования
    start_x = None
    start_y = None
    shape_type = tk.StringVar(value="oval")

    def start_draw(event: tk.Event):
        """Запоминает координаты нажатия кнопки мыши."""
        nonlocal start_x, start_y
        start_x, start_y = event.x, event.y

    def finish_draw(event: tk.Event):
        """Рисует фигуру от начальной до конечной точки."""
        if start_x is None or start_y is None:
            return

        if shape_type.get() == "oval":
            canvas.create_oval(
                start_x, start_y, event.x, event.y,
                outline="black", width=2
            )
        elif shape_type.get() == "rect":
            canvas.create_rectangle(
                start_x, start_y, event.x, event.y,
                outline="black", width=2
            )
        elif shape_type.get() == "line":
            canvas.create_line(
                start_x, start_y, event.x, event.y,
                fill="black", width=2
            )

    # Привязка событий мыши к холсту
    canvas.bind("<ButtonPress-1>", start_draw)
    canvas.bind("<ButtonRelease-1>", finish_draw)

    # Фрейм для выбора типа фигуры
    frame = tk.Frame(draw_window)
    frame.pack()

    for text, value in [
        ("Овал", "oval"),
        ("Прямоугольник", "rect"),
        ("Линия", "line")
    ]:
        rb = tk.Radiobutton(
            frame,
            text=text,
            variable=shape_type,
            value=value
        )
        rb.pack(side=tk.LEFT)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Лабораторная работа (Вариант 9)")
    root.geometry("400x300")

    title_label = tk.Label(
        root,
        text="Выберите задание:",
        font=("Arial", 14, "bold")
    )
    title_label.pack(pady=20)

    # Кнопки для вызова каждого задания
    tasks = [
        ("1. Кнопка «Привет» (Средняя 1)", task1_greet),
        ("6. Прогрессбар (Средняя 6)", task6_progress),
        ("9. Цветная панель (Средняя 9)", task9_color_panel),
        ("2. Рисование мышью (Повышенная 2)", task_high2_draw)
    ]

    for text, command in tasks:
        btn = tk.Button(root, text=text, command=command, width=35)
        btn.pack(pady=5)

    root.mainloop()
