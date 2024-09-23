# <a name="up" />Портфолио QA-Yandex

В портфолио собраны проекты, выполненные во время обучения по специальности [Инженер по тестированию Плюс](https://practicum.yandex.ru/qa-engineer-plus/) в Яндекс.Практикуме.

[Проектирование тестов](#test-design)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тест-анализ | Mind map | Серые зоны<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тест-дизайн | Классы эквивалентности | Граничные значения<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Тестовая документация | Чек-листы | Тест-кейсы

<!--[Тестирование веб-приложений](#web-testing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DevTools | Charles<br>

[Тестирование мобильных приложений](#mobile-testing)<br>
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

[Блок схема](https://downloader.disk.yandex.ru/preview/0afcad20895ebb198a4bf40983f08419f936396f1ea65697e8ef10ebe1d824cc/66ec1e63/mEsF7H3r567gsM9DJd1PprUBqGcfIDpt-OIGfhAXtbcYniWYYcRO_W2sbPyC85YhIQTSdWJN-y9DFtC35FFoBQ%3D%3D?uid=0&filename=Блок%20схема.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048)

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


