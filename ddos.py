import threading
import requests

target_url = "http://exemple.com"  # Replace with a legitimate, authorized URL

def send_requests():
    while True:  # Infinite loop
        try:
            response = requests.get(target_url)
            print(f"Request sent: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

# Number of threads to use for parallel requests
num_threads = 10
threads = []

# Create and start threads
for i in range(num_threads):
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
