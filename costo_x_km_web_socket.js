var WebSocket = require('ws');
var cookie = require('cookie');

var ws = new WebSocket(
    'http://localhost/auth',
    [],
    {
        'headers': {
            'Cookie': cookie.serialize('id', '496E66DD')
        }
    }
);
