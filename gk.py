from greeter import output
import wolframalpha


def wolform(question):
    app_id = 'WVUXYH-QA4ULTKQ2U'
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        # print(question)
        # Includes only text from the response
        answer = next(res.results).text
        
        ## STopIteration exception daal bc

        # Stores the response from 
        # wolf ram alpha
        
        output(answer)
    except Exception as e:
        pass