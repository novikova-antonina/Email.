import smtplib
import os


FRIEND = "%friend_name%"
IAM = "%my_name%"
SITE= "%website%"
letter = """
From: novikovaantonina93a@yandex.ru
To: profil.utch@yandex.ru
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


replacements = {"{FRIEND}":"Арсений", "{IAM}":"Антонина", "{SITE}": "https://dvmn.org/profession-ref-program/novikovantoninalex/ayYBP/"}
for old, new in replacements.items():
    letter = letter.replace(old, new)
    message = letter.encode("UTF-8")
from dotenv import load_dotenv
load_dotenv()  
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail('novikovaantonina93a@yandex.ru', 'profil.utch@yandex.ru', message)
print('My congratulations! See SPAM folder.')
server.quit()