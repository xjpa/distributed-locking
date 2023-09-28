import http.client
import time
import sys

def increment_counter():
    connection = http.client.HTTPConnection('localhost', 8000)
    connection.request("GET", "/increment")
    response = connection.getresponse()
    print(f"Response: {response.read().decode()}")

if __name__ == "__main__":
    num_requests = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    for _ in range(num_requests):
        increment_counter()
        time.sleep(0.1)
