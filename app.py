#pip install fastapi uvicorn
from fastapi import FastAPI, Form, Request # conda update typing-extensions
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

expenses = []
templates = Jinja2Templates(directory="templates") #pip install Jinja2

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "expenses": expenses})

@app.post("/add_expense", response_class=HTMLResponse) #pip install python-multipart
async def add_expense(request: Request, payer: str = Form(...), description: str = Form(...), amount: float = Form(...)):
    if payer and description and amount:
        expense = {'payer': payer, 'description': description, 'amount': amount}
        expenses.append(expense)

        # Aquí puedes agregar la lógica para calcular y mostrar las deudas individuales

    return templates.TemplateResponse("index.html", {"request": request, "expenses": expenses})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
