# Валидатор IP-адресов

Простая Python-утилита для проверки и классификации IP-адресов на IPv4, IPv6 или невалидные.

## Возможности

- Проверяет адреса форматов IPv4 и IPv6
- Возвращает четкую классификацию ("IPv4", "IPv6" или "Invalid")
- Использует встроенный модуль Python `ipaddress` для надежной проверки
- Легковесная, не требует дополнительных зависимостей

## Как использовать

```python
from ip_validator import validIPAddress

result = validIPAddress("192.168.1.1")
print(result)  # Вывод: "IPv4"

result = validIPAddress("2001:db8::1")
print(result)  # Вывод: "IPv6"

result = validIPAddress("invalid.address")
print(result)  # Вывод: "Invalid"
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш_username/ip-validator.git
cd ip-validator
```

2. Скрипт требует Python 3.6+. Дополнительные пакеты не нужны.

## Примеры использования

### Валидный IPv4:
```python
print(validIPAddress("192.168.1.1"))  # "IPv4"
```

### Валидный IPv6:
```python
print(validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # "IPv6"
```

### Невалидный адрес:
```python
print(validIPAddress("256.300.1.1"))  # "Invalid"
print(validIPAddress("not.an.ip"))    # "Invalid"
```

## Как это работает

Функция `validIPAddress` использует встроенный модуль Python `ipaddress`:
1. Пытается создать объект IP-адреса из переданной строки
2. Если успешно - определяет тип адреса (IPv4 или IPv6)
3. При ошибке преобразования возвращает "Invalid"

## Тестирование

В коде уже есть примеры тестов. Для дополнительного тестирования можно добавить адреса в блок `__main__`.

## Лицензия

[MIT](LICENSE)
