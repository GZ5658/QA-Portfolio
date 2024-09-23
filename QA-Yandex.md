# <a name="up" />Портфолио QA-Yandex

В портфолио собраны проекты, выполненные во время обучения по специальности [Инженер по тестированию Плюс](https://practicum.yandex.ru/qa-engineer-plus/) в Яндекс.Практикуме.

[Проектирование тестов](#test-design)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тест-анализ | Mind map | Серые зоны<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тест-дизайн | Классы эквивалентности | Граничные значения<br>
<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тестовая документация | Чек-листы | Тест-кейсы-->

[Тестирование веб-приложений](#web-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DevTools | Charles<br>

<!--[Тестирование мобильных приложений](#mobile-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Таблицы принятия решений | попарное тестирование | Баг-репорты<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Матрица устройств | Эмуляторы | Android Studio

[Тестирование API](#api-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;REST API | JSON | Postman

[Тестирование баз данных](#data-bases)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Консоль | SQL | PostgreSQL

[Основы автоматизации тестирования](#test-automation)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python| NodeJS | Puppeteer-->

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



