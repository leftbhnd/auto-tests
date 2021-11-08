# Настройка окружения на ubuntu 18.04

```
sudo apt-get install -y python-pytest
sudo apt-get install -y scrot
pip install pyautogui
pip install xmltodict
pip install psycopg2
```

# Структура проекта:

`main.py` - класс объединяющий ros классы

`src/conftest.py` - вспомогательные функции, переиспользуемые в тестах

`src/helpers/buttons/*` - координаты кнопок у соответствующего экрана

`src/helpers/modals/*` - координаты кнопок у соответствующего модального окна

`src/helpers/params/*` - enum классы параметров робота

`src/helpers/config.py` - конфигурационный файл проекта (задается разрешение экрана, координаты и так далее)

`src/helpers/keyboard.py` - объект с координатами экранной клавиатуры

`src/helpers/messages.py` - классы для создания сообщений

`src/helpers/mouse_position.py` - скрипт для получения текущей координаты

`src/helpers/robot_*.py` - классы объединяющие общие сущности (кнопки, модалки, параметры)

`src/helpers/screen_maker.py` - скрипт для создания скриншота

`src/services/*` - классы управления ros

`src/tests/*` - unit и e2e тесты

`src/test_data/*` - тестовые данные

`*_run.sh` - bash скрипты запуска тестов

# Codestyle

- Название тестов должно содержать: `test_*.py`
- Внутри тестов функции должны содержать слово `test`
- Использовать уникальный `@pytest.mark.X` внутри одного модуля

# API класса main.py

## Publishers:

- `node.autoModePub()`
- `node.joyModePub()`
- `node.toPointPub(int)`
- `node.enableDrivePausePub()`
- `node.disableDrivePausePub()`
- `node.chargeAppPub()`
- `node.driveStationPub()`

#

- `node.facePub(type, track_id, id, source, score)`
- `node.clearFacePub()`

#

- `node.interactionPub(state, reason)`

#

- `node.joyPhraseModePub()`
- `node.joyCommandPub(joy_msg)`

#

- `node.cancelScriptPub()`

#

- `node.asrPub(str)`
- `node.ttsPub(str)`
- `node.cancelSpeechPub()`

#

## Services:

- `node.setLevelSrv([int])` -> [0, 1, 2, 3,...]
- `resetLevelSrv()` -> устанавливает уровень ответов в дефолт
- `getLevelsOrder()` -> ['0', '1', '2',...] = [str, str, str,...]

#

## Getters:

- `node.getDriveMode()` -> X = int
- `node.getCurrentPoint()` -> X = int
- `node.getWheelsData()` -> [rwheel, lwheel] = [int, int]
- `node.getDrivePause()` -> True|False = bool
- `node.getDriveStationStatus()` -> True|False = bool
- `node.getDriveStatus()` -> X = int
- `node.getChargeState()` -> True|False = bool
- `node.getUseRadius()` -> True|False = bool

#

- `node.getInteraction()` -> [State, Reason] = [bool, int]

#

- `node.getJoyCmd()` -> [[0.0, 0.0, 0.0, 0.0, RT, LT], [A, B, 0, X, Y, 0, LB, RB, 0, 0, 0, start, 0, 0, 0, back, 0, up, right, down, left]]
- `node.getJoySpeech()` -> True|False = bool

#

- `node.getScriptProcess()` -> [Process, Name] = [bool, str]

#

- `node.getServosState()` -> [servos]

#

- `node.getAnswer()` -> 'текст ответа' = str
- `node.getTts()` -> 'текст произношения' = str
- `node.getLevelsOrder()` -> ['0', '1', '2', '3', '4', '5', '6', '7']
- `node.getSystemLanguage()` -> 'выбранный язык системы' = str

#

# Фикстуры (вспомогательные функции)

- `screenDiffChecker('dir/original_image', coordinates=screen_resolution)` - создает скриншот текущего экрана, сравнивает с оригиналом. Если нет оригинального скриншота - делает его
- `dNd((start[0], start[1]), (finish[0], finish[1]))` - функция Drag And Drop
- `click(btn.X.X|modal.X.X|param.X.X)` - функция клика на указанную координату (кнопку, модальное окно, параметр)
- `openPwdModal()` - функция, открывающая модальное окно ввода пароля
- `openServiceMenu()` - функция, открывающая сервисное меню из запущенной gui
- `typeText('привет'|123456)` - функция печати, если тип аргумента str - печатает текст, если тип аргумента int - сначала выбирается ввод цифр, затем печать цифр
- `node.getX()` - методы получения данных с топика
- `node.XPub(data|empty)` - методы для публикации данных в топик
- `joy.upVolume()|downVolume()|upMic()|downMic()|phraseMode()|nextPhrase()|previousPhrase()|autoMode()` - методы имитации управления джойстиком
- `db.updateValue([{'name': param.X.X, value: any}])` - метод обновления параметров робота, аргумент: массив объекта(ов) с ключами 'name' и 'value'
- `db.getValue(param.X.X)` - метод получения значения у указанного параметра, например, param.driving.radius = '/driving/useRaius'

#

# Пример теста

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import time

from src.helpers.config import btn, modal, running, restart #импорт кнопок, модалок, таймаутов


@pytest.mark.interface # маркер для запуска
def test_dialog_line(click, screenDiffChecker, node): # название тестовой функции с аргументами-фикстурами
    click(btn.start.play) # клик на кнопку Play на стартовом экране
    click(modal.radius.yes) # клик на кнопку ДА у модального окна радиуса
    time.sleep(running) # таймаут для запуска
    node.cancelSpeechPub() # прерывание текущей реплики робота
    node.asrPub('тестовое правило') # публикация сообщения роботу для распознавания речи
    assert screenDiffChecker(
        'interfaces/dialog_line.png'
    ) is None # сравнение скриншота текущего экрана с оригиналом


@pytest.mark.interface
def test_restore(click, openServiceMenu):
    openServiceMenu() # фикстура открытия сервисного меню
    click(btn.control.restart) # клик на кнопку перезапуска на экране "Управление"
    click(modal.restart.yes) # клик на кнопку ДА у модального окна перезапуска
    time.sleep(restart) # таймаут перезапуска
```

# Запуск тестов

### Подготовка

```
export DISPLAY=:0
```

### Запуск всех тестов:

```
pytest -v
```

### Запуск конкретного теста:

```
pytest test_name.py -v
```

### Запуск тестов по маркеру:

```
Для запуска всех тестов с маркировкой driving необходимо выполнить команду:
pytest -m driving -v
```

### Использование нескольких входных параметров:

```
@pytest.mark.parametrize("question, answer", [
    ('привет', 'добрый день'),
    ('как дела', 'хорошо'),
    (True, True),
    (1, 1)
])
def test_differ(question, answer):
   assert question == answer
```

### Остановка тестов после N сбоев:

```
pytest test_example.py -v --maxfail=3

Тест завершится после трех неудачных попыток
```

# Формирование отчета

```
pytest test_example.py -v --junitxml="result.xml"
```
