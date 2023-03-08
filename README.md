# GalkaElbrusTest_bot
Телеграм бот, транслитерирующий ФИО и кириллицы в латиницу в соответствии с правилами МИД РФ  https://t.me/GalkaElbrusTest_bot

## Запуск через Docker
1.Для получения токена создайте бот в телеграм при помощи https://t.me/BotFather  
2.Скопируйте полученный токен в ENV TOKEN=<token> в dockerfile  
3.В терминале создайте образ при помощи команды docker build .  
4.Используя команду docker images получаем IMAGE id 
5.Запуск бота командой docker run -d -p 80:80 <id_image>, подставляя полученный на шаге 4 IMAGE id  
6.Остановка бота  командой docker stop <id_container>. id контейнера можно получить командой docker ps  
