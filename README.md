to run

start server

`
$ python3 server.py
`

open other terminals, start other clients making requests, like the ff makes 100 requests

`
$ python3 client.py 100
`

client terminals will be updated concurrently, see screenshot:

![img](screenshot.jpg)

# delays

their updates are delayed because of the `time.sleep(0.1)` call which i added for rate limiting and reduce resources being hogged. 

i'm using `http.server` which is single threaded based on their source code here [https://github.com/python/cpython/blob/3.11/Lib/http/server.py](https://github.com/python/cpython/blob/3.11/Lib/http/server.py) where it builds upon socketserver, looking at their code, there doesnt seem to be a pattern where each incoming request has a new thread getting spawned to handle it. thus have to limit the requests.

as well as to visually demo it better and "mimic" real world scenarios

# distributed locking

it's a simple version of distributed locking, made on a quick friday morning minutes after waking up cause i got bored and curious from something i read last night. it's very simple, one central server that manages the lock, in real life it's a cluster of servers using some consensus algorithm to decide which gets lock


this simple version demos distributed locking in a simple setup of multiple client nodes accessing a shared resource which in this case is the counter that is managed by the server to ensure sequential access