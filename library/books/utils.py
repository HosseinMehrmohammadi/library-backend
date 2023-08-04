def save_log(request, response):
    try:
        log_file = open('D:\\Programming\\Library_Logs.txt', 'a')
        api = request.get_full_path()
        method = request.method
        body = request.body.decode('ascii')
        log_file.write(
            '{\n'
            '\tid: ' + response['response_id'] + '\n' +
            '\tapi: ' + api + '\n' +
            '\tmethod: ' + method + '\n' +
            '\tbody: ' + body + '\n' +
            '\tmessage: ' + response['response_message'] + '\n' +
            '}\n'
        )
        log_file.close()
    
    except Exception as e:
        print(e)