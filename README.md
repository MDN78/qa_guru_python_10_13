## Задание 13 Управляем параметрами в коде и в Jenkins

1. Доработать свой код на регистрационную форму с аллюровскими степами

2. Доработать код, чтобы он запускался не локально, а браузер в selenoid.autotests.cloud

3. Добавить аттачменты - скриншот, логи консоли, page source, видео

4. Сделать сборку в jenkins.autotests.cloud (регистрация открыта) с кодом

5. Передать из дженкинса адрес удаленного браузера

6. Спрятать логин/пароль к удаленному браузеру в .env файл

### добавил логирование - файл `logger.py` и добавил аттач файла в отчет аллюр

## Уведомление в Телеграмм локально:  
Добавил локальную нотификацию - создал папку `notifications`  
в нее добавил два файла скачанный [allure-notification](https://github.com/qa-guru/allure-notifications/releases)  
файл `config.json` и заполнил под нужный мессенджер  
Запустил локально тесты стандартной командой  
далее в терминале 
```commandline
allure generate allure-results 
```

затем  
```commandline
java "-DconfigFile=notifications/config.json" -jar notifications/allure-notifications-4.6.1.jar 
```

И нотификация прошла

### доп информация

[wiki info](https://github.com/MDN78/qa_guru_python_10_13/wiki)

[allure notifications](https://github.com/qa-guru/allure-notifications)

