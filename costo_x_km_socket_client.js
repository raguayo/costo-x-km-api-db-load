import { Socket } from 'socket.io-client';

HTTP.post('http://localhost:8082/api/session', {

    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    content: "email=SOME_EMAIL&password=SOME_PASSWORD"

}, function(response, some){

    console.log(response);

    var socket = new Socket('ws://localhost:8082/api/socket');

    console.log(socket);
}
