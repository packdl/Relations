# A Relationship calculator gramplet using QRCodes
# $Id$

"""Gramplet/QRCode Relationship Calculator"""

from __future__ import unicode_literals

#------------------------------------------------------------------------
#
# GTK+ modules
#
#------------------------------------------------------------------------


from gi.repository import Gtk, GtkSource, GObject



d = 1

#------------------------------------------------------------------------
#
# GRAMPS modules
#  
#------------------------------------------------------------------------
#from gramps.gen.display.name import displayer
from gramps.gen.plug import Gramplet

#------------------------------------------------------------------------
#
# Relations Gramplet
#
#------------------------------------------------------------------------
class QRCodeRelationshipGramplet(Gramplet):
    
    def init(self):
        self.gui.WIDGET =self.build_gui()
        self.gui.get_container_widget().remove(self.gui.textview)
        self.gui.get_container_widget().add_with_viewport(self.gui.WIDGET)
        self.mainbox.show_all()
        
    def build_gui(self):
        """
        Making the GUI
        """
        
        
                