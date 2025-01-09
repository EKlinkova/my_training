import re
def isvalidemail(email):
    """
    Проверяет, является ли строка email адресом.
    Условия:
    1. Должен содержать символ "@"
    2. Должен оканчиваться на ".com", ".ru" или ".net"
    """
    # Регулярное выражение для проверки корректности email
    pattern = r'^[\w\.\+\-]+\@[\w\-]+\.[a-z]{2,4}$'
    return bool(re.match(pattern, email))


def send_email(message, recipient, sender="university.help@gmail.com"):
    """
    Отправляет email-сообщение.
    :param message: Сообщение, которое будет отправлено.
    :param recipient: Адрес получателя.
    :param sender: Адрес отправителя, по умолчанию "university.help@gmail.com".
    """
    # Проверка корректности email адресов
    if not isvalidemail(sender) or not isvalidemail(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на совпадение адресов sender и recipient
    if sender == recipient:
        print(f"Невозможно отправить письмо, так как адреса совпадают: {sender}")
        return
    # Логика отправки письма
    # Здесь можно подключить библиотеку для отправки реальных email,
    # например smtplib, если необходимо.
    print(f"Сообщение от {sender} отправлено {recipient}: {message}")


# Примеры использования функции
send_email("Привет, как дела?", "student@example.com")
send_email("Привет, как дела?", "student@example")
send_email("Привет, как дела?", "university.help@gmail.com", "university.help@gmail.com")
### Описание:
# 1. Функция isvalidemail(email):- Использует регулярное выражение для проверки корректности email.Принимает
# строку email и возвращает True, если она корректна и False в противном случае.
# 2. Функция send_email(message, recipient, sender="university.help@gmail.com"):
# - Принимает сообщение, адрес получателя и(необязательный) адрес отправителя.
# - Проверяет корректность адресов и выводит соответствующие сообщения об ошибках.
# - Проверяет, совпадают ли адреса отправителя и получателя.
# - Если все проверки пройдены, выводит сообщение об успехе.
# Если вам нужно добавить реальную отправку писем, вы можете использовать библиотеку smtplib, но
# для простоты в этом примере мы просто выводим информацию на консоль.