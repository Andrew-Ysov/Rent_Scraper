# Парсер жилья в моём городе через группы в вк и авито

## Цель этого проекта:
Оптимизировать поиск жилья, которое можно арендовать, чтобы оно ещё и соответствовало условиям (главным образом касательно цены)

## Задачи, которые должен выполнять проект:
- Поиск вариантов для съёма жилья по заранее определённым группам в вк
- Получение ссылок и фотографий вариантов квартир (домов) для аренды

## Как пользоваться этим проектом:
Первоначально стоит определить набор мест, где будет происходить поиск,
для этого будет использован массив ссылок на группы в вк
При использовании проекта стоит заполнить этот массив ссылками нужных групп

Затем стоит указать границы бюджета, в пределах которого будут показаны варианты

Необходимо указать свой токен для работы с VK API,
о том как его получить можно почитать [здесь](https://dev.vk.com/ru/api/access-token/getting-started).
Нужно создать файл vk_api_token, где в переменную с таким же именем поместить строкой этот ключ

Предварительно нужно установить библиотеки: requests, bs4, lxml

Результаты будут записываться в таблицу и сохраняться в отдельном файле,
а именно в файле будут: цена, адрес и ссылка на объявление

На данный момент парсинг записей из vk работает, но не полноценно, то есть ссылки на записи собираются, 
но текст записей не анализируется и из-за этого записи никак не фильтруются

В отдельном файле есть парсер с сайта (однако им нельзя пользоваться для других сайтов, так как 
на каждом сайте своя разметка и теги, которые использовались для одного сайта не сработают для другого)
