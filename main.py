import json

conteudo = open('source_file_2.json').read()

mainDict = json.loads(conteudo)
managersDict = dict()
managersDict2 = dict()
watchersDict = dict()
watchersDict2 = dict()

for item in mainDict:
  for x in item['managers']:
    if not x in managersDict:
        managersDict[x] = dict()
    managersDict[x][item['name']] = item['priority']
for x in managersDict:
    for item in sorted(managersDict[x], key = managersDict[x].get):
        if not x in managersDict2:
            managersDict2[x] = list()
        managersDict2[x].append(item)

for item in mainDict:
  for x in item['watchers']:
    if not x in watchersDict:
        watchersDict[x] = dict()
    watchersDict[x][item['name']] = item['priority']
for x in watchersDict:
    for item in sorted(watchersDict[x], key = watchersDict[x].get):
        if not x in watchersDict2:
            watchersDict2[x] = list()
        watchersDict2[x].append(item)

listaManagers = list()
listaWatchers = list()
listaManagers.append(managersDict2)
listaWatchers.append(watchersDict2)

def write(mlist,name):
    f = open(f'{name}.json', 'w')
    json.dump(mlist, f,indent=4)
write(listaManagers,"managers")
write(listaWatchers,"watchers")