# Видеоплеер

Статическая страница с кастомным видеоплеером на базе `Playable` и `jQuery`.
Проект запускается через `livereload` и автоматически обновляет страницу при изменении `html/css/js`.

<img width="1205" height="859" alt="image" src="https://github.com/user-attachments/assets/53c3e11c-0674-4f32-b719-361c3aed4441" />

## Опубликованный сайт

[Сайт](https://remik202.github.io/video_player_layout/)

## Запуск

1. Установить зависимости:
   `pip install -r requirements.txt`
2. Запустить сервер:
   `python serve.py`
3. Открыть:
   `http://127.0.0.1:8000`

## Открыть без запуска сервера (просто через браузер)

1. Скачайте проект и распакуйте у себя на ПК.
2. Откройте папку проекта:
   `С:\.....\layout_video_player`
3. Откройте файл `index.html` двойным кликом.

## Структура проекта

- `index.html` — основная страница плеера.
- `static/` — статические файлы (`bootstrap`, `font-awesome`, `player.js`, шрифты).
- `media/` — медиафайлы проекта (favicon и другие локальные ресурсы).
- `serve.py` — запуск локального сервера с livereload.

