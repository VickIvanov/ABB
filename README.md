# online-hack



## Требования

- Установить [Docker](https://www.docker.com/products/docker-desktop)
- `git clone https://github.com/VickIvanov/ABB.git`

## Запуск сервера

Перейти в папку проекта:

```bash
docker-compose build
docker-compose up -d
```

Открываем наше приложение: [http://127.0.0.1](http://127.0.0.1)

Для разработки дополнительно доступен прямой доступ к бекенду и БД

- postgre: 127.0.0.1:5432
- pgadmin: 127.0.0.1:5000

## Остановка сервера

```bash
docker-compose down
```
