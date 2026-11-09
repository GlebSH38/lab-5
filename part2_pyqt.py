"""Лабораторная работа. Вариант 9. Часть 2 (PyQt5).

Реализовано задание:
- Повышенная сложность 9: Приложение PyQt с таблицей.
"""

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class TableApp(QMainWindow):
    """Главное окно приложения с таблицей и кнопкой добавления строк."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Приложение с таблицей")
        self.resize(600, 400)

        # Центральный виджет и компоновка
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Создаем таблицу
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["Имя", "Возраст", "Город"]
        )

        # Тестовые данные для заполнения таблицы
        data = [
            ("Иван", "25", "Москва"),
            ("Мария", "30", "Санкт-Петербург"),
            ("Алексей", "22", "Казань"),
        ]

        for row_idx, row_data in enumerate(data):
            for col_idx, item_text in enumerate(row_data):
                item = QTableWidgetItem(item_text)
                self.table.setItem(row_idx, col_idx, item)

        # Кнопка для добавления пустой строки
        btn_add_row = QPushButton("Добавить строку")
        btn_add_row.clicked.connect(self.add_row)

        # Добавляем элементы на форму
        layout.addWidget(self.table)
        layout.addWidget(btn_add_row)

    def add_row(self):
        """Добавляет пустую строку в конец таблицы."""
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        for col in range(self.table.columnCount()):
            empty_item = QTableWidgetItem("")
            self.table.setItem(row_count, col, empty_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableApp()
    window.show()
    sys.exit(app.exec_())
