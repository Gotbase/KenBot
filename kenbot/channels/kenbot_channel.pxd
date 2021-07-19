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
cimport async_channel.channels as channels
cimport async_channel.consumer as consumers
cimport async_channel.producer as producers


cdef class kenbotChannel(channels.Channel):
    pass

cdef class kenbotChannelConsumer(consumers.Consumer):
    pass

cdef class kenbotChannelProducer(producers.Producer):
    pass
