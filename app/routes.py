# импорт библиотек и приложения
from flask import render_template, request, redirect, url_for
from app import app

# Список для хранения заполненных форм
blanks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # Проверяем метод запроса
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')

        # Проверяем, что все поля заполнены
        if name and age and city and hobby:
            # Добавляем данные в список
            blanks.append({'name': name, 'age': age, 'city': city, 'hobby': hobby})
            return redirect(url_for('index'))  # Перенаправляем на главную страницу после добавления данных

    # Отображаем шаблон 'blank.html' с переданным списком заполненных форм
    return render_template('blank.html', blanks=blanks)