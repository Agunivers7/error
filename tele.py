Traceback (most recent call last):
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 1348, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1282, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1328, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1277, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1037, in _send_output
    self.send(msg)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 975, in send
    self.connect()
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1447, in connect
    super().connect()
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 941, in connect
    self.sock = self._create_connection(
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\socket.py", line 845, in create_connection
    raise err
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\socket.py", line 833, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "e:\facerego\face.py", line 9, in <module>
    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 519, in open
    response = self._open(req, data)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 536, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 496, in _call_chain
    result = func(*args)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 1391, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>
PS C:\Users\AADHITHYA> & C:/Users/AADHITHYA/AppData/Local/Programs/Python/Python310/python.exe e:/facerego/face.py
Traceback (most recent call last):
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 1348, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1282, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1328, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1277, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1037, in _send_output
    self.send(msg)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 975, in send
    self.connect()
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1447, in connect
    super().connect()
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 941, in connect
    self.sock = self._create_connection(
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\socket.py", line 845, in create_connection
    raise err
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\socket.py", line 833, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "e:\facerego\face.py", line 9, in <module>
    img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 519, in open
    response = self._open(req, data)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 536, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 496, in _call_chain
    result = func(*args)
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 1391, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Users\AADHITHYA\AppData\Local\Programs\Python\Python310\lib\urllib\request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>
PS C:\Users\AADHITHYA>
