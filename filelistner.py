######################
#NOT USED
######################

#import pythoncom
#import wmi
#
#import jsonhandler
#
#def programlistner():
#    targetApplication = jsonhandler.read("config.json")["data"]["applicationToListenForCaption"]
#
#    pythoncom.CoInitialize() #init libaries
#    c = wmi.WMI()
#
#    for _ in c.Win32_Process(name=targetApplication): #for every process open, if it has the proper name, return true
#        return True
