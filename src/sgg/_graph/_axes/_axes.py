"""
References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html
    https://matplotlib.org/stable/api/ticker_api.html
    https://matplotlib.org/stable/api/dates_api.html
"""

from matplotlib.axes import Axes
from matplotlib.dates import (AutoDateLocator, DateFormatter, DayLocator,
                              HourLocator, MicrosecondLocator, MinuteLocator,
                              MonthLocator, SecondLocator, WeekdayLocator,
                              YearLocator)
from matplotlib.scale import ScaleBase
from matplotlib.ticker import (AutoLocator, FuncFormatter, LogLocator,
                               MaxNLocator, NullFormatter, NullLocator,
                               PercentFormatter, ScalarFormatter,
                               StrMethodFormatter)

from sgg._constant import _SCALE_TUPLE

__all__ = ("_AXES",)


class _AXES:
    # axis
    _ax: Axes

    @property
    def ax(self) -> Axes:
        return self._ax

    # x軸
    def set_xlim(self, min=None, max=None, *, emit=True, auto=False):
        self._ax.set_xlim(min, max, emit=emit, auto=auto)
        self._redraw()

    def get_xlim(self):
        return self._ax.get_xlim()

    def set_xbound(self, min=None, max=None):
        self._ax.set_xbound(min, max)
        self._redraw()

    def get_xbound(self):
        return self._ax.get_xbound()

    def set_xlabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        self._ax.set_xlabel(label, fontdict, labelpad, loc=loc, **kw)
        self._redraw()

    def get_xlabel(self):
        return self._ax.get_xlabel()

    def set_xticks(self, ticks, labels=None, *, minor=False, **kw):
        self._ax.set_xticks(ticks, labels=labels, minor=minor, **kw)
        self._redraw()

    def get_xticks(self, *, minor=False):
        return self._ax.get_xticks(minor=minor)

    def set_xscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_xscale(value, **kw)
            self._redraw()

    def get_xscale(self):
        return self._ax.get_xscale()

    # ticker
    # x_ticker_major
    def xmajor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.xaxis.set_major_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def xmajor_auto(self):
        self._ax.xaxis.set_major_locator(AutoLocator())
        self._redraw()

    def xmajor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.xaxis.set_major_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def xmajor_hide(self):
        self._ax.xaxis.set_major_locator(NullLocator())
        self._redraw()

    def xmajor_strformat(self, format):
        self._ax.xaxis.set_major_formatter(StrMethodFormatter(format))
        self._redraw()

    def xmajor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.xaxis.set_major_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def xmajor_funcformat(self, func):
        self._ax.xaxis.set_major_formatter(FuncFormatter(func))
        self._redraw()

    def xmajor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.xaxis.set_major_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def xmajor_hideformat(self):
        self._ax.xaxis.set_major_formatter(NullFormatter())
        self._redraw()

    # 日付
    def xmajor_yearlocator(self, base=1, month=1, day=1, tz=None):
        self._ax.xaxis.set_major_locator(YearLocator(base, month, day, tz))
        self._redraw()

    def xmajor_monthlocator(self, bymonth=None, bymonthday=1, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(
            MonthLocator(bymonth, bymonthday, interval, tz)
        )
        self._redraw()

    def xmajor_weekdaylocator(self, byweekday=1, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(WeekdayLocator(byweekday, interval, tz))
        self._redraw()

    def xmajor_daylocator(self, bymonthday=None, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(DayLocator(bymonthday, interval, tz))
        self._redraw()

    def xmajor_hourlocator(self, byhour=None, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(HourLocator(byhour, interval, tz))
        self._redraw()

    def xmajor_minutelocator(self, byminute=None, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(MinuteLocator(byminute, interval, tz))
        self._redraw()

    def xmajor_secondlocator(self, bysecond=None, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(SecondLocator(bysecond, interval, tz))
        self._redraw()

    def xmajor_microsecondlocator(self, interval=1, tz=None):
        self._ax.xaxis.set_major_locator(MicrosecondLocator(interval, tz))
        self._redraw()

    def xmajor_autodatelocator(
        self, tz=None, minticks=5, maxticks=None, interval_multiples=True
    ):
        self._ax.xaxis.set_major_locator(
            AutoDateLocator(tz, minticks, maxticks, interval_multiples)
        )
        self._redraw()

    def xmajor_dateformat(self, fmt, tz=None, *, usetex=None):
        self._ax.xaxis.set_major_formatter(DateFormatter(fmt, tz, usetex=usetex))
        self._redraw()

    # x_ticker_minor
    def xminor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.xaxis.set_minor_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def xminor_auto(self):
        self._ax.xaxis.set_minor_locator(AutoLocator())
        self._redraw()

    def xminor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.xaxis.set_minor_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def xminor_hide(self):
        self._ax.xaxis.set_minor_locator(NullLocator())
        self._redraw()

    def xminor_strformat(self, format):
        self._ax.xaxis.set_minor_formatter(StrMethodFormatter(format))
        self._redraw()

    def xminor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.xaxis.set_minor_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def xminor_funcformat(self, func):
        self._ax.xaxis.set_minor_formatter(FuncFormatter(func))
        self._redraw()

    def xminor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.xaxis.set_minor_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def xminor_hideformat(self):
        self._ax.xaxis.set_minor_formatter(NullFormatter())
        self._redraw()

    # 日付
    def xminor_yearlocator(self, base=1, month=1, day=1, tz=None):
        self._ax.xaxis.set_minor_locator(YearLocator(base, month, day, tz))
        self._redraw()

    def xminor_monthlocator(self, bymonth=None, bymonthday=1, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(
            MonthLocator(bymonth, bymonthday, interval, tz)
        )
        self._redraw()

    def xminor_weekdaylocator(self, byweekday=1, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(WeekdayLocator(byweekday, interval, tz))
        self._redraw()

    def xminor_daylocator(self, bymonthday=None, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(DayLocator(bymonthday, interval, tz))
        self._redraw()

    def xminor_hourlocator(self, byhour=None, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(HourLocator(byhour, interval, tz))
        self._redraw()

    def xminor_minutelocator(self, byminute=None, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(MinuteLocator(byminute, interval, tz))
        self._redraw()

    def xminor_secondlocator(self, bysecond=None, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(SecondLocator(bysecond, interval, tz))
        self._redraw()

    def xminor_microsecondlocator(self, interval=1, tz=None):
        self._ax.xaxis.set_minor_locator(MicrosecondLocator(interval, tz))
        self._redraw()

    def xminor_autodatelocator(
        self, tz=None, minticks=5, maxticks=None, interval_multiples=True
    ):
        self._ax.xaxis.set_minor_locator(
            AutoDateLocator(tz, minticks, maxticks, interval_multiples)
        )
        self._redraw()

    def xminor_dateformat(self, fmt, tz=None, *, usetex=None):
        self._ax.xaxis.set_minor_formatter(DateFormatter(fmt, tz, usetex=usetex))
        self._redraw()

    # y軸
    def set_ylim(self, min=None, max=None, *, emit=True, auto=False):
        self._ax.set_ylim(min, max, emit=emit, auto=auto)
        self._redraw()

    def get_ylim(self):
        return self._ax.get_ylim()

    def set_ybound(self, min=None, max=None):
        self._ax.set_ybound(min, max)
        self._redraw()

    def get_ybound(self):
        return self._ax.get_ybound()

    def set_ylabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        self._ax.set_ylabel(label, fontdict, labelpad, loc=loc, **kw)
        self._redraw()

    def get_ylabel(self):
        return self._ax.get_ylabel()

    def set_yticks(self, ticks, labels=None, *, minor=False, **kw):
        self._ax.set_yticks(ticks, labels=labels, minor=minor, **kw)
        self._redraw()

    def get_yticks(self, *, minor=False):
        return self._ax.get_yticks(minor=minor)

    def set_yscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_yscale(value, **kw)
            self._redraw()

    def get_yscale(self):
        return self._ax.get_yscale()

    # ticker
    # y_ticker_major
    def ymajor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.yaxis.set_major_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def ymajor_auto(self):
        self._ax.yaxis.set_major_locator(AutoLocator())
        self._redraw()

    def ymajor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.yaxis.set_major_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def ymajor_hide(self):
        self._ax.yaxis.set_major_locator(NullLocator())
        self._redraw()

    def ymajor_strformat(self, format):
        self._ax.yaxis.set_major_formatter(StrMethodFormatter(format))
        self._redraw()

    def ymajor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.yaxis.set_major_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def ymajor_funcformat(self, func):
        self._ax.yaxis.set_major_formatter(FuncFormatter(func))
        self._redraw()

    def ymajor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.yaxis.set_major_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def ymajor_hideformat(self):
        self._ax.yaxis.set_major_formatter(NullFormatter())
        self._redraw()

    # 日付
    def ymajor_yearlocator(self, base=1, month=1, day=1, tz=None):
        self._ax.yaxis.set_major_locator(YearLocator(base, month, day, tz))
        self._redraw()

    def ymajor_monthlocator(self, bymonth=None, bymonthday=1, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(
            MonthLocator(bymonth, bymonthday, interval, tz)
        )
        self._redraw()

    def ymajor_weekdaylocator(self, byweekday=1, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(WeekdayLocator(byweekday, interval, tz))
        self._redraw()

    def ymajor_daylocator(self, bymonthday=None, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(DayLocator(bymonthday, interval, tz))
        self._redraw()

    def ymajor_hourlocator(self, byhour=None, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(HourLocator(byhour, interval, tz))
        self._redraw()

    def ymajor_minutelocator(self, byminute=None, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(MinuteLocator(byminute, interval, tz))
        self._redraw()

    def ymajor_secondlocator(self, bysecond=None, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(SecondLocator(bysecond, interval, tz))
        self._redraw()

    def ymajor_microsecondlocator(self, interval=1, tz=None):
        self._ax.yaxis.set_major_locator(MicrosecondLocator(interval, tz))
        self._redraw()

    def ymajor_autodatelocator(
        self, tz=None, minticks=5, maxticks=None, interval_multiples=True
    ):
        self._ax.yaxis.set_major_locator(
            AutoDateLocator(tz, minticks, maxticks, interval_multiples)
        )
        self._redraw()

    def ymajor_dateformat(self, fmt, tz=None, *, usetex=None):
        self._ax.yaxis.set_major_formatter(DateFormatter(fmt, tz, usetex=usetex))
        self._redraw()

    # y_ticker_minor
    def yminor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.yaxis.set_minor_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def yminor_auto(self):
        self._ax.yaxis.set_minor_locator(AutoLocator())
        self._redraw()

    def yminor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.yaxis.set_minor_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def yminor_hide(self):
        self._ax.yaxis.set_minor_locator(NullLocator())
        self._redraw()

    def yminor_strformat(self, format):
        self._ax.yaxis.set_minor_formatter(StrMethodFormatter(format))
        self._redraw()

    def yminor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.yaxis.set_minor_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def yminor_funcformat(self, func):
        self._ax.yaxis.set_minor_formatter(FuncFormatter(func))
        self._redraw()

    def yminor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.yaxis.set_minor_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def yminor_hideformat(self):
        self._ax.yaxis.set_minor_formatter(NullFormatter())
        self._redraw()

    # 日付
    def yminor_yearlocator(self, base=1, month=1, day=1, tz=None):
        self._ax.yaxis.set_minor_locator(YearLocator(base, month, day, tz))
        self._redraw()

    def yminor_monthlocator(self, bymonth=None, bymonthday=1, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(
            MonthLocator(bymonth, bymonthday, interval, tz)
        )
        self._redraw()

    def yminor_weekdaylocator(self, byweekday=1, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(WeekdayLocator(byweekday, interval, tz))
        self._redraw()

    def yminor_daylocator(self, bymonthday=None, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(DayLocator(bymonthday, interval, tz))
        self._redraw()

    def yminor_hourlocator(self, byhour=None, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(HourLocator(byhour, interval, tz))
        self._redraw()

    def yminor_minutelocator(self, byminute=None, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(MinuteLocator(byminute, interval, tz))
        self._redraw()

    def yminor_secondlocator(self, bysecond=None, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(SecondLocator(bysecond, interval, tz))
        self._redraw()

    def yminor_microsecondlocator(self, interval=1, tz=None):
        self._ax.yaxis.set_minor_locator(MicrosecondLocator(interval, tz))
        self._redraw()

    def yminor_autodatelocator(
        self, tz=None, minticks=5, maxticks=None, interval_multiples=True
    ):
        self._ax.yaxis.set_minor_locator(
            AutoDateLocator(tz, minticks, maxticks, interval_multiples)
        )
        self._redraw()

    def yminor_dateformat(self, fmt, tz=None, *, usetex=None):
        self._ax.yaxis.set_minor_formatter(DateFormatter(fmt, tz, usetex=usetex))
        self._redraw()
