# Инструмент для Code Review с использованием GitHub API

## Описание проекта

Этот проект представляет собой инструмент для внутреннего Code Review, разработанный с использованием Django, Celery и GitHub API. Он позволяет автоматизировать процесс проверки кода, собирать метрики и улучшать качество разработки.

## Основные функции

-   **Авторизация через GitHub**: Интеграция с GitHub API с использованием OAuth 2.0 для безопасной аутентификации пользователей.
-   **Получение пулл-реквестов и коммитов**: Автоматический сбор информации о пулл-реквестах и коммитах из репозиториев GitHub.
-   **Оценка качества кода**: Возможность оценивать изменения в коде и выставлять оценки (например, от 1 до 5).
-   **Комментирование кода**: Встроенная система комментариев для каждого пулл-реквеста, позволяющая оставлять замечания и предложения.
-   **Анализ метрик**: Сбор и анализ метрик для улучшения процесса ревью (время, количество комментариев, рейтинг качества кода и т. д.).
-   **Автоматические уведомления**: Уведомления о новых пулл-реквестах.

## Технологии

-   **Backend**: Django
-   **Интеграция с GitHub**: GitHub API, OAuth 2.0
-   **База данных**: PostgreSQL
-   **Асинхронные задачи**: Celery, Redis
-   **Кэширование**: Redis
-   **Контейнеризация**: Docker, Docker Compose
-   **Документация API**: drf-spectacular

## Установка

1.  Клонируйте репозиторий:
    
    ```bash
    git clone https://github.com/Rhae9ar/code_review_tool.git
    ```
    
2.  Создайте виртуальное окружение:
    
    ```bash
    python -m venv venv
    ```
    
3.  Активируйте виртуальное окружение:
    
    ```bash
    source venv/bin/activate # Для Linux/macOS
    venv\Scripts\activate # Для Windows
    ```
    
4.  Установите зависимости:
    
    ```bash
    pip install -r requirements.txt
    ```
    
5.  Настройте базу данных в `core/settings.py`.
6.  Выполните миграции:
    
    ```bash
    python manage.py migrate
    ```
    
7.  Запустите сервер:
    
    ```bash
    python manage.py runserver
    ```
    

## Настройка Celery и Redis

1.  Запустите Redis:
    
    ```bash
    redis-server
    ```
    
2.  Запустите Celery worker:
    
    ```bash
    celery -A core worker -l info
    ```
    
3.  Запустите Celery beat:
    
    ```bash
    celery -A core beat -l info
    ```
    

## Документация API

Документация API доступна по адресу `http://localhost:8000/api/schema/swagger-ui/` после запуска сервера.

## Контейнеризация

Для запуска проекта в Docker выполните:

```bash
docker-compose up --build
