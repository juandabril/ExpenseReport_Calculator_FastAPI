# FastAPI Calculator

This repository contains a Python-based calculator application developed using FastAPI. To get started with the project, follow these steps:

1. Ensure you have a Python compiler installed (version 3.11 was used for this project).

2. Install FastAPI and its dependencies by running the following command:
   ```
   pip install fastapi uvicorn
   ```

3. Install the Jinja2 template engine using the following command:
   ```
   pip install Jinja2
   ```

4. Install the python-multipart package with this command:
   ```
   pip install python-multipart
   ```

5. Run your project using one of the following commands:
   - With Uvicorn:
     ```
     uvicorn app:app --reload
     ```
   - Alternatively, with a custom port (e.g., 8500):
     ```
     uvicorn app:app --reload --port 8500
     ```
   - Or, using the Python module:
     ```
     python -m uvicorn app:app --reload
     ```

This will start the FastAPI calculator application and make it available for testing and usage. Remember to replace "app" with the appropriate module name if you've organized your code differently.
