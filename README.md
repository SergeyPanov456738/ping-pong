# Игра пинг - понг

Это симулятор игры пинг - понг разработаный на языке програмирования [python](https://www.python.org/) и с использованием библиотеки [pygame](https://www.pygame.org/). Цель игры отбивать мяч ракетками и не дать ему уйти за границы окна.

Игра разработана для двух игроков, управление ракетками осуществляется кнопками <kbd>W</kbd> и <kbd>S</kbd> и стрелкой верх\вниз.

### Скриншоты из игры
Начало игры:

<img src='https://raw.githubusercontent.com/SergeyPanov456738/ping-pong/refs/heads/master/images/start_game.png' width='400'>

Конец игры:

<img src='https://raw.githubusercontent.com/SergeyPanov456738/ping-pong/refs/heads/master/images/player_win.png' width='400'>

### Пример кода
```python
class Ball(GameSprite):
    def move(self):
        self.rect.x += dir_x
        self.rect.y += dir_y
```