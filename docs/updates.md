# Размышления после добавления импорта JUnit файлов

Результаты сюит, кейсов и степов не содержат практически никакой инфы кроме статуса, их имя
и описание всё лежит в родителях.
При изменении родителей мы также изменим и информацию о прогоне (Run).
Это не критично если суть теста не изменилась, но если это не так, то прогон перестанет 
отражать реальную картину "как было" и будет отражать результаты как будто они были выполнены
уже на обновленных тестах.

При выводе информации о прогоне скорее всего получим очень тяжелый запрос в SQL т.к. нужно будет
выдернуть не только результаты, но и их родителей, чтобы получить имена и описание.
Может быть о производительности еще рановато думать, но не хотелось бы выстрелить себе в ногу каким
нибудь одним особо неудачным решением

Чтобы адресовать вышеизложенные проблемы придётся сделать что-то из следующего:

- Часть инфы о тесткейсе, сюите копировать в их результат, чтобы не пришлось его отдельно запрашивать.
- При изменении кейсов/сюитов иметь выбор обновить их "in-place" или создать копию. Оригинальный
  кейс/сюита пропадают из отображения в проекте, но остаются в базе. Все существующие прогоны
  ссылаются на них, а новые уже на новые

В случае кейсе получим очень много дублирования в БД, а также каскадных обновлений. Но ускорим запросы.
Второй всем кажется лучше, если запросы для Run'ов будут не очень медленные.