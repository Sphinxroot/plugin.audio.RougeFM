########################################

import os, sys, xbmc, xbmcgui, xbmcplugin, xbmcaddon
	
#Radio Rouge FM en Direct By Sphinxroot QC

# Various constants used throughout the script
HANDLE = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.audio.RougeFM')
LANGUAGE  = ADDON.getLocalizedString
THUMBNAIL_PATH = os.path.join( ADDON.getAddonInfo( 'path' ), 'resources', 'media')

def start() :

	li = xbmcgui.ListItem(label=LANGUAGE(30000), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Amqui-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://17343.live.streamtheworld.com/CFVMFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30001), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Drummondvile-back-rouge.png'))		
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://18363.live.streamtheworld.com/CHRDFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30002), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Ottawa-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://20263.live.streamtheworld.com/CIMFFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30003), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Montreal-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://18073.live.streamtheworld.com/CITEFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30004), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Quebec-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://20793.live.streamtheworld.com/CITFFMAACTEST_48.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30005), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Rimouski-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://17443.live.streamtheworld.com/CJOIFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30006), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Sanguenay-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://17343.live.streamtheworld.com/CFIXFMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30007), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Estrie-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://17613.live.streamtheworld.com/CITE1FMAAC.aac", listitem=li, isFolder=False)
	li = xbmcgui.ListItem(label=LANGUAGE(30008), thumbnailImage=os.path.join(THUMBNAIL_PATH, 'Mauricie-back-rouge.png'))
	xbmcplugin.addDirectoryItem(handle=HANDLE, url="https://18123.live.streamtheworld.com/CHEYFMAAC.aac", listitem=li, isFolder=False)
	setViewMode("500")		
	xbmcplugin.endOfDirectory( HANDLE )		
	
def setViewMode(id):
	if xbmc.getSkinDir() == "skin.confluence":
		xbmc.executebuiltin("Container.SetViewMode(" + id + ")")
			
start()