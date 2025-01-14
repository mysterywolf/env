# -*- coding:utf-8 -*-
#
# File      : cmds.py
# This file is part of RT-Thread RTOS
# COPYRIGHT (C) 2006 - 2018, RT-Thread Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Change Logs:
# Date           Author          Notes
# 2018-5-28      SummerGift      Add copyright information
#

__all__ = ['cmd_package', 'cmd_system', 'cmd_menuconfig', 'cmd_sdk']

try:
    import requests
except ImportError:
    print("****************************************\n"
          "* Import requests module error.\n"
          "* Please install requests module first.\n"
          "* pip install step:\n"
          "* $ pip install requests\n"
          "* command install step:\n"
          "* $ sudo apt-get install python-requests\n"
          "****************************************\n")
