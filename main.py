from Modele import Gamer
from Modele import Match
from Modele import Round
from Modele import Tournament
from Modele import Models
from view import View
from view import MenuView
from Controleur import ControllerMenu
from Controleur import Controller


def main():
    models = Models(Tournament(), Gamer(), Round(), Match())
    view = View(MenuView())
    controller = Controller(view, models)
    menu = ControllerMenu(view, controller)
    menu.execute()


if __name__ == "__main__":
    while True:
        main()
