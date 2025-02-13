import smtplib
import os
from dotenv import load_dotenv

FRIEND = "%friend_name%"
IAM = "%my_name%"
SITE= "%website%"
sender = "novikovaantonina93a@yandex.ru"
recipient = "profil.utch@yandex.ru"
replacements = {"{sender}":"novikovaantonina93a@yandex.ru","{recipient}":"{profil.utch@yandex.ru}", "{FRIEND}":"Арсений", "{IAM}":"Антонина", "{SITE}": "https://dvmn.org/profession-ref-program/novikovantoninalex/ayYBP/"}
letter = """From: {sender}
To: {recipient}
Subject: Invitation
Content-Type: text/plain; charset="UTF-8";


Привет, {FRIEND}! 

{IAM} приглашает тебя на сайт {SITE}!

{SITE} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {SITE}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {SITE}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""



for old, new in replacements.items():
    letter = letter.replace(old, new)
    message = letter.encode("UTF-8")

load_dotenv()  
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(sender, recipient, message)
server.quit()