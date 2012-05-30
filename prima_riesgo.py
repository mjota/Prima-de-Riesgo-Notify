#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Prima de riesgo Notify - Notificador periódico de prima de riesgo
# Copyright (c) 2012 - Manuel Joaquin Díaz Pol
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
#==============================================================================
#

import time
import twitter
import re
from gi.repository import Notify

TWITNAME = "PrimaRiesgoBot"
TIMEWAIT = 600

class Main():
    def __init__(self):
        self.api = twitter.Api()
        
        Notify.init("PrimadeRiesgo")
        self.notif = Notify.Notification.new ("Prima de riesgo","Notificación periódica activada","dialog-information")
        self.notif.show()
        
        time.sleep(3)
        self.show_prima()
            
    def show_prima(self): 
        statuses = self.api.GetUserTimeline(TWITNAME)
        twit = re.split("//", statuses[0].text)
        self.notif.update("Prima de riesgo", twit[0] + " Cambio: " + twit[1], "dialog-information")
        self.notif.show()  
    
    def time_update(self):
        n = 0
        while(1):
            time.sleep(1)
            n+=1
            if(n>=TIMEWAIT):
                self.show_prima()
                n=0  
      
if __name__ == '__main__':
    prima = Main()
    prima.time_update()
