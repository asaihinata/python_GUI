from sgg.font import TKFont
from sgg.popup import (Popup, PopupError, PopupInformation, PopupQuestion,
                       PopupWarning)
from sgg.version import __version__, __version_info__
from sgg.widget import *


class gui:
    @classmethod
    def window(cls, cnf={}, **kw):
        return Window(cnf, **kw)

    @staticmethod
    def Label(**kw):
        return {"type": "label", "kw": kw}

    @staticmethod
    def Image(**kw):
        return {"type": "Image", "kw": kw}

    @staticmethod
    def Button(**kw):
        return {"type": "Button", "kw": kw}

    @staticmethod
    def AskColorButton(**kw):
        return {"type": "AskColorButton", "kw": kw}

    @staticmethod
    def AskDirectoryButton(**kw):
        return {"type": "AskDirectoryButton", "kw": kw}

    @staticmethod
    def AskFileButton(**kw):
        return {"type": "AskFileButton", "kw": kw}

    @staticmethod
    def SaveFileButton(**kw):
        return {"type": "SaveFileButton", "kw": kw}

    @staticmethod
    def Checkbutton(**kw):
        return {"type": "Checkbutton", "kw": kw}

    @staticmethod
    def Radiobutton(**kw):
        return {"type": "Radiobutton", "kw": kw}

    @staticmethod
    def Scale(**kw):
        return {"type": "Scale", "kw": kw}

    @staticmethod
    def Listbox(**kw):
        return {"type": "Listbox", "kw": kw}

    @staticmethod
    def Text(**kw):
        return {"type": "Text", "kw": kw}

    @staticmethod
    def Entry(**kw):
        return {"type": "Entry", "kw": kw}

    @staticmethod
    def Spinbox(**kw):
        return {"type": "Spinbox", "kw": kw}

    @staticmethod
    def Menu(**kw):
        return {"type": "Menu", "kw": kw}

    @staticmethod
    def Frame(**kw):
        return {"type": "Frame", "kw": kw}

    @staticmethod
    def FrameLabel(**kw):
        return {"type": "FrameLabel", "kw": kw}

    @staticmethod
    def TLabel(**kw):
        return {"type": "TLabel", "kw": kw}

    @staticmethod
    def TImage(**kw):
        return {"type": "TImage", "kw": kw}

    @staticmethod
    def TButton(**kw):
        return {"type": "TButton", "kw": kw}

    @staticmethod
    def TAskColorButton(**kw):
        return {"type": "TAskColorButton", "kw": kw}

    @staticmethod
    def TAskDirectoryButton(**kw):
        return {"type": "TAskDirectoryButton", "kw": kw}

    @staticmethod
    def TAskFileButton(**kw):
        return {"type": "TAskFileButton", "kw": kw}

    @staticmethod
    def TSaveFileButton(**kw):
        return {"type": "TSaveFileButton", "kw": kw}

    @staticmethod
    def TCheckbutton(**kw):
        return {"type": "TCheckbutton", "kw": kw}

    @staticmethod
    def TRadiobutton(**kw):
        return {"type": "TRadiobutton", "kw": kw}

    @staticmethod
    def TSpinbox(**kw):
        return {"type": "TSpinbox", "kw": kw}

    @staticmethod
    def TEntry(**kw):
        return {"type": "TEntry", "kw": kw}

    @staticmethod
    def TScale(**kw):
        return {"type": "TScale", "kw": kw}

    @staticmethod
    def TProgressbar(**kw):
        return {"type": "TProgressbar", "kw": kw}

    @staticmethod
    def TFrame(**kw):
        return {"type": "TFrame", "kw": kw}

    @staticmethod
    def TFrameLabel(**kw):
        return {"type": "TFrameLabel", "kw": kw}

    @staticmethod
    def TNotebook(**kw):
        return {"type": "TNotebook", "kw": kw}

    @staticmethod
    def Plot(**kw):
        return {"type": "Plot", "kw": kw}

    @staticmethod
    def Scatter(**kw):
        return {"type": "Scatter", "kw": kw}


def __dir__():
    return (i for i in globals().keys() if i.startswith("__") or not i.startswith("_"))
