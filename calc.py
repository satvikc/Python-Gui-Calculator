# Python-Gui-calc
# Created by Satvik Chauhan
# Copyright 2011 Satvik Chauhan .
import pygtk
pygtk.require('2.0')
import gtk
import sys, string
buffer = []
memory=''
def make_box(homogeneous, spacing, expand, fill, padding,var,entry):
    box = gtk.HBox(homogeneous, spacing)
    for i in var:
        button = gtk.Button(i)
        button.connect("clicked",action,i,entry)
        box.pack_start(button, expand, fill, padding)
        button.show()
    return box
def action(widget,var,entry):
    global memory
    if (var=='space'):
        x=entry.get_text()
        entry.set_text(x+' ')
    elif (var=='Clear'):
        entry.set_text('')
    elif(var=='='):
        x=entry.get_text()
        x=x.replace(" ","")
        try:
            entry.set_text(str(eval(x)))
        except:
            entry.set_text("Can't Be Done")
    else:
        x=entry.get_text()
        entry.set_text(x+var)
class calc:
    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)
        box1 = gtk.VBox(False, 0)
        entry = gtk.Entry()
        entry.set_text("")
        box1.pack_start(entry,False,False,0)
        entry.show()
        box2 = make_box(False, 10, True, True, 0,['1','2','3','+'],entry)
        box1.pack_start(box2, False, False, 0)
        box2.show()
        box2 = make_box(False, 10, True, True, 0,['4','5','6','-'],entry)
        box1.pack_start(box2, False, False, 0)
        box2.show()
        box2 = make_box(False, 10, True, True, 0,['7','8','9','*'],entry)
        box1.pack_start(box2, False, False, 0)
        box2.show()
        box2 = make_box(False, 10, True, True, 0,['.','0','Clear','/'],entry)
        box1.pack_start(box2, False, False, 0)
        box2.show()
        box2 = make_box(False, 10, True, True, 0,['(',')','%','='],entry)
        box1.pack_start(box2, False, False, 0)
        box2.show()
        box2 = make_box(False, 10, True, True, 0,['space'],entry)
        box1.pack_start(box2, False, False, 0)
        box2.show()
        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 5)
        separator.show()
        separator = gtk.HSeparator()
        box1.pack_start(separator, False, True, 5)
        separator.show()
        quitbox = gtk.HBox(False, 0)
        button = gtk.Button("Quit")
        button.connect("clicked", lambda w: gtk.main_quit())
        quitbox.pack_start(button, True, False, 0)
        box1.pack_start(quitbox, False, False, 0)
        self.window.add(box1)
        button.show()
        quitbox.show()
        box1.show()
        self.window.show()
def main():
    gtk.main()
    return 0         
if __name__ =="__main__":
    calc()
    main()
