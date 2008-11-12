# Copyright (C) 2008 Valmantas Paliksa <walmis at balticum-tv dot lt>
# Copyright (C) 2008 Tadas Dailyda <tadas at dailyda dot com>
#
# Licensed under the GNU General Public License Version 3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

import dbus

class OdsBase(dbus.proxies.Interface):
	
	def OdsMethod(fn):
		def new(self, *args, **kwargs):

			fn(self, *args, **kwargs)
			getattr(super(OdsBase,self), fn.__name__)(*args, **kwargs)
		return new
	
	def __init__(self, service_name, obj_path):
		self.bus = dbus.SessionBus()
		
		service = self.bus.get_object("org.openobex", obj_path)
		dbus.proxies.Interface.__init__(self, service, service_name)
