import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="testfunc")
def testfunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="helloworld")
def helloworld(req: func.HttpRequest) -> func.HttpResponse:
    msg = req.params.get('message')
    if not msg:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
    elif msg.lower() == 'greetings':
        return func.HttpResponse("Hello World")
    else:
        return func.HttpResponse(f"Hello {msg}")