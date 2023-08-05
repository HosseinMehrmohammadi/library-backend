from django.utils import timezone

def save_log(request, response):
    try:
        log_file = open('D:\\Programming\\Library_Logs.txt', 'a')
        time = str(timezone.now())
        api = request.get_full_path()
        method = request.method
        body = request.body.decode('ascii').replace('\n', '\n\t')
        log_file.write(
            '{\n'
            '\tid: ' + response['response_id'] + '\n' +
            '\ttime: ' + time + '\n' +
            '\tapi: ' + api + '\n' +
            '\tmethod: ' + method + '\n' +
            '\tbody: ' + body + '\n' +
            '\tmessage: ' + response['response_message'] + '\n'
        )
        if 'error' in response.keys():
            log_file.write(
                '\terror: ' + response['error'] + '\n'
            )
        log_file.write('}\n')
        log_file.close()
    
    except Exception as e:
        print(e)