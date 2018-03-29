var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();
page.onResourceRequested = function(requestt){
	console.log('Request' + JSON.stringify(requestt, undefined, 4));
};
page.onResourceReceived = function(response) {
	console.log('Receive' + JSON.stringify(response, undefined, 4));
};
page.open(url)