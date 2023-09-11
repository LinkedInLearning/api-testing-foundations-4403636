import requests

for i in range(10):
    response = requests.post(
        "http://127.0.0.1:8000/tasks",
        json={
            "description": f"todo_{i}",
            "status": "Draft",
            "created_by": "anonymous",
        },
    )
