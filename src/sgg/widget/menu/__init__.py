from tkinter import Menu as tkmenu

from sgg.models import _setDefaultValues2

__all__ = ("Menu",)


class Menu(tkmenu):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "activebackground": None,
            "activeborderwidth": None,
            "activeforeground": None,
            "background": None,
            "bd": None,
            "bg": None,
            "border": None,
            "borderwidth": None,
            "cursor": "arrow",
            "disabledforeground": None,
            "fg": None,
            "font": None,
            "foreground": None,
            "name": None,
            "postcommand": "",
            "relief": None,
            "selectcolor": None,
            "takefocus": 0,
            "tearoff": 1,
            "tearoffcommand": "",
            "title": "",
            "type": "normal",
            "menubar": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        menubar = self._default_dict.pop("menubar", None)
        super().__init__(master, self._default_dict)
        if menubar is not None:
            self._create_menu(menubar)

    def _create_menu(self, menu):
        self.delete(0, "end")
        for menus in menu:
            if not isinstance(menus, dict):
                continue
            for key, val in menus.items():
                submenu = tkmenu(self, self._default_dict)
                self._add_items_recursive(submenu, val)
                self.add_cascade(label=key, menu=submenu)

    def _add_items_recursive(self, menu: tkmenu, item):
        for items in item:
            if items == "---":
                menu.add_separator()
            elif isinstance(items, str):
                menu.add_command(label=items)
            elif isinstance(items, dict):
                label = items.get("label", "")
                command = items.get("command", "")
                menu.add_command(label=label, command=command)
