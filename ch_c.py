def change_color(list_widget, color):
    """Функция меняет цвет виджетам переданных в списке"""
    for widgets in list_widget:
        size_font = widgets[-1]
        for w in widgets[:-1]:
            style = f'font: {size_font}pt "MS Shell Dlg 2"; background-color: rgb(156, 138, 138);'
            w.setStyleSheet(style + ' color: {}'.format(color.name()))
