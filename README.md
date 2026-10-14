# Clean Order Service

Мини-сервис управления заказами для лабораторной работы N7 по теме "Инструментальные средства разработки ПО".

Проект показывает:

- разделение на слои Clean Architecture;
- инверсию зависимостей через интерфейс репозитория;
- корень композиции в `src/main.py`;
- работу двух реализаций репозитория: in-memory и SQLite;
- логирующий middleware для сценария использования;
- юнит-тесты доменной логики и сценариев использования;
- готовые материалы для отчета и защиты.

## Структура

```text
src/
  domain/          # бизнес-сущности и правила
  use_cases/       # сценарии использования и интерфейсы
  infrastructure/  # внешние адаптеры: память, SQLite, middleware
  main.py          # composition root
tests/             # автоматические тесты
docs/              # отчет и Git-материалы
```

## Запуск в VS Code

1. Открыть папку `clean_order_service` в Visual Studio Code.
2. Выбрать интерпретатор Python 3.10+.
3. В терминале выполнить:

```bash
python -m src.main
python -m unittest discover -s tests
```

## Быстрая проверка

```bash
python -m unittest discover -s tests -v
```

