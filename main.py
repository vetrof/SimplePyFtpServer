import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    # Создаем директорию, если она не существует
    root_path = "ftp"  # Измените путь, если нужно, на относительный
    if not os.path.exists(root_path):
        os.makedirs(root_path)

    # Создаем авторизатор и добавляем пользователей
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", root_path, perm="elradfmw")  # Используем root_path
    authorizer.add_anonymous(root_path, perm="elr")

    # Создаем обработчик
    handler = FTPHandler
    handler.authorizer = authorizer

    # Настраиваем и запускаем сервер
    address = ("0.0.0.0", 2121)  # Слушаем все интерфейсы на порту 2121
    server = FTPServer(address, handler)

    print("FTP-сервер запущен на порту 2121...")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
