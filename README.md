Проект телеграмм бота-магазина с кошельком и балансом monero(xmr)
 - В разработке!


Установка Docker: Выполните следующие команды для установки Docker:

sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
Перезапустите сервер или выйдите и снова войдите, чтобы изменения вступили в силу.

Установка Docker Compose: Docker Compose используется для оркестрации контейнеров. Чтобы установить его:

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

Проверьте установку:

docker-compose --version
Шаг 2: Подготовка проекта
Склонируйте репозиторий проекта: Если вы не сделали этого ранее, клонируйте репозиторий вашего проекта.

git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd <ПАПКА_С_ПРОЕКТОМ>
Создайте файл .env для переменных окружения: В корне проекта создайте файл .env для хранения переменных окружения:

touch .env

Пример содержимого .env:

TELEGRAM_TOKEN=<ваш_токен_бота_telegram>
MONERO_RPC_LOGIN=user:password
MONERO_RPC_URL=http://127.0.0.1:18081
MONERO_WALLET_PASSWORD=<ваш_пароль_кошелька>
TELEGRAM_TOKEN: токен вашего бота в Telegram.
MONERO_RPC_LOGIN: логин и пароль для доступа к RPC Monero.
MONERO_RPC_URL: URL вашего монеро-узла (если используете локальный).
MONERO_WALLET_PASSWORD: пароль вашего кошелька Monero.

Настройка Docker Compose: Убедитесь, что у вас есть файл docker-compose.yml в корне проекта. Вот пример конфигурации:

yaml
version: '3.8'

services:
  bot:
    build:
      context: ./bot
    environment:
      - TELEGRAM_TOKEN=${TELEGRAM_TOKEN}
      - MONERO_RPC_LOGIN=${MONERO_RPC_LOGIN}
      - MONERO_RPC_URL=${MONERO_RPC_URL}
      - MONERO_WALLET_PASSWORD=${MONERO_WALLET_PASSWORD}
    ports:
      - "5000:5000"
    volumes:
      - ./bot:/app
    depends_on:
      - monero-node

  monero-node:
    image: "monero/monero:v0.18.3.4"
    ports:
      - "18081:18081"  # RPC для Monero
      - "18082:18082"  # Wallet RPC для Monero
    command: ["monerod", "--rpc-bind-ip", "0.0.0.0", "--rpc-bind-port", "18081", "--detach"]
    volumes:
      - monero_data:/root/.bitmonero

volumes:
  monero_data:
Шаг 3: Сборка и запуск проекта
Сборка и запуск контейнеров:

В директории с файлом docker-compose.yml, выполните следующую команду для сборки и запуска контейнеров:

docker-compose up --build -d

Это создаст и запустит два контейнера:

Bot — контейнер с вашим Telegram-ботом.
Monero Node — контейнер с локальным монеро-узлом.
Проверьте статус контейнеров: Для проверки статуса контейнеров используйте команду:

docker-compose ps

Вы должны увидеть оба контейнера с состоянием Up.

Шаг 4: Настройка и использование Monero Wallet RPC
Проверьте доступность Monero RPC: Чтобы убедиться, что RPC сервер для Monero работает, выполните запрос:

curl -u user:password http://127.0.0.1:18081/get_info

Это должен вернуть информацию о текущем состоянии узла.

Проверьте доступность Monero Wallet RPC: Для проверки доступности Wallet RPC, выполните команду:

curl -u user:password http://127.0.0.1:18082/get_balance
Это должен вернуть баланс кошелька.

Шаг 5: Управление и обновление
Логи: Вы можете проверять логи работы бота и Monero Node:

Для бота:

docker-compose logs -f bot

Для Monero Node:

docker-compose logs -f monero-node

Остановка контейнеров: Для остановки всех контейнеров используйте команду:

docker-compose down

Если хотите остановить только один контейнер, например, бот:

docker-compose stop bot

Обновление контейнеров: Для обновления контейнеров выполните команду:
docker-compose pull
docker-compose up --build -d

Шаг 6: Доступ к админ-меню и взаимодействие с ботом
Администрирование:

Администратор может получить доступ к функционалу админ-меню через admin.py и управлять товарами, категориями и пользователями.
Для этого администратор должен быть идентифицирован по Telegram ID, который прописан в конфиге бота.
Пример использования:

Пользователи могут просматривать баланс, историю заказов и делать заказы.
Администраторы могут управлять товарами, категориями и пользователями.

Дополнительные советы:

Проверка портов: Убедитесь, что порты 18081, 18082 и 5000 не блокируются брандмауэром на сервере. Если необходимо, настройте правила в ufw или другом брандмауэре:

