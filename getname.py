'''
Place this file in the same folder as /Content/
'''

import os
import json

def GetFileList(PATH):

	fileList = os.listdir(PATH)
	files = list()

	for entry in fileList:
		fullPath = os.path.join(PATH, entry)

		# If entry is a sub-directory, then get list of files from it
		if os.path.isdir(fullPath):
			files = files + GetFileList(fullPath)
		else:
			files.append(fullPath)

	return files

os.system('chcp 65001')
os.system('cls')

print("--------------------------------------")
print(" Searching & Listing .png files")
print("--------------------------------------")

# Set path & get all files
contentPath  = 'Content\\'
contentFiles = GetFileList(contentPath)

actorsPath  = 'Content\\Actors\\'
actorsFiles = GetFileList(actorsPath)

componentsPath  = 'Content\\Components\\'
componentsFiles = GetFileList(componentsPath)

content_dlc3Path  = 'Content\\Content_DLC3\\'
content_dlc3Files = GetFileList(content_dlc3Path)

content_dlc4Path  = 'Content\\Content_DLC4\\'
content_dlc4Files = GetFileList(content_dlc4Path)

content_dlc5Path  = 'Content\\Content_DLC5\\'
content_dlc5Files = GetFileList(content_dlc5Path)

content_dlc6Path  = 'Content\\Content_DLC6\\'
content_dlc6Files = GetFileList(content_dlc6Path)

cuesPath  = 'Content\\Cues\\'
cuesFiles = GetFileList(cuesPath)

decorPath  = 'Content\\Decor\\'
decorFiles = GetFileList(decorPath)

effectsPath  = 'Content\\Effects\\'
effectsFiles = GetFileList(effectsPath)

materialsPath  = 'Content\\Materials\\'
materialsFiles = GetFileList(materialsPath)

modelsPath  = 'Content\\Models\\'
modelsFiles = GetFileList(modelsPath)

patch1Path  = 'Content\\Patch1\\'
patch1Files = GetFileList(patch1Path)

patch2Path  = 'Content\\Patch2\\'
patch2Files = GetFileList(patch2Path)

saveiconsPath  = 'Content\\SaveIcons\\'
saveiconsFiles = GetFileList(saveiconsPath)

texturesPath  = 'Content\\Textures\\'
texturesFiles = GetFileList(texturesPath)

uiPath  = 'Content\\UI\\'
uiFiles = GetFileList(uiPath)

indicatorPath = 'Content\\indicator.png' 

# filter files
contentFilesFiltered = [ contentFile for contentFile in contentFiles if contentFile.endswith(".png") ] + [ contentFile for contentFile in contentFiles if contentFile.endswith(".tga") ]

actorsFilesFiltered = [ actorsFile for actorsFile in actorsFiles if actorsFile.endswith(".png") ] + [ actorsFile for actorsFile in actorsFiles if actorsFile.endswith(".tga") ]
componentsFilesFiltered = [ componentsFile for componentsFile in componentsFiles if componentsFile.endswith(".png") ] + [ componentsFile for componentsFile in componentsFiles if componentsFile.endswith(".tga") ]
content_dlc3FilesFiltered = [ content_dlc3File for content_dlc3File in content_dlc3Files if content_dlc3File.endswith(".png") ] + [ content_dlc3File for content_dlc3File in content_dlc3Files if content_dlc3File.endswith(".tga") ]
content_dlc4FilesFiltered = [ content_dlc4File for content_dlc4File in content_dlc4Files if content_dlc4File.endswith(".png") ] + [ content_dlc4File for content_dlc4File in content_dlc4Files if content_dlc4File.endswith(".tga") ]
content_dlc5FilesFiltered = [ content_dlc5File for content_dlc5File in content_dlc5Files if content_dlc5File.endswith(".png") ] + [ content_dlc5File for content_dlc5File in content_dlc5Files if content_dlc5File.endswith(".tga") ]
content_dlc6FilesFiltered = [ content_dlc6File for content_dlc6File in content_dlc6Files if content_dlc6File.endswith(".png") ] + [ content_dlc6File for content_dlc6File in content_dlc6Files if content_dlc6File.endswith(".tga") ]
cuesFilesFiltered = [ cuesFile for cuesFile in cuesFiles if cuesFile.endswith(".png") ] + [ cuesFile for cuesFile in cuesFiles if cuesFile.endswith(".tga") ]
decorFilesFiltered = [ decorFile for decorFile in decorFiles if decorFile.endswith(".png") ] + [ decorFile for decorFile in decorFiles if decorFile.endswith(".tga") ]
effectsFilesFiltered = [ effectsFile for effectsFile in effectsFiles if effectsFile.endswith(".png") ] + [ effectsFile for effectsFile in effectsFiles if effectsFile.endswith(".tga") ]
materialsFilesFiltered = [ materialsFile for materialsFile in materialsFiles if materialsFile.endswith(".png") ] + [ materialsFile for materialsFile in materialsFiles if materialsFile.endswith(".tga") ]
modelsFilesFiltered = [ modelsFile for modelsFile in modelsFiles if modelsFile.endswith(".png") ] + [ modelsFile for modelsFile in modelsFiles if modelsFile.endswith(".tga") ]
patch1FilesFiltered = [ patch1File for patch1File in patch1Files if patch1File.endswith(".png") ] + [ patch1File for patch1File in patch1Files if patch1File.endswith(".tga") ]
patch2FilesFiltered = [ patch2File for patch2File in patch2Files if patch2File.endswith(".png") ] + [ patch2File for patch2File in patch2Files if patch2File.endswith(".tga") ]
saveiconsFilesFiltered = [ saveiconsFile for saveiconsFile in saveiconsFiles if saveiconsFile.endswith(".png") ] + [ saveiconsFile for saveiconsFile in saveiconsFiles if saveiconsFile.endswith(".tga") ]
texturesFilesFiltered = [ texturesFile for texturesFile in texturesFiles if texturesFile.endswith(".png") ] + [ texturesFile for texturesFile in texturesFiles if texturesFile.endswith(".tga") ]
uiFilesFiltered = [ uiFile for uiFile in uiFiles if uiFile.endswith(".png") ] + [ uiFile for uiFile in uiFiles if uiFile.endswith(".tga") ]


