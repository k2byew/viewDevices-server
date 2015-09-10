Netdiscover's OUI list is oudated, need to recompile to update the list: http://unix.stackexchange.com/questions/25053/how-can-i-update-the-oui-list-used-for-netdiscover

Netdiscover provides a script to update oui.h, the but file generated has unnecessary new lines which breaks the build.

An updated and valid oui.h is kept here for convenience.
