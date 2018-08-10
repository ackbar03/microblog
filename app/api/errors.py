from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    '''
    ###Michael: from site:  The jsonify() function returns a Flask Response object with a 
    default status code of 200, so after I create the response, I set 
    the status code to the correct one for the error.
    '''
    return response


def bad_request(message):
    return error_response(400, message)

###Michael: note this error page doesn't really cover all, a lot will still respond according to the global
### error handlers. We then reroute it from there (app/errors). Implementation quite straight forward, just check
### preference and then if else.