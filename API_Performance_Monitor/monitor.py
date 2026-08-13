import time
import requests

from database import save_metric


def monitor_api(api_url):
    try:
        start_time = time.perf_counter()

        response = requests.get(api_url, timeout=10)

        end_time = time.perf_counter()

        response_time = round((end_time - start_time) * 1000, 2)

        status_code = response.status_code

        if response.ok:
            status = "SUCCESS"
        else:
            status = "ERROR"

        save_metric(
            api_url,
            response_time,
            status_code,
            status
        )

        return {
            "api_url": api_url,
            "response_time": response_time,
            "status_code": status_code,
            "status": status
        }

    except requests.exceptions.RequestException as error:

        response_time = 0
        status_code = 0
        status = "ERROR"

        save_metric(
            api_url,
            response_time,
            status_code,
            status
        )

        return {
            "api_url": api_url,
            "response_time": response_time,
            "status_code": status_code,
            "status": status,
            "error": str(error)
        }


if __name__ == "__main__":

    test_url = "https://jsonplaceholder.typicode.com/posts"

    result = monitor_api(test_url)

    print("\nAPI Performance Result")
    print("----------------------")
    print("API URL:", result["api_url"])
    print("Response Time:", result["response_time"], "ms")
    print("Status Code:", result["status_code"])
    print("Status:", result["status"])