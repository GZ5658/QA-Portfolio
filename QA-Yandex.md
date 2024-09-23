# <a name="up" />Портфолио QA-Yandex

В портфолио собраны проекты, выполненные во время обучения по специальности [Инженер по тестированию Плюс](https://practicum.yandex.ru/qa-engineer-plus/) в Яндекс.Практикуме.

[Проектирование тестов](#test-design)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тест-анализ | Mind map | Серые зоны<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тест-дизайн | Классы эквивалентности | Граничные значения<br>
<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тестовая документация | Чек-листы | Тест-кейсы-->

[Тестирование веб-приложений](#web-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DevTools | Charles<br>

[Тестирование мобильных приложений](#mobile-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Таблицы принятия решений | попарное тестирование | Баг-репорты<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Эмуляторы | Android Studio

[Тестирование API](#api-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;REST API | JSON | Postman

[Тестирование баз данных](#data-bases)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Консоль | SQL | PostgreSQL

[Основы автоматизации тестирования](#test-automation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python

<details>
<summary><h2><a name="test-design" />Проектирование тестов </h2></summary>

### Тест-анализ. Mind map. Серые зоны

**1. Mindmap**

Изучи [требования к Яндекс Маршрутам](https://disk.yandex.ru/i/G3a6N1qfxbpUwg).
Создай mindmap: структурируй и декомпозируй всю информацию из требований, а потом представь её в графическом виде.

**2. Новая фича: mindmap**

1. Проанализируй [требования к новой фиче](https://disk.yandex.ru/i/_237O6PKcly3Kw).
2. Создай ещё одну mindmap: отобрази, как изменится функциональность приложения после добавления фичи.

**3. Серые зоны**
 Если встретишь серые зоны, составь запрос на уточнение в шаблоне гугл-дока.
    - В первой строке укажи, кому из команды Движа адресуешь письмо.
    - Дальше подробно сформулируй запрос — так, будто пишешь настоящее письмо коллеге.
<details>
<summary><h3> Решение </h3></summary>

**1. Mindmap**

![Mindmap](https://s665sas.storage.yandex.net/rdisk/e44815f3bf8e818a2cd87d324f5193ac2369fa2a4baa87622906ff30eec06ba3/66ec1880/cLka90c0RtHR-J6qcog-7ZA3d9-z6Fk7GA-eEyaEYFYytFykU5q5lJvJnomVyBS4KJcU4qilmbcjpI01BydSjA==?uid=1118579539&filename=Mind%20map.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1118579539&fsize=773499&hid=5ea4110d9f2b7ac08ad8b294444f5848&media_type=image&tknv=v2&etag=3177560ee04df31fcef1f3b0601411a2&ts=6227808d72000&s=249e75ea1b2a35669bd590f740929938873fce3e34bbb939fce38e17ad40e30a&pb=U2FsdGVkX1_qJMn4BxRhpwZO8tI8mAYq7q_LcoOEQ0tvv8LcMrqBDo6mqoeW4mmU2NVCgrvpExzEaRw89I45EFLOVG9SR0bdRE8r18MAGes)

[Mindmap в большом разрешении](https://i.ibb.co/vLMP7X8/yandex-routes.png)

[Блок схема](https://downloader.disk.yandex.ru/preview/9c7070077097359d479bb0d92ef1c4375eb7c6948467854756ad1dd7fdd9d318/66f1748e/mEsF7H3r567gsM9DJd1PprUBqGcfIDpt-OIGfhAXtbcYniWYYcRO_W2sbPyC85YhIQTSdWJN-y9DFtC35FFoBQ%3D%3D?uid=0&filename=Блок%20схема.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048)

**2. Mindmap фичи**

![Mindmap фичи](https://downloader.disk.yandex.ru/preview/78f69d3fe1baba5eae1b93c0d01712eac4d47ee94e74040731d21d124cb7e453/66ec1b46/azcsURrCMw7q4zY-tpz9Us5eXlmUcrsUOYZ5ys-8rqf9SHVbCGhRfvRHYfeifNM0ZmOOVzZSi7E_d14gmikIhg%3D%3D?uid=0&filename=Mind%20map%20Фича%201.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048)

![Mindmap фичи](https://downloader.disk.yandex.ru/preview/e70b16905418a3dfd73ad1afbb716294031bd74113023bbe4c328542f9f270dc/66ec1ae1/cydfbRPIy_LKdRee_9pwCs5eXlmUcrsUOYZ5ys-8rqd9WumpYW6L-vHY38MUn7fAYPqCCuz0xVYk3N14Bb6yAg%3D%3D?uid=0&filename=Mind%20map%20Фича%202.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048)

[Mindmap фичи в большом разрешении](https://miro.com/app/board/uXjVMNktZBA=/?share_link_id=728346512324)

**3. Запрос на уточнение серых зон**

Менеджеру

	Привет Менеджер! В требованиях к Яндекс Маршрутам 1.0 для Поля ввода минут не указан диапазон ввода целых чисел. Смею предположить, что он составит от 0 до 59 включительно

Дизайнеру

	Привет Дизайнер! В требованиях к Яндекс Маршрутам 1.0 на первом изображении Макета в картах отсутствует “Открыть в Яндекс Картах” (нижний левый угол)

Менеджеру

	Привет Менеджер! В требованиях к Яндекс Маршрутам 1.0 в изображении на Макете в картах присутствуют кнопки масштабирования “+” “-” и ползунок, информации по ним нет, должны ли они присутствовать и алгоритм их работы

Разработчику

	Привет Разработчик! В требованиях к Яндекс Маршрутам 1.0 не указано про возможность выбора адреса не вводом в Поле Адреса, а путем кликанья по области в Картах. Будет ли такой способ построения маршрута?

Менеджеру

	Привет Менеджер! В требованиях к Яндекс Маршрутам 1.0 для нет информации по нижнему блоку:

    - Будет ли осуществляться переход на главную страницу Яндекс Карты по клику на “Открыть в Яндекс Картах” (расположена в левом нижнем углу карты)

    - Будет ли осуществляться переход на страницу с Условиями использования по клику на “Условия использования” (расположена в правом нижнем углу карты)
    по верхнему блоку:
    - Кликабельны ли слова “Яндекс” и “Маршруты”, будет ли осуществляться переход на главную страницу Яндекс и ЯндексМаршруты соответственно 

Аналитику

	Привет Аналитик! При указании адреса в приложении может возникнуть такое, что произойдет совпадение название улиц и домов расположенных в разных городах, например адрес Можайское шоссе, дом 46 расположен как в Одинцово, так и в Москве.

Менеджеру

	Привет Менеджер! В требованиях к Яндекс Маршрутам 1.1 Режим Курьер указано расхождение в скидке на Самокат, указано два значения 3.5 рубля и 2 рубля. Какое из двух значений верно?

Менеджеру

	Привет Менеджер! В требованиях к Яндекс Маршрутам 1.1 Режим Курьер указано “При включенном переключателе в режиме расчёта «Свой» блокируется выбор такси и каршеринга”, а также имеется информация “Курьеры передвигаются на велосипедах, самокатах, пешком или на своём автомобиле, поэтому при включенном чек-боксе нельзя построить маршрут на такси или каршеринге”, какое из двух требований актуально?

</details>

### Тест-дизайн. Классы эквивалентности. Граничные значения

**1. Проверка формы добавления прав: КЭ и ГЗ**
Необходимо роверить корректность валидации данных в форме добавления прав. Тебе нужны следующие поля:<br>
«Имя»,<br>
«Фамилия»,<br>
«Дата рождения»,<br>
«Номер».

**2. Переходы между всплывающими окнами: Диаграмма состояний переходов**
В приложении много разных экранов и всплывающих окон. Нужно проверить, что все переходы между ними работают правильно. 

**3. Таблица принятия решений для кнопки «Забронировать**
Необходимо подготовить таблицу принятия решений для кнопки "Забронировать".

<details>
<summary><h3> Решение </h3></summary>

**1. Проверка формы добавления прав: КЭ и ГЗ**

![Проверка формы добавления прав: КЭ и ГЗ](https://downloader.disk.yandex.ru/preview/220c22ba8eefd284b90169e23f8784326d35f5dcb99c4c69cfca1c50a9c9f3ce/66ec2584/7zBbuElXtpX5JXGSXq1ZGrTUHXG1m1wgXxBLBz2U-p5MZkBje_KdeAJEUNfO53BVvLR0vLJEg3bsYlBFnPK2jg%3D%3D?uid=0&filename=Проверка%20формы%20добавления%20прав%20КЭ%20и%20ГЗ.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Проверка формы добавления прав: КЭ и ГЗ](https://docs.google.com/spreadsheets/d/1RdbmEzG8MV9FE-UEEQKEvcykeCJiniKX/edit?usp=sharing&ouid=106744543532953560427&rtpof=true&sd=true)

**2. Переходы между всплывающими окнами: Диаграмма состояний переходов**

Диаграмма состояний переходов

![Диаграмма состояний переходов](https://downloader.disk.yandex.ru/preview/dc02338b7f7b712bef6b2b6c0c5f941ef207991a5b55a164954348a404bd9490/66ec26c6/FATobBTblnI_BUhsiZAHlGOgDe2yjspzOWf9akp8hu7wLCIMRC9X3hBU_pajt4kDmGOWgQmmHcgVy-LVgrCmZw%3D%3D?uid=0&filename=Диаграма%20состояний%20переходов.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

**3. Таблица принятия решений для кнопки «Забронировать**

[Таблица принятия решений](https://docs.google.com/spreadsheets/d/1RdbmEzG8MV9FE-UEEQKEvcykeCJiniKX/edit?usp=sharing&ouid=106744543532953560427&rtpof=true&sd=true)

![Таблица принятия решений](https://downloader.disk.yandex.ru/preview/6804292df2e55ce10a4a3d568ca6cd2030944d57d914b4a3c1639a29849d84fe/66ec28e0/0_0kwqBkC-2_aRc9DSrS3kPuYGSRxdc2eXGdV3vpIhBepZNaJ4FWIIaMrdUvWc6MvBQ5vgl4uX54YpJgBIYqpA%3D%3D?uid=0&filename=Таблица%20принятия%20решений.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)


</details>

<!--### Тестовая документация | Чек-листы | Тест-кейсы

**1. Переходы между всплывающими окнами: Чек лист**

Составить чек лист проверки переходов между окнами


**2. Тест кейсы для кнопки «Забронировать**

Составить тест кейсы для кнопки "Забронировать"

<details>

<summary><h3> Решение </h3></summary>

**1. Переходы между всплывающими окнами: Чек лист**

Чек лист:
- При нажатии на кнопку “Забронировать” открывается Форма Бронирования
- При нажатии на кнопку “Назад” в Форме бронирования можно вернуться к выбору режимов в Форме Яндекс Маршрутов
- При нажатии на кнопку “Добавить права” - открывается Форма добавления прав
- Форма добавления прав закрывается по нажатию на кнопку “Крестик”
- Форма добавления прав закрывается по нажатию на кнопку “Отмена”
- При нажатии на кнопку “Добавить” в Форме добавления прав, открывается Информационное окно “Спасибо! Документы отправлены на проверку. Скоро расскажем о результатах”
- При нажатии на кнопку “Принято” в Информационном окне  “Спасибо! Документы отправлены на проверку. Скоро расскажем о результатах” можно перейти в Форму бронирования
- При нажатии на кнопку “Крестик” в Информационном окне  “Спасибо! Документы отправлены на проверку. Скоро расскажем о результатах” можно перейти в Форму бронирования
- При нажатии на кнопку “Способ оплаты” открывается Окно Способ оплаты
- При нажатии на кнопку “Добавить карту” откроется Форма Добавление карты
- Форма Добавления карты закрывается по нажатию на кнопку Крестик
- Форма Добавления карты закрывается по нажатию на кнопку Отмена
- При нажатии на кнопку “Привязать” в Форме Добавление карты  открывается Окно Способ оплаты
- При нажатии на кнопку “Забронировать” в Форме Бронирования открывается Информационное окно “Машина забронирована”
- При нажатии на “Крестик” в Информационном окне “Машина забронирована” открывается Окно “Вы уверены, что хотите отменить поездку?”
- При нажатии на кнопку Нет в Окне “Вы уверены, что хотите отменить поездку?” открывается Информационное окно “Машина забронирована”
- При нажатии на кнопку ДА в Окне “Вы уверены, что хотите отменить поездку?” открывается Окно “Поездка отменена”
- При нажатии на кнопку “Принято” открывается Форма Яндекс маршруты (Комментарий: тут конечно чистая импровизация, потому что, ни на Виртуальном сервере, ни в Требованиях к Яндекс Маршрутам нет возможности проверить действие этой кнопки, у меня даже на Виртуальном сервере не кликается кнопка Отмена в Окне Машина Забронирована поэтому не были добавлены пункты после нажатия на кнопку Отмена, в Макетах конечно есть данные на нажатие кнопки Отмена, но в задании так же есть Инфа Если требования и макеты не сходятся — ориентируйся на требования………. )

**2. Тест кейсы для кнопки «Забронировать**

</details>
</details>-->

</details>


<details>
<summary><h2><a name="web-testing" />Тестирование веб-приложений </h2></summary>

### DevTools. Charles

**1. Протестировать новую функциональность — аэротакси (Charles)**

Задача — протестировать реализацию на фронтенде, не дожидаясь бэкенда. Для этого придётся поработать в Charles.
Используй только одно окружение: Яндекс.Браузер.
Изучи требования к новой фиче.
Запусти Яндекс Маршруты и подмени ответы от бэкенда, чтобы отобразить новый тип транспорта. В интерфейсе должен появиться расчёт стоимости и времени поездки.

<details>
<summary><h3> Решение </h3></summary>

**1. Протестировать новую функциональность — аэротакси (Charles)**

[Оригинальный ответ с видами транспорта Charles](https://downloader.disk.yandex.ru/preview/2cc0f91104bc2fed7038ed2304fc2fa759279c3efd80bd76d70f92c59e548560/66ed6506/12BP3PoB2Y-tP_46fLCjdnhxtuq1AkjCD-avvNFvVyse_n1LlRMnM9LMcfHRjvJUpEf68qil8J8iPginUMWBlA%3D%3D?uid=0&filename=1%20Ориг%20ответ%20с%20видами%20транспорта%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![Оригинальный ответ с видами транспорта Charles](https://downloader.disk.yandex.ru/preview/2cc0f91104bc2fed7038ed2304fc2fa759279c3efd80bd76d70f92c59e548560/66ed6506/12BP3PoB2Y-tP_46fLCjdnhxtuq1AkjCD-avvNFvVyse_n1LlRMnM9LMcfHRjvJUpEf68qil8J8iPginUMWBlA%3D%3D?uid=0&filename=1%20Ориг%20ответ%20с%20видами%20транспорта%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Изменённый ответ с видами транспорта из Charles](https://downloader.disk.yandex.ru/preview/5a28ba5db938ccd113039794d7b59c50f82799c95f6d9a8ce9ae0955d027469d/66ed662f/kRn-afO_jaNF9xsNO9_yG3hxtuq1AkjCD-avvNFvVyvhRiniTvX_aNOXiB7lsxzLrJTfKeuhzos4w6sTSYyzPw%3D%3D?uid=0&filename=2.%20Изменённый%20ответ%20с%20видами%20транспорта%20из%20Charles..PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![Изменённый ответ с видами транспорта из Charles](https://downloader.disk.yandex.ru/preview/5a28ba5db938ccd113039794d7b59c50f82799c95f6d9a8ce9ae0955d027469d/66ed662f/kRn-afO_jaNF9xsNO9_yG3hxtuq1AkjCD-avvNFvVyvhRiniTvX_aNOXiB7lsxzLrJTfKeuhzos4w6sTSYyzPw%3D%3D?uid=0&filename=2.%20Изменённый%20ответ%20с%20видами%20транспорта%20из%20Charles..PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Окно с настройками автоматического ответа по видам транспорта из Charles](https://downloader.disk.yandex.ru/preview/9eabd08464ddd8126c6caefee3c7cd9bcd7e14a3dfe0bf1d333c6486d52ab174/66ed6652/gWOAM47Q7oZCTJaAhYUYyXhxtuq1AkjCD-avvNFvVyuAIqJ6G3COyC6nuDgT7S24arYl5zerdFFdjOai9hknUg%3D%3D?uid=0&filename=3.%20Окно%20с%20настройками%20автоматического%20ответа%20по%20видам%20транспорта%20из%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![Окно с настройками автоматического ответа по видам транспорта из Charles](https://downloader.disk.yandex.ru/preview/9eabd08464ddd8126c6caefee3c7cd9bcd7e14a3dfe0bf1d333c6486d52ab174/66ed6652/gWOAM47Q7oZCTJaAhYUYyXhxtuq1AkjCD-avvNFvVyuAIqJ6G3COyC6nuDgT7S24arYl5zerdFFdjOai9hknUg%3D%3D?uid=0&filename=3.%20Окно%20с%20настройками%20автоматического%20ответа%20по%20видам%20транспорта%20из%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Оригинальный ответ с расчётом стоимости и длительности поездки из Charles](https://downloader.disk.yandex.ru/preview/e4f61e148c9db2717f544c95c900313ea6e0894505e93e8e5005d24000836eb9/66ed666e/_MzY5rwV1c57KJHMkisa_nhxtuq1AkjCD-avvNFvVyuV0sMvhFYqdO0R7wbfrtL1C4MTtVqqxMeHyTkys3_v0g%3D%3D?uid=0&filename=4.%20Оригинальный%20ответ%20с%20расчётом%20стоимости%20и%20длительности%20поездки%20из%20DevTools%20или%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![Оригинальный ответ с расчётом стоимости и длительности поездки из Charles](https://downloader.disk.yandex.ru/preview/e4f61e148c9db2717f544c95c900313ea6e0894505e93e8e5005d24000836eb9/66ed666e/_MzY5rwV1c57KJHMkisa_nhxtuq1AkjCD-avvNFvVyuV0sMvhFYqdO0R7wbfrtL1C4MTtVqqxMeHyTkys3_v0g%3D%3D?uid=0&filename=4.%20Оригинальный%20ответ%20с%20расчётом%20стоимости%20и%20длительности%20поездки%20из%20DevTools%20или%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Изменённый ответ с расчётом стоимости и длительности поездки из Charles](https://downloader.disk.yandex.ru/preview/5f8a7c4298c05e1b646a39a4add70b3a3489736ad982da4f36d8e9142c690f13/66ed6687/GopyMazLfl_mXzYYt9LV4cL785hrJws4kSNCdeDDWz6mfWGJEBW2eSp-cIyw7yXqeYChqJBCbuEy9NfnaPX10A%3D%3D?uid=0&filename=5.%20Изменённый%20ответ%20с%20расчётом%20стоимости%20и%20длительности%20поездки%20из%20Charles..PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![Изменённый ответ с расчётом стоимости и длительности поездки из Charles](https://downloader.disk.yandex.ru/preview/5f8a7c4298c05e1b646a39a4add70b3a3489736ad982da4f36d8e9142c690f13/66ed6687/GopyMazLfl_mXzYYt9LV4cL785hrJws4kSNCdeDDWz6mfWGJEBW2eSp-cIyw7yXqeYChqJBCbuEy9NfnaPX10A%3D%3D?uid=0&filename=5.%20Изменённый%20ответ%20с%20расчётом%20стоимости%20и%20длительности%20поездки%20из%20Charles..PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

[Окно с настройками автоматического ответа по расчёту стоимости и длительности поездки из Charles](https://downloader.disk.yandex.ru/preview/f7609dc2acd55fe1a8adb52512919bf0319322fd2b0c00b8847fdb4eb5053ea4/66ed669f/P2HaXOBFwmZQIJQni-fgBXhxtuq1AkjCD-avvNFvVyunZlcrIPoz5l-dXKe5f4hOyeK9BovShcYvFCvzjhiuag%3D%3D?uid=0&filename=6.%20Окно%20с%20настройками%20автоматического%20ответа%20по%20расчёту%20стоимости%20и%20длительности%20поездки%20из%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

![Окно с настройками автоматического ответа по расчёту стоимости и длительности поездки из Charles](https://downloader.disk.yandex.ru/preview/f7609dc2acd55fe1a8adb52512919bf0319322fd2b0c00b8847fdb4eb5053ea4/66ed669f/P2HaXOBFwmZQIJQni-fgBXhxtuq1AkjCD-avvNFvVyunZlcrIPoz5l-dXKe5f4hOyeK9BovShcYvFCvzjhiuag%3D%3D?uid=0&filename=6.%20Окно%20с%20настройками%20автоматического%20ответа%20по%20расчёту%20стоимости%20и%20длительности%20поездки%20из%20Charles.PNG&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)

</details>
</details>

<details>
<summary><h2><a name="#mobile-testing" />Тестирование мобильных приложений </h2></summary>

### Таблицы принятия решений. Попарное тестирование. Баг-репорты

Команда Яндекс Метро сделала рефакторинг мобильного приложения на Android — внесла правки в код. Чтобы выпустить новую версию, предварительно нужно: 
    - протестировать те части продукта, которых коснулись изменения;
    - провести регрессионное тестирование и убедиться, что новую версию можно заливать в стор.
Ссылки для работы: 
- текущая версия приложения, которую пользователи скачивают из стора;
- готовящаяся сборка;
- требования к Яндекс Метро.

**1. Таблицы принятия решений**

Спроектировать таблицу принятия решений для требования "Маршрут и выбранные станции сохраняются в истории после того, как пользователь построил маршрут"

**2. Попарное тестирование**

Спроектировать попарное тестирование для блока "Настройки (город, язык, темная тема)

**3. Баг-репорты**

Протестируй мобильное приложение по своим тест-кейсам и чек-листу.
Заведи баг-репорты в YouTrack.

<details>
<summary><h3> Решение </h3></summary>

**1. Таблицы принятия решений**

[Таблица принятия решений для требования "Маршрут и выбранные станции сохраняются в истории после того, как пользователь построил маршрут"](https://docs.google.com/spreadsheets/d/1vEX-7zue1bGkdXjlcVYK-VpRBWi5urDx/edit?usp=sharing&ouid=106744543532953560427&rtpof=true&sd=true)

**2. Попарное тестирование**

[Таблица попарного тестирование для блока "Настройки (город, язык, темная тема)](https://docs.google.com/spreadsheets/d/1u3JefUj1o4VdL98a-xXn7BkdF35PNAyp/edit?usp=sharing&ouid=106744543532953560427&rtpof=true&sd=true)

**3. Баг-репорты**

Из 118 тестов успешно прошло 79, не прошло — 38, пропущено - 1
Список багов, найденных при тестировании, разбит по приоритетам:
Блокирующие: нет

Критичные: 4 шт
[YMSprint6-9](https://gz5658.youtrack.cloud/issue/YMSprint6-9/Prilozhenie-ne-obnovlyaetsya-avtomaticheski-s-versii-2.13-na-3.6)<br>
[YMSprint6-10](https://gz5658.youtrack.cloud/issue/YMSprint6-10/Ne-funkcioniruet-obratnaya-svyaz-v-prilozhenii)<br>
[YMSprint6-11](https://gz5658.youtrack.cloud/issue/YMSprint6-11/Na-sheme-Minska-ne-pravilno-otobrazhaetsya-anglijskij-yazyk)<br>
[YMSprint6-12](https://gz5658.youtrack.cloud/issue/YMSprint6-12/Net-anglijskogo-yazyka-v-ryade-gorodov)<br>

Средний приоритет: 4 шт
[YMSprint6-2](https://gz5658.youtrack.cloud/issue/YMSprint6-2/Vybrannye-stancii-v-istorii-ne-sohranyayutsya-v-nuzhnom-poryadke)<br>
[YMSprint6-4](https://gz5658.youtrack.cloud/issue/YMSprint6-4/Kartochka-stancii-ne-vsplyvaet-pri-zapolnenii-polya-Otkuda)<br>
[YMSprint6-8](https://gz5658.youtrack.cloud/issue/YMSprint6-8/Ne-poyavlyaetsya-uvedomlenie-ob-oshibke-pri-otsutstvii-interneta)<br>
[YMSprint6-13](https://gz5658.youtrack.cloud/issue/YMSprint6-13/Vremennoj-interval-marshruta-ne-obnovlyaetsya-avtomaticheski)<br>

Низкий приоритет: 7 шт
[YMSprint6-1](https://gz5658.youtrack.cloud/issue/YMSprint6-1/Rezhim-Avtomaticheski-v-nastrojkah-temy-ne-menyaetsya-po-vremeni)<br>
[YMSprint6-5](https://gz5658.youtrack.cloud/issue/YMSprint6-5/Kartochka-marshruta-ne-ostaetsya-v-raskrytom-sostoyanii-pri-smene-orientacii)<br>
[YMSprint6-](https://gz5658.youtrack.cloud/issue/YMSprint6-6/Kartochka-marshruta-ne-ostaetsya-v-otkrytom-sostoyanii-na-seredine-prokrutke-pri-smene-orientacii)<br>
[YMSprint6-7](https://gz5658.youtrack.cloud/issue/YMSprint6-7/Pri-long-tape-na-stanciyu-ne-otkryvaetsya-kartochka)<br>
[YMSprint6-14](https://gz5658.youtrack.cloud/issue/YMSprint6-14/Okno-nastroek-ne-ostaetsya-v-srednem-sostoyanii-pri-smene-orientacii)<br>
[YMSprint6-15](https://gz5658.youtrack.cloud/issue/YMSprint6-15/Kartochka-stancii-ne-ostaetsya-v-srednem-sostoyanii-posle-smeny-orientacii)<br>
[YMSprint6-16](https://gz5658.youtrack.cloud/issue/YMSprint6-16/Masshtab-ne-sohranyaetsya-pri-smene-orientacii)<br>

</details>

### Матрица устройств. Эмуляторы. Android Studio

**1. Проектный месяц**

В рамках проектного месяца была выполнена задача от реального заказчика, работа выполнялась совместо с однокурсниками-тестировщиками, а также другими специалистами: менеджерами и разработчиками.
Необходимо составить отчет.


<details>
<summary><h3> Отчет </h3></summary>

Описание проекта:
Какой проект делала твоя команда?:
> Наша замечательная команда тестировала стор для Android приложений AppBazar от МТС на лэндинге<br>
Какая задача перед вами стояла?:
> Протестировать приложение AppBazar на девайсах с ОС Android от 6 до 14. Предоставить заказчику обратную связь по продукту. Первичная \ повторная авторизация, отображение и работа приложений на девайсах разных вендоров, взаимодействие с Лентой и видео контентом, поиск приложений в сторе, жизненный цикл приложения в сторе (скачивание-установка-открытие-удаление).
Сколько человек было в команде? 
> В команде вместе со мной участвовало 10 человек: руководитель тестирования, продукт-менеджер, тимлид и 7 тестировщиков
Как вы распределили задачи между собой? 
> Самое удивительное, задачи между собой мы разделили очень быстро, каждый сам взял  себе определенную ответственную роль и функционал приложения.
Какая задача была в твоей зоне ответственности? 
> В мою зону ответственности входили оформление вкладки Чек-листы и тестирование функциональности раздела Приложение
Сложилось ли взаимодействие с разработчиками и коллегами-тестировщикам? По каким вопросам? 
> Взаимодействие с разработчиками и коллегами-тестировщиками сложилось. Разработчикам были заданы вопросы по серым зонам и по принципам работы приложения и, соответственно, получены ответы от них. Коллеги-тестировщики участвовали в обсуждениях тех или иных вопросов, возникающих во время работы над проектом. Например, у меня возник баг, когда на вновь установленное приложение, у меня не всплывало окно выбора любимых жанров.

Документация

[ТК, ЧЛ и БР разработанные мной и моей командой, с указанием ФИО в столбце Автор](https://docs.google.com/spreadsheets/d/1caUSdL83x1pgd82LG2fR1SErvheXG8go6ob-HTNyXCM/edit?usp=sharing)

[Вопросы и пожелания к заказчику](https://docs.google.com/spreadsheets/d/1UXeHTI1kt7HcOkckXiUrHU3zdiznHVnV-UM6PCCMmRw/edit?usp=sharing)


Ход работы:
> Первым делом я решил “присмотреться” к приложению через Android Studio, Создал устройство по техническим характеристикам приближенного к моему, установил и запустил приложение. Осмотрел максимально каждую вкладку и по своему разделу (Приложения) описал серые зоны, написав их в вопросах к заказчику. Затем начал составлять Чек листы, “погружаясь глубже” в приложение, изучая принцип его работы и возможности. После составления ЧК я начал их тестировать, постепенно закрывая пропущенные пробелы и добавляя новое, удаляя лишнее и повторяющееся, а также, на те ЧЛ, которые я посчитал нужным перевести в ТК, были написаны ТК и новые ТК, на которые ЧЛ не были написаны. Далее приложение (на тот момент 15.1(152498) было установлено на свой физический телефон (его параметры: Мобильное устройство Xiaomi Redmi Note 11 Pro, ОС Android 13, разрешение экрана 1080х2400, диагональ 6.53”) и оно сразу же запросило обновление, в результате чего приложение обновилось до версии 16.1(162628) и были созданы дополнительные и подправлены имеющиеся ЧЛ и ТК. После окончательно составления всех ЧЛ и ТК, были проведены их проверки, а также кросс-ревью проверка Ольги Гоголевой. По результатам проверок были созданы БР, а также добавлены новые ЧЛ и ТК, и поправленные/доработанные/удалены имеющиеся
> Параллельно всему, велось общение с командой данного проекта и задавались и получались ответы от разработчика (через проджект-менеджера) и добавление тех или иных ЧЛ и/или ТК
>По результатам тестирования были созданы БР, которые были воспроизведены на устройстве.
>Было проведено кросс-ревью Ольги Гоголевой - в результате которых были написаны комментарии Ольге по темам мне не понятным, либо по вопросам и доработкам . Все ее ТК и ЧЛ прошли проверку и отмечены статус в отчете.


Выводы
Баги:
Сколько всего багов нашла твоя команда? А ты? 
> Наша команда нашла 30 багов, лично мной из них - 13
Какой баг показался самым критичным, если такой есть? 
> Самым критичным оказался Баг под номером BTcAPL-29
Баги исправлялись быстро? 
> Во время проектного месяца Баги не исправлялись, по крайней мере обратной связи по БР от заказчика не поступали.
Если нет, почему? Как можно ускорить процесс исправления багов? 
> По информации из брифа, заказчику необходимо было получить обратную связь по репортам и фидбекам в любом виде, которые они сами в дальнейшем отсортируют
Как ты думаешь, это хороший результат? Почему? 
>Количество багов говорит о том, насколько качественно сделан тот или иной продукт, говорить о том, хороший ли результат в 30 Багов - сложно, с одной стороны это не много, тогда как с другой - есть над чем поработать.

Серые зоны:
Были ли в требованиях серые зоны? 
> В требованиях была одна большая, даже громадная Серая зона - а именно, отсутствие требований =)
Если да, то какую самую «хитрую» серую зону нашла твоя команда? 
> Лично мне понравился вопрос моего коллеги Ярослава: “Как работает логика сортировки по новизне? И работает ли вообще?” - Ответ на который: “Там всё плохо и сортируется неправильно, забудьте 😢” Ну, а в целом, на мой взгляд, это серая зона по работе чек-боксов Приложений и Игр, для чего разработчикам, так же на мой взгляд-, пришлось писать “на коленках” соответствие приложениям/играм их возрастных категорий
Проектирование тестов:
Тебе удалось разработать тесты? 
> Да, мне удалось разработать 45 тест кейсов
Если да, как ты оцениваешь их качество? 
> В целом качество ТК неплохое, есть конечно над чем поработать, но все приходит с опытом. И все же, осталось какое то чувство, что что-то упущено
Как их можно улучшить? 
> Сократить количество шагов, максимально указав Предусловия. Более четче и понятнее описывать шаги.
Остальные участники команды разрабатывали тесты? 
> Да. остальными участниками команды было разработано дополнительно 49 тест кейсов
А остальные в команде успели разработать тесты? Как ты оцениваешь результат? Можно ли его улучшить? 
> Считаю, что количество тест кейсов недостаточно, можно улучшить данный результат, подробнее расписав те или иные действия, не ограничиваясь ЧЛ, но, как говорится - тестировщику виднее =)

Продукт:
Опиши качество продукта, который тестировала твоя команда? 
> По результатам тестирования продукта от МТС AppBazar, и в результате найденного количества Багов и во многом их незначительности, считаю, что качество данного продукта на высоком уровне, но есть над чем поработать. Все пожелания были написаны и отправлены разработчику
Такой продукт можно выпускать в релиз? Как можно улучшить продукт перед релизом?  
> Вопрос не актуален, так как приложение уже в проде, но по результатам найденных багов, необходимо исправить наиболее критические - и “приложению месту быть”Все дополнительные предложения по улучшениям были направлены разработчику.

</details>

</details>


<details>
<summary><h2><a name="api-testing" />Тестирование API </h2></summary>

### Тестирование API

**1. RES API. JSON. Postman**
Необходимо протестировать часть функциональности API приложения Яндекс Прилавок 
Требования к приложению находятся тут.
1. Составь чек-лист для проверки четырёх эндпоинтов, которые указаны ниже. 
2. Проведи тестирование API через Postman по составленному чек-листу и заведи баг-репорты в YouTrack.
3. Составь отчет

Эндпоинты:
- Работа с курьерами: возможность проверить, есть ли доставка курьерской службой «Привезём быстро» и сколько она стоит — ручка POST /fast-delivery/v3.1.1/calculate-delivery.xml.
- Работа с корзиной: возможность получить список продуктов, которые добавили в корзину — ручка GET /api/v1/orders/:id. 
- Возможность добавлять продукты в корзину — ручка PUT /api/v1/orders/:id. 
- Возможность удалять корзину — ручка DELETE /api/v1/orders/:id.

<details>
<summary><h3> Отчет </h3></summary>

Отчёт о тестировании Яндекс Прилавка
Тестирование API Яндекс Прилавка проводилось с использованием инструмента Postman.<br>
Для тестирования API составлен [чек-лист](https://docs.google.com/spreadsheets/d/1KzRPds99JmNAbX32mBKWREYY8Y_riNlEUFutHennZ-Y/edit?usp=sharing)<br>
[Результаты выполнения тестов](https://docs.google.com/spreadsheets/d/1KzRPds99JmNAbX32mBKWREYY8Y_riNlEUFutHennZ-Y/edit?usp=sharing)<br>
[Коллекция Postman](https://disk.yandex.ru/d/3VYXJpjrnW9GSQ)

Из 101 проверок успешно прошло 66, не прошло — 44, пропущено — 1.<br>
Список багов, найденных при тестировании, разбит по приоритетам:<br>
Критичные:<br>
[YP-1](https://gz5658.youtrack.cloud/issue/YMSprint6-24/8-14-Status-200-pri-otpravke-zaprosa-na-dostavku-vne-rabochego-vremeni)<br>
[YP-2](https://gz5658.youtrack.cloud/issue/YMSprint6-25/16-18-Dostavka-privezem-bystro-dostupna-pri-ukazanii-bukvy-zaprose-v-deliveryTime)<br>
[YP-3](https://gz5658.youtrack.cloud/issue/YMSprint6-26/19-Dostavka-privezem-bystro-dostupna-pri-ukazanii-specsimvola-v-zaprose-v-deliveryTime)<br>
[YP-4](https://gz5658.youtrack.cloud/issue/YMSprint6-27/20-Oshibka-v-otvete-pri-ukazanii-otricatelnogo-chisla-v-zaprose-v-deliveryTime)<br>
[YP-5](https://gz5658.youtrack.cloud/issue/YMSprint6-28/22-23-Dostavka-privzem-bystro-dostupna-pri-ukazanii-ne-celogo-chisla-v-deliveryTime)<br>
[YP-6](https://gz5658.youtrack.cloud/issue/YMSprint6-29/24-Dotsavka-privezem-bystro-dostupna-pri-pustom-znachenii-deliveryTime)<br>
[YP-7](https://gz5658.youtrack.cloud/issue/YMSprint6-30/25-Dostavka-Privezem-bystro-dostupna-esli-productsCount-ravno-0)<br>
[YP-8](https://gz5658.youtrack.cloud/issue/YMSprint6-31/38-Dostavka-Privezem-bystro-dostupna-esli-productsCount-pustoe-znachenie)<br>
[YP-9](https://gz5658.youtrack.cloud/issue/YMSprint6-32/39-41-Dostavka-Privezem-bystro-dostupna-esli-v-productsCount-bukvennoe-znachenie)<br>
[YP-10](https://gz5658.youtrack.cloud/issue/YMSprint6-33/42-43-Dostavka-Privezem-bystro-dostupna-esli-v-productsCount-ne-celoe-chislo)<br>
[YP-11](https://gz5658.youtrack.cloud/issue/YMSprint6-34/44-Dostavka-Privezem-bystro-dostupna-esli-v-productsCount-specsimvol)<br>
[YP-12](https://gz5658.youtrack.cloud/issue/YMSprint6-36/46-Oshibka-v-strukture-otveta-esli-productWeight-ravno-0)<br>
[YP-13](https://gz5658.youtrack.cloud/issue/YMSprint6-35/45-Oshibka-v-strukture-otveta-esli-v-productsCount-otricatelnoe-chislo)<br>
[YP-14](https://gz5658.youtrack.cloud/issue/YMSprint6-37/59-61-Oshibka-v-strukture-otveta-esli-v-productsWeight-ukazana-bukva)<br>
[YP-15](https://gz5658.youtrack.cloud/issue/YMSprint6-38/63-Oshibka-v-strukture-otveta-esli-v-productsWeight-otricatelnoe-chislo)<br>
[YP-16](https://gz5658.youtrack.cloud/issue/YMSprint6-39/64-Oshibka-v-strukture-otveta-esli-v-productsWeight-pustoe-znachenie)<br>
[YP-17](https://gz5658.youtrack.cloud/issue/YMSprint6-40/25-7-Oshibka-v-otvete-pri-Poluchenie-spiska-produktov-v-korzine-ukazannoj-bukvami)<br>
[YP-18](https://gz5658.youtrack.cloud/issue/YMSprint6-41/28-Oshibka-v-otvete-pri-Poluchenie-spiska-produktov-v-korzine-ukazannoj-specsimvolom)<br>
[YP-19](https://gz5658.youtrack.cloud/issue/YMSprint6-41/28-Oshibka-v-otvete-pri-Poluchenie-spiska-produktov-v-korzine-ukazannoj-specsimvolom)<br>
[YP-20](https://gz5658.youtrack.cloud/issue/YMSprint6-42/29Oshibka-v-otvete-pri-Poluchenie-spiska-produktov-v-korzine-ukazannoj-c-tochkoj)<br>
[YP-21](https://gz5658.youtrack.cloud/issue/YMSprint6-43/210Oshibka-v-otvete-pri-Poluchenie-spiska-produktov-v-korzine-ukazannoj-c-zapyatoj)<br>
[YP-22](https://gz5658.youtrack.cloud/issue/YMSprint6-45/39Oshibka-v-otvete-pri-doavlenii-spiska-produktov-v-korzinu-so-specsimvolom)<br>
[YP-23](https://gz5658.youtrack.cloud/issue/YMSprint6-44/35-Oshibka-v-otvete-pri-doavlenii-spiska-produktov-v-korzinu-kazannoj-bukvami)<br>
[YP-24](https://gz5658.youtrack.cloud/issue/YMSprint6-46/311Oshibka-v-otvete-pri-doavlenii-spiska-produktov-v-korzinu-ukazannoj-s-tochkoj)<br>
[YP-25](https://gz5658.youtrack.cloud/issue/YMSprint6-47/317-Produkt-dobavlyaetsya-v-korzinu-s-kolichestvom-0)<br>
[YP-26](https://gz5658.youtrack.cloud/issue/YMSprint6-48/318-Produkt-dobavlyaetsya-v-korzinu-s-pustym-kolichestvom)<br>
[YP-27](https://gz5658.youtrack.cloud/issue/YMSprint6-22/42-Udalenie-korziny)<br>
Также в рамках работы была составлена схема приложения:

Локализация бага [YP-20](https://gz5658.youtrack.cloud/issue/YMSprint6-17) показала, что баг находится на стороне фронтенда. Должна быть валидация поля Имя набора на длину не менее 2 и не более 15 символов,только русские и английские буквы, пробел, тире  (согласно требованиям), но при этом валидация проходит на одном символе и цифре.<br> 
БР: [YP-21](https://gz5658.youtrack.cloud/issue/YMSprint6-53/V-pole-Imya-nabora-mozhno-vvesti-bolee-15-simvolov) - можно ввести более 15 символов в Имя набора [YP-22](https://gz5658.youtrack.cloud/issue/YMSprint6-54/V-pole-Imya-nabora-mozhno-vvesti-menee-2-simvolov) - можно ввести менее 2 символов в Имя набора<br> 
При воспроизведении бага не выдается Окно об ошибке. Во время воспроизведения ошибки использовался Devtools, который показал в запросе products текст  500 Internal Server Error, тогда как ожидалась ошибка 400 "Не все необходимые параметры были переданы" . БР YMSprint6-57- Неверное отображение ошибки при создании набора без выбора продуктов<br>
Так же обнаружены Баги<br> 
[YP-23](https://gz5658.youtrack.cloud/issue/YMSprint6-49/V-pole-Nazvanie-pri-sozdanii-nabora-mozhno-vvesti-specsimvol) -  в поле Имя набора можно ввести спецсимвол<br>
[YP-24](https://gz5658.youtrack.cloud/issue/YMSprint6-50/Mozhno-sozdat-nabor-bez-produktov) - создание набора без продуктов<br>
[YP-25](https://gz5658.youtrack.cloud/issue/YMSprint6-55/V-pole-Imya-nabora-mozhno-vvesti-cifry) - можно ввести цифры в Имя набора <br>
[YP-26](https://gz5658.youtrack.cloud/issue/YMSprint6-56/V-pole-produkty-mozhno-dobavit-bolee-30-produktov) - можно добавить более 30 продуктов при создании<br>

Баги на Бэкэнде [YP-27](https://gz5658.youtrack.cloud/issue/YMSprint6-51/100.-Sozdanie-nabora-bez-peredachi-obyazatelnogo-parametra-productsList) - Создание набора без передачи обязательного параметра productsList 
[YP-28](https://gz5658.youtrack.cloud/issue/YMSprint6-52/101.-Sozdanie-nabora-s-pustym-znacheniem-productsList) - Создание набора с пустым значением productsList<br>

Для анализа информационных логов необходимо выполнить следующие команды:
```
$ ssh-keygen
$ cat ~/.ssh/id_rsa.pub
$ ssh d7c6b116-c409-4ac4-ba5c-340e7342e6c6@serverhub.praktikum-services.ru -p 4554 
$ mkdir home/morty/generallogs
$ cp ../var/www/backend/packages/main/logs/combined.log logs1.log
$ cp ../var/www/backend/packages/secondary/build/logslogs/combined.log logs2.log
$ grep -i INFO home/morty/generallogs/logs1.log > info.log
$ grep -i INFO home/morty/generallogs/logs2.log >> info.log
```

Найденные критические дефекты расположены в основных пользовательских сценариях, команда тестирования против публикации текущей версии API<br> 
Так же обнаружен баг, перекрывающий контент при регистрации 
[YP-29](https://gz5658.youtrack.cloud/issue/YMSprint6-23/Perekrytie-teksta-Okna-registracii-polzovatelya-Yandeks-Prilavok)


</details>

</details>

<!--<details>
<summary><h2><a name="data-bases" />Тестирование баз данных </h2></summary>

### Тестирование баз данных




<details>
<summary><h3> Отчет </h3></summary>






</details>

</details>
-->

<details>
<summary><h2><a name="test-automation" />Основы автоматизации тестирования </h2></summary>

### Тестирование баз данных

Разработать тесты на проверку параметра name при создании наборов с продуктами в Яндекс.Прилавок с помощью API Яндекс.Прилавок.

<details>
<summary><h3> Отчет </h3></summary>

[Файлы с кодом представлены тут](https://github.com/GZ5658/QA-Portfolio/tree/developer/Основы%20автоматизации%20тестирования)


</details>

</details>