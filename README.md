Websockets Shell
=============

This is a simple implementation of websockets to send and receive text commands and output.

The ws_server contains server_wsh.py that is the actual server that receives input and executes it against the Operating System giving shell like functionality. The output of the command is sent back via the websocket to the browser page where it is displayed.

You can use [pywebsocket] (https://code.google.com/p/pywebsocket/) to host the server_wsh.py file.

Installation
-----------

There is no installation as such. However, please note the following:
* This was tested sucessfully with [pywebsocket] (https://code.google.com/p/pywebsocket/). I cannot gaurantee it will work with other websocket servers, don't see why it won't work though.
* This shell was designed to work under Linux and Windows, but the file on github is for Windows. To make it work on Linux, replace the `cmd.exe /c` with `/bin/sh` or equivalent.
* There is no check for authentication or authorization. Any client would be able to connect and send and receive data (and take complete control over the server). Please feel free to commit or fork and add auth. There will be no revisions to this project from my end.


Usage
-----
To run the server on port 9998 (default in this code, can be changed):

1. Get [pywebsocket] (https://code.google.com/p/pywebsocket/)
2. Run `python pywebsocket\mod_pywebsocket\standalone.py -p 9998 -w ws_server`
3. Open index.html in any browser that supports websockets. Latest Chrome/Firefox is good enough.
4. Enter a (Windows) command like `ipconfig`
5. Hit the Execute! button.
6. Potato.


Closing notes
-------------

I built this as part of the popular Xtreme Web Hacking training that [Akash] (https://github.com/makash) and I deliver.

Contact
-------------

Twitter: @riyazwalikar
Twitter: @wincmdfu




