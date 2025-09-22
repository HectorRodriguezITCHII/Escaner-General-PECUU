import flet as ft

def setup_ui(page: ft.Page):
    text_title = ft.Text(
        value="ESCANEO GENERAL",
        size=32,
        color=ft.Colors.INDIGO_700,
        weight="bold",
    )

    scan_button = ft.FilledButton(
        text="ESCANEAR", 
        width=200, 
        height=50, 
        bgcolor=ft.Colors.INDIGO_700, 
        color=ft.Colors.WHITE, 
        style=ft.ButtonStyle(text_style=ft.TextStyle(size=22, weight="bold")),
    )
    
    results_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment = ft.CrossAxisAlignment.CENTER
    )

    loading_indicator = ft.ProgressRing(width=30, height=30, stroke_width=4)
    status_text = ft.Text(value="", size=20)

    loading_row = ft.Row(
        controls=[loading_indicator, status_text],
        alignment=ft.MainAxisAlignment.CENTER,
        visible=False
    )

    return text_title, scan_button, results_column, loading_row