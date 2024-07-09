# импортируется объект `app` из модуля `app`
from app import app

# - проверяется условие, если переменная `name` равна строке "main"
if __name__ == "__main__":
# запускается Flask-приложение с включенным режимом отладки (debug=True)
    app.run(debug=True)