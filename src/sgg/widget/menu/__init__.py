from tkinter import Menu as tkmenu

from sgg.models import _do_func, _setDefaultValues2, _setDefaultValues3

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
            "menubar": None,
            "name": None,
            "postcommand": "",
            "relief": None,
            "selectcolor": None,
            "takefocus": 0,
            "tearoff": 1,
            "tearoffcommand": "",
            "title": "",
            "type": "normal",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._set_dict = _setDefaultValues3(self._default_dict, {"menubar"})
        super().__init__(master, **self._set_dict)
        menubar = self._default_dict["menubar"]
        if menubar is not None:
            self._create_menu(menubar)

    def _create_menu(self, menu):
        self.delete(0, "end")
        for menus in menu:
            if not isinstance(menus, dict):
                continue
            for key, val in menus.items():
                submenu = tkmenu(self, **self._set_dict)
                self._add_items_recursive(submenu, val)
                self.add_cascade(label=key, menu=submenu)

    def _add_items_recursive(self, menu: tkmenu, item):
        for items in item:
            if items == "---":
                menu.add_separator()
            elif isinstance(items, str):
                menu.add_command(label=items)
            elif isinstance(items, dict):
                menu.add_command(
                    label=items.get("label", ""),
                    command=lambda x=items.get("command", None): _do_func(x),
                )