sudo ufw allow 18081,18082,5000

Резервное копирование данных: Чтобы сделать резервные копии данных Monero, можно скопировать каталог данных:
docker cp <container_id>:/root/.bitmonero ./backup

Установка Monero CLI и Wallet RPC на сервере Ubuntu 22.04

1. Скачайте Monero CLI
Перейдите на официальную страницу загрузки Monero и выберите версию для Linux. Или используйте команду wget для загрузки.

Скачивание с помощью wget:
wget https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.2.2.tar.bz2

Замените v0.18.2.2 на последнюю доступную версию с сайта Monero.

2. Распакуйте архив
Распакуйте загруженный файл:

bash

tar -xvf monero-linux-x64-v0.18.2.2.tar.bz2

Перейдите в распакованную папку:


cd monero-x86_64-linux-gnu-v0.18.2.2
3. Установите Monero
Скопируйте бинарные файлы в каталог /usr/local/bin для удобства:


sudo cp monerod monero-wallet-cli monero-wallet-rpc /usr/local/bin
Теперь Monero CLI и Wallet RPC доступны из любого места в системе.

4. Настройка Monero Daemon (монерод)
Монерод (Monero Daemon) синхронизирует блокчейн Monero и предоставляет доступ к узлу сети.

Запуск Monero Daemon:

monerod --detach
--detach позволяет запустить процесс в фоне.

По умолчанию Monero Daemon начнет синхронизацию блокчейна. Это может занять значительное время и место на диске (более 100 ГБ).
Альтернатива: Подключение к удаленному узлу
Если вы не хотите синхронизировать весь блокчейн:


monerod --daemon-address=node.moneroworld.com:18081
5. Создайте кошелек
Используйте Monero CLI для создания кошелька:

monero-wallet-cli --generate-new-wallet mywallet
Укажите имя кошелька (mywallet).
Задайте сложный пароль (он понадобится позже для Wallet RPC).
Запишите seed-фразу, которую программа выдаст — она потребуется для восстановления кошелька.
6. Запуск Monero Wallet RPC
Теперь вы можете запустить Monero Wallet RPC, чтобы взаимодействовать с кошельком через API.

Пример команды:

monero-wallet-rpc \
  --wallet-file=/path/to/mywallet \
  --password=<your_wallet_password> \
  --rpc-bind-port=18082 \
  --rpc-login=user:password \
  --daemon-address=node.moneroworld.com:18081
Параметры:

--wallet-file — путь к созданному кошельку.
--password — пароль кошелька.
--rpc-bind-port — порт, на котором работает Wallet RPC (по умолчанию 18082).
--rpc-login — логин и пароль для аутентификации.
--daemon-address — адрес узла Monero Daemon (локального или удаленного).
7. Настройка автозапуска
Если вы хотите, чтобы Monero Daemon и Wallet RPC запускались автоматически при старте сервера, создайте systemd-сервисы.

Systemd-сервис для Monero Daemon:
Создайте файл /etc/systemd/system/monerod.service:


sudo nano /etc/systemd/system/monerod.service
Добавьте в файл:

ini

[Unit]
Description=Monero Daemon
After=network.target

[Service]
ExecStart=/usr/local/bin/monerod --detach
Restart=always
User=root

[Install]
WantedBy=multi-user.target
Сохраните и запустите:


sudo systemctl enable monerod
sudo systemctl start monerod
Systemd-сервис для Wallet RPC:
Создайте файл /etc/systemd/system/monero-wallet-rpc.service:


sudo nano /etc/systemd/system/monero-wallet-rpc.service
Добавьте:

[Unit]
Description=Monero Wallet RPC
After=network.target

[Service]
ExecStart=/usr/local/bin/monero-wallet-rpc \
  --wallet-file=/path/to/mywallet \
  --password=<your_wallet_password> \
  --rpc-bind-port=18082 \
  --rpc-login=user:password \
  --daemon-address=node.moneroworld.com:18081
Restart=always
User=root

[Install]
WantedBy=multi-user.target

Сохраните и запустите:

sudo systemctl enable monero-wallet-rpc
sudo systemctl start monero-wallet-rpc

8. Проверка работы Wallet RPC
Убедитесь, что Wallet RPC работает, отправив тестовый запрос:

curl -u user:password \
     -X POST http://127.0.0.1:18082/json_rpc \
     -d '{"jsonrpc":"2.0","id":"0","method":"get_balance"}' \
     -H "Content-Type: application/json"
Если все настроено правильно, вы получите баланс кошелька.
