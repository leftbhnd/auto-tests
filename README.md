# Настройка окружения

```
sudo apt-get install -y python-pytest
pip install pyautogui
sudo apt-get install scrot
```

# Структура проекта:

`main.py` - класс управления топиками робота

`src/conftest.py` - функции, которые можно использовать без импорта в тестах

`src/helpers/*` - вспомогательные скрипты/конфиги

`src/tests/*` - unit и e2e тесты

# Test's codestyle

- Название тестов должно содержать: `*_test.py` или `*test_*.py`
- Внутри тестов функции должны содержать слово `test`
- Использовать уникальный `@pytest.mark.X` внутри одного файла

# API класса main.py

<deatails>
<summary>Подробнее</summary>

### Publishers:

- `node.facePub(msg)`
- `node.interactionPub(msg)`
- `node.asrPub(msg)`
- `node.cancelSpeechPub(msg)`
- `node.ttsPub(msg)`
- `node.autoModePub(msg)`
- `node.joyModePub(msg)`
- `node.toPointPub()`
- `node.enableDrivePausePub(msg)`
- `node.disableDrivePausePub(msg)`
- `node.chargeAppPub(msg)`
- `node.driveStationPub(msg)`
- `node.joyPhraseModePub(msg)`
- `node.joyCommandPub(msg)`

### Getters:

- `node.getInteraction()`
- `node.getScriptProcess()`
- `node.getScriptProcess()`
- `node.getServosState()`
- `node.getAnswer()`
- `node.getTts()`
- `node.getLevelsOrder()`
- `node.getDriveMode()`
- `node.getCurrentPoint()`
- `node.getWheelsData()`
- `node.getDrivePause()`
- `node.getDriveStationStatus()`
- `node.getDriveStatus()`
- `node.getChargeState()`
- `node.getUseRadius()`
- `node.getJoyCmd()`
</details>

# Фикстуры

<deatails>
<summary>Подробнее</summary>

- `mouseClick(msg.x, msg.y)`
- `screenDiffChecker('original_image', coordinates=(0, 40, 1280, 800))`
- `pressAndMove([(x1, y1), (x2, y2)])`
- `clickOn('button')`
- `openPasswordModal()`
- `typeText(['привет'])`
- `node`
- `joy`

</details>

# Запуск тестов

<deatails>
<summary>Подробнее</summary>

### Запуск всех тестов:

```
pytest -v
```

### Запуск конкретного теста:

```
pytest test_name.py -v
```

### Запуск нескольких тестов с однотипным словом в названии:

```
pytest -k word_in_test -v
```

### Вызов тестовых функций отдельных тестов:

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
pytest test_example.py -v --maxfail = 3

Тест завершится после трех неудачных попыток
```

</details>

# Формирование отчета

```
pytest test_example.py -v --junitxml="result.xml"
```
