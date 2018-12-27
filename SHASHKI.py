from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

letters = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}


class Window(QWidget):
    def __init__(self):
        super().__init__()

        def creating_board(self):
            self.ch_board = [[None for _ in range(9)] for _ in range(9)]
            self._size_cell = 60
            for i in range(8):
                self.ch_board[i + 1][0] = str(i + 1)
                self.ch_board[0][i + 1] = str(letters[i + 1])

        def ranking_checkers(self):
            for i in range(1, 4):
                for j in range(1, 9):
                    self.ch_board[i][j] = '⚪'
            for i in range(5, 9):
                for j in range(1, 9):
                    self.ch_board[i][j] = '⚫'

        self._played_white = False
        self.i = 0
        self.j = 0
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.old_i = 0
        self.old_j = 0
        self.flag_white = False
        self.flag_black = False
        self.flag_old_coords = False
        creating_board(self)
        ranking_checkers(self)

        self.good_click_coords = False

    def mouseReleaseEvent(self, e):

        def click_determ(self):
            self.good_click_coords = False
            if not self.good_click_coords:
                self.i = e.pos().y() // self._size_cell
                self.j = e.pos().x() // self._size_cell
                if ((self.i % 2 != 0 and self.j % 2 != 0) or (self.i % 2 == 0 and self.j % 2 == 0)) and (
                        self.i > 0 and self.i < 9 and self.j > 0 and self.j < 9):
                    self.good_click_coords == True

        click_determ(self)

        if self.i == 0 or self.i >= 9 or self.j == 0 or self.j >= 9 or (self.i % 2 == 0 and self.j % 2 != 0) or (
                self.i % 2 != 0 and self.j % 2 == 0):
            return

        def remove_white(self):
            if self.ch_board[self.i][self.j] == '⚪' and not self._played_white:
                if may_go(self):
                    self._played_white = True
                    self.ch_board[self.i][self.j] = ''
                    self.ch_board[self.i][self.j] = None
                    self.old_i = self.i
                    self.old_j = self.j
                    self.flag_old_coords = True
            else:
                pass

        def create_white(self):
            if self._played_white:
                click_determ(self)
                if self.ch_board[self.i][self.j] is None:
                    if (
                            self.j - 1 == self.old_j or self.j + 1 == self.old_j) and self.i - 1 == self.old_i and self.flag_white is False:
                        self.ch_board[self.i][self.j] = '⚪'
                        self.flag_white = True
                    else:
                        self.i = self.old_i
                        self.j = self.old_j
                        self.flag_black = False
            else:
                pass

        def remove_black(self):
            click_determ(self)
            if self.ch_board[self.i][self.j] == '⚫' and self._played_white:
                if may_go(self):
                    self._played_white = False
                    self.ch_board[self.i][self.j] = ''
                    self.ch_board[self.i][self.j] = None
                    self.old_i = self.i
                    self.old_j = self.j
            else:
                pass

        def create_black(self):
            if not self._played_white and not may_eat(self):
                click_determ(self)
                if self.ch_board[self.i][self.j] is None:
                    if (
                            self.j - 1 == self.old_j or self.j + 1 == self.old_j) and self.i + 1 == self.old_i and self.flag_black is False:
                        self.ch_board[self.i][self.j] = '⚫'
                        self.flag_black = True
                    else:
                        self.i = self.old_i
                        self.j = self.old_j
                        self.flag_white = False
            else:
                pass

        def may_go(self):
            if self.ch_board[self.i][self.j] == '⚪':
                if (self.ch_board[self.i + 1][self.j + 1] is None or self.ch_board[self.i + 1][
                    self.j - 1] is None) or may_eat(self):
                    return True
                else:
                    return False

            elif self.ch_board[self.i][self.j] == '⚫':
                if (self.ch_board[self.i - 1][self.j - 1] is None or self.ch_board[self.i - 1][
                    self.j + 1] is None) or may_eat(self):
                    return True
                else:
                    return False

        def may_eat(self):
            if self.ch_board[self.i][self.j] == '⚪':
                if self.ch_board[self.i + 1][self.j + 1] == '⚫' and self.ch_board[self.i + 2][self.j + 2] is None:
                    return True
                elif self.ch_board[self.i + 1][self.j - 1] == '⚫' and self.ch_board[self.i + 2][self.j - 2] is None:
                    return True
                else:
                    return False

            if self.ch_board[self.i][self.j] == '⚫':
                if self.ch_board[self.i - 1][self.j - 1] == '⚪' and self.ch_board[self.i - 2][self.j - 2] is None:
                    return True
                elif self.ch_board[self.i - 1][self.j + 1] == '⚪' and self.ch_board[self.i - 2][self.j + 2] is None:
                    return True
                else:
                    return False

        def may_eat_when_up(self):
            if self.ch_board[self.i + 1][self.j + 1] == '⚫' and self.ch_board[self.i + 2][self.j + 2] is None:
                return True
            elif self.ch_board[self.i + 1][self.j - 1] == '⚫' and self.ch_board[self.i + 2][self.j - 2] is None:
                return True

            if self.ch_board[self.i - 1][self.j - 1] == '⚪' and self.ch_board[self.i - 2][self.j - 2] is None:
                return True
            elif self.ch_board[self.i - 1][self.j + 1] == '⚪' and self.ch_board[self.i - 2][self.j + 2] is None:
                return True
            else:
                # print('Nonononoooooo')
                return False

        def eat(self):
            click_determ(self)
            print(self.ch_board[self.i + 1][self.j + 1])
            if self.ch_board[self.i + 1][self.j + 1] == '⚫' and self.ch_board[self.i][self.j] is None:
                click_determ(self)
                print('ok')
                print(self.i, self.j)
                self.ch_board[self.i - 1][self.j - 1] = ''
                self.ch_board[self.i - 1][self.j - 1] = None

                self.ch_board[self.i][self.j] = '⚫'
                self.flag_white = True
            elif (self.ch_board[self.i + 1][self.j - 1] == '⚪' and self.ch_board[self.i + 2][self.j - 2] is None):
                self.ch_board[self.i + 1][self.j - 1] = ''
                self.ch_board[self.i + 1][self.j - 1] = None

                self.ch_board[self.i + 2][self.j - 2] = '⚫'
                self.flag_white = True
            else:
                print('qwqweqwe')
                self.i = self.old_i
                self.j = self.old_j
                self.flag_black = False

        remove_white(self)
        if may_eat_when_up(self) is True:
            print('MAYEATWHENUP_TRUE')
            eat(self)
        else:
            create_white(self)
            # print('MAYEATWHENUP_False')

        remove_black(self)
        create_black(self)

        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(Qt.black)

        def drawing_table(self):
            for i in range(len(self.ch_board)):
                row = self.ch_board[i]
                for j in range(len(row)):
                    self.x = j * self._size_cell
                    self.y = i * self._size_cell
                    self.w = self._size_cell
                    self.h = self._size_cell

                    painter.drawRect(self.x, self.y, self.w, self.h)
                    painter.save()
                    painter.setFont(QFont('Arial', 26))

                    value = self.ch_board[i][j]
                    painter.setPen(Qt.black if value == '⚪' else Qt.black)
                    painter.drawText(self.x, self.y, self.w, self.h, Qt.AlignCenter, value)
                    painter.restore()

        drawing_table(self)
        self.drawcell(painter)

    def drawcell(self, painter):
        painter.setBrush(QColor(0, 255, 255))
        for i in range(1, 9):
            for j in range(1, 9):
                if (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 == 0):
                    painter.drawRect(self._size_cell * i, self._size_cell * j, self._size_cell, self._size_cell)


if __name__ == '__main__':
    app = QApplication([])
    w = Window()
    w.show()
app.exec()
