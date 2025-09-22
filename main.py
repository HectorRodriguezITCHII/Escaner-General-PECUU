import flet as ft
from ui import setup_ui
from scanner import scan_urls_handler
import threading

def main(page: ft.Page):
    page.bgcolor = ft.Colors.GREY_50
    page.title = "Escaneo General"
    page.scroll = True
    page.padding = ft.padding.symmetric(25, 10)
    page.vertical_alignment = ft.CrossAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    text_title, scan_button, results_column, loading_row = setup_ui(page)

    scan_button.on_click = lambda e: threading.Thread(
        target=scan_urls_handler,
        args=(e, results_column, loading_row, scan_button, page)
    ).start()

    page.add(
        ft.Column([text_title], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        ft.Container(content=scan_button, padding=15),
        loading_row,
        results_column
    )

if __name__ == "__main__":
    ft.app(target=main)