# list files
count = 0

contentData      = []

actorsData       = []
componentsData   = []
content_dlc3Data = []
content_dlc4Data = []
content_dlc5Data = []
content_dlc6Data = []
cuesData         = []
decorData        = []
effectsData      = []
materialsData    = []
modelsData       = []
patch1Data       = []
patch2Data       = []
saveiconsData    = []
texturesData     = []
uiData           = []

for contentFile in contentFilesFiltered:
	contentData.append(contentFile.replace('\\', '/').replace('Content/', ''))
with open('Content.json', 'w') as contentJSON:
	json.dump(contentData, contentJSON, indent=2)

for actorsFile in actorsFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",actorsFile)
	count += 1
	actorsData.append(actorsFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Actors.json', 'w') as actorsJSON:
	json.dump(actorsData, actorsJSON, indent=2)

for componentsFile in componentsFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",componentsFile)
	count += 1
	componentsData.append(componentsFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Components.json', 'w') as componentsJSON:
	json.dump(componentsData, componentsJSON, indent=2)

for content_dlc3File in content_dlc3FilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",content_dlc3File)
	count += 1
	content_dlc3Data.append(content_dlc3File.replace('\\', '/').replace('Content/', ''))
with open('json\\Content_DLC3.json', 'w') as content_dlc3JSON:
	json.dump(content_dlc3Data, content_dlc3JSON, indent=2)

for content_dlc4File in content_dlc4FilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",content_dlc4File)
	count += 1
	content_dlc4Data.append(content_dlc4File.replace('\\', '/').replace('Content/', ''))
with open('json\\Content_DLC4.json', 'w') as content_dlc4JSON:
	json.dump(content_dlc4Data, content_dlc4JSON, indent=2)

for content_dlc5File in content_dlc5FilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",content_dlc5File)
	count += 1
	content_dlc5Data.append(content_dlc5File.replace('\\', '/').replace('Content/', ''))
with open('json\\Content_DLC5.json', 'w') as content_dlc5JSON:
	json.dump(content_dlc5Data, content_dlc5JSON, indent=2)

for content_dlc6File in content_dlc6FilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",content_dlc6File)
	count += 1
	content_dlc6Data.append(content_dlc6File.replace('\\', '/').replace('Content/', ''))
with open('json\\Content_DLC6.json', 'w') as content_dlc6JSON:
	json.dump(content_dlc6Data, content_dlc6JSON, indent=2)

for cuesFile in cuesFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",cuesFile)
	count += 1
	cuesData.append(cuesFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Cues.json', 'w') as cuesJSON:
	json.dump(cuesData, cuesJSON, indent=2)

for decorFile in decorFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",decorFile)
	count += 1
	decorData.append(decorFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Decor.json', 'w') as decorJSON:
	json.dump(decorData, decorJSON, indent=2)

for effectsFile in effectsFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",effectsFile)
	count += 1
	effectsData.append(effectsFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Effects.json', 'w') as effectsJSON:
	json.dump(effectsData, effectsJSON, indent=2)

for materialsFile in materialsFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",materialsFile)
	count += 1
	materialsData.append(materialsFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Materials.json', 'w') as materialsJSON:
	json.dump(materialsData, materialsJSON, indent=2)

for modelsFile in modelsFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",modelsFile)
	count += 1
	modelsData.append(modelsFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Models.json', 'w') as modelsJSON:
	json.dump(modelsData, modelsJSON, indent=2)

for patch1File in patch1FilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",patch1File)
	count += 1
	patch1Data.append(patch1File.replace('\\', '/').replace('Content/', ''))
with open('json\\Patch1.json', 'w') as patch1JSON:
	json.dump(patch1Data, patch1JSON, indent=2)

for patch2File in patch2FilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",patch2File)
	count += 1
	patch2Data.append(patch2File.replace('\\', '/').replace('Content/', ''))
with open('json\\Patch2.json', 'w') as patch2JSON:
	json.dump(patch2Data, patch2JSON, indent=2)

for saveiconsFile in saveiconsFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",saveiconsFile)
	count += 1
	saveiconsData.append(saveiconsFile.replace('\\', '/').replace('Content/', ''))
with open('json\\SaveIcons.json', 'w') as saveiconsJSON:
	json.dump(saveiconsData, saveiconsJSON, indent=2)

for texturesFile in texturesFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",texturesFile)
	count += 1
	texturesData.append(texturesFile.replace('\\', '/').replace('Content/', ''))
with open('json\\Textures.json', 'w') as texturesJSON:
	json.dump(texturesData, texturesJSON, indent=2)

for uiFile in uiFilesFiltered:
	print("\x1b[1m \x1b[32m Found : \x1b[0m",uiFile)
	count += 1
	uiData.append(uiFile.replace('\\', '/').replace('Content/', ''))
with open('json\\UI.json', 'w') as uiJSON:
	json.dump(uiData, uiJSON, indent=2)

print()
print("-----------------------------------------------")
print("\x1b[1m \x1b[32m Found",count,"files \x1b[0m")
print("-----------------------------------------------")