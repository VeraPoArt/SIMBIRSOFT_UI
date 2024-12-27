# Проект автотестов для http://uitestingplayground.com


    tests/ – сами тесты.
    pages/ – реализация Page Object Model (POM).
    conftest.py – общие фикстуры (например, driver) и команды (pytest_addoption) для запуска в разных браузерах.
    pytest.ini – конфигурация Pytest (например, --reruns, --reruns-delay, регистрация маркировок).
    requirements.txt – список Python-зависимостей.
    README.md – данное руководство.

## Установка зависимостей
`pip install -r requirements.txt`

## Запуск тестов

Все тесты запускаются через Pytest. Базовая команда (из корня проекта):
`pytest`

## Параллельный запуск тестов

Для параллельного запуска необходимо:

    Установить плагин pytest-xdist 

    Запустить тесты с параметром -n [число_воркеров], например:

`pytest -n 4`

Это запустит тесты в 4 параллельных потоках.

## Запуск только упавших тестов

Если при предыдущем прогоне были упавшие тесты, вы можете запустить только их:

`pytest --last-failed`

## Генерация отчётов Allure
`pytest --alluredir=allure-results`

После завершения тестов:

`allure serve allure-results`

