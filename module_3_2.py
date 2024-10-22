def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    if '@' not in recipient or '@' not in sender or\
    not recipient.endswith(('.com', 'ru', 'net')) or not sender.endswith(('.com', 'ru', 'net')):
        print("Невозможно отправить письмо с адреса 'arak@utro.du' на адрес narak@vecher.com")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса university.help@gmail.com на адрес arak@utro.ru")

    elif "university.help@gmail.com" not in sender:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса pyton@language.com на адрес control@print.net.")

send_email(message="Идет вебинар", recipient='arak@utro.du', sender='narak@vecher.com')
send_email(message='Hey, bro!', recipient='winter@noch.net', sender='winter@noch.net')
send_email(message='learn python', recipient='arak@utro.ru')
send_email(message="lesson tomorrow", recipient='control@print.net' ,sender='pyton@language.com')