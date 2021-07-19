# cython: language_level=3
#  gotbase kenbot
#  Copyright (c) gotbase, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
cimport kenbot.kenbot  as kenbot_class


cdef class kenbotBacktestingFactory(kenbot_class.kenbot):
    cdef object independent_backtesting
    cdef bint log_report
    cdef bint run_on_common_part_only
    cdef bint enable_join_timeout
