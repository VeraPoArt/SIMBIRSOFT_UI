# Проект автотестов

## Описание проекта
Автоматизация тестирования функционала веб-приложения.

### Основные технологии
- Python
- Selenium
- Allure

## Установка зависимостей
pip install -r requirements.txt

## Запуск тестов
    pytest --alluredir=allure-results

## Отчёт Allure
    allure serve allure-results

### **Инструкция для запуска автотестов с Allure-отчётами**

#### Шаги:
1. **Убедитесь, что Allure CLI установлен.**
   - Для Windows: скачайте с [официального сайта Allure](https://github.com/allure-framework/allure2/releases).
   - Для macOS/Linux: установите через `brew` или `apt`.

2. **Запустите тесты:**
   ```bash
   pytest --alluredir=allure-results
   
2. **Откройте Allure-отчёт:**
   ```bash
   allure serve allure-results
