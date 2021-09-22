# Настройка окружения

```
sudo apt-get install -y python-pytest
sudo apt-get install -y scrot
pip install pyautogui
pip install xmltodict
```

# Структура проекта:

`main.py` - класс с методами управления топиками робота

`src/conftest.py` - фикстуры

`src/helpers/*` - скрипты, конфиги, классы с сообщениями/координатами кнопок

`src/tests/*` - unit и e2e тесты

`src/test_data/*` - тестовые данные

# Test's codestyle

- Название тестов должно содержать: `test_*.py`
- Внутри тестов функции должны содержать слово `test`
- Использовать уникальный `@pytest.mark.X` внутри одного модуля

# API класса main.py

### Publishers:

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

### Getters:

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

# Фикстуры

- `screenDiffChecker('directory/original_image', coordinates=screen_resolution)`
- `dNd((start[0], start[1]), (finish[0], finish[1]))`
- `click(btn.X|modal.X|params.X)`
- `openPwdModal()`
- `openServiceMenu()`
- `type('привет')`
- `node.getX()`
- `node.XPub(data|empty)`
- `joy.upVolume()|downVolume()|upMic()|downMic()|phraseMode()|nextPhrase()|previousPhrase()|autoMode()`

# Запуск тестов

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
