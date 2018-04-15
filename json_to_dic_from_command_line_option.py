#JSON String to Dic when a JSON Obbj
#is passed as a command line argument
def jsonToDict(jsonStr):
   '''
   Helper function to load passed json string object into dict
   '''
   jsonList = [l.strip('{}:,') for l in jsonStr]
   patchHeader = {}
   list_length = len(jsonList)
   increment = 0
   while(increment<list_length-1):
       if(jsonList[increment] != "leaf_services"):
           patchHeader[jsonList[increment]] = jsonList[increment+1]
           increment += 2
       else:
           service_list = []
           increment += 1
           while(jsonList[increment][-1] != ']'):
               service_list.append(jsonList[increment].strip('[]'))
               increment += 1
           service_list.append(jsonList[increment].strip('[]'))
           increment += 1
           patchHeader["leaf_services"] = service_list
   return patchHeader
