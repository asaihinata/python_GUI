from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

__all__ = ("_Base_Graph",)


class _set_figure_canvas(FigureCanvasTkAgg):
    def __init__(self, figure=None, master=None):
        super().__init__(figure, master)
        self.draw()


class _Base_Graph:
    def __new__(cls, master=None, figure=None):
        cls = _set_figure_canvas(figure=figure, master=master).get_tk_widget()
        return cls
