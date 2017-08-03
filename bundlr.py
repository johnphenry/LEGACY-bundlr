import os
import sys
from subprocess import call
NAME = sys.argv[1]
BUNDNAME = NAME + ".app"
os.mkdir( BUNDNAME )
call("makeicns","-512", "icon.png", "-32", "icon.png")
os.rename(NAME, BUNDNAME+"/"+"icon.icns")
os.rename(NAME, BUNDNAME+"/"+NAME)
os.chdir( BUNDNAME )
file = open("Info.plist", "w")
plistFileText = """
<?xml version = "1.0" encoding="ASCII"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleExecutable</key>
	<string>"""+NAME+"""</string>
	<key>CFBundleIdentifier</key>
	<string>com.john-henry."""+NAME+"""</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CDBundleName</key>
	<string>"""+NAME+"""</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
    <key>CFBundleIconFile</key>
    <string>icon</string>
</dict>
</plist>"""
file.write( plistFileText )
