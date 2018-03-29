phantomjs常用模块和方法

1.phantom模块

{Boolean}addCookie(Object) 添加一个Cookie信息到CookieJar中  
phantom.addCookie({
	'name': 'Added-Cookie-Name',
	'value': 'Added-Cookie-Value',
	'domain': '.google.com'
});

{void} clearCookie() 删除CookieJar中所有的Cookie信息
phantom.clearCookies();

{Boolean}deleteCookie(cookieName) 删除指定名称的Cookie信息
phantom.deleteCookie('Added-Cookie-Name');

{void}phantom.exit(returnValue) 以指定的返回值退出程序
if (somethingIsWrong) {
	phantom.exit(1);
} else {
	phantom.exit(0);
}

{boolean}phantom.injectJs(filename) 注入外部的js文件
var wasSuccessful = phantom.injectJs('lib/utils.js')


2.webpage模块
includeJs、open两个普通方法，onInitialized、onLoadFinished两个回调方法

includeJs方法原型为includeJs(url, callback){void},
功能是包含从指定的URL获取远程javaScript脚本并执行回调
var webPage = require('webpage');
var page = webPage.create();
page.includeJs(
	// Include the https version, you can change this to http if you like
	'https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js',
	function(){
	(page.evaluate(function(){
	//jQuery is loaded, now manipulate the DOM
	var $loginForm = $('form# login');
	$loginForm.find('input[name="username"]').value('phantomjs');
	$loginForm.find('input[name="password"]').value('c45p3r')
	}))
}
);

open方法比较复杂，有4种函数重载方式，open(url, callback){void}、open(url, method, callback){void}、 open(url, method, data, callback){void}、open(url, settings, callback){void}.
open(url,method,data,callback)中url为链接，method为GET或POST请求，data为附加的数据，callback为回调函数
var page = require('webpage').create();
var postBody = 'user=username&password=password';
page.open('http://www.google.com/', 'POST', postBody, function(status) {
	console.log('Status:' + status)
	//Do other things here...
});

open(url,settings,callback)中url为链接，setting为对请求头和内容的设置，callback为回调函数
var page = require('webpage').create();
var settings = {
	operation: "POST",
	encoding: "utf8",
	headers: {
	"Content-Type": "application/json"
},
data: JSON.stringify({
	some: "data",
	another: ["custom", "data"]
})
};

page.open('http://your.custom.api', settings, function(status){
	console.log('Status:' + status);
	//Do other things here...
});

onInitialized是回调方法在webpage对象被创建之后，url被加载之前被调用，主要是用来操作一些全局变量

var page = require('webpage').create();
page.onInitialized = function() {
	page.evaluate(function) {
	document.addEventListener('DOMContentLoaded', function(){
		console.log('DOM content has loaded.');
	}, false);
});
};

onLoadFinished是回调方法，在页面加载完成之后调用，方法还有一个参数status。如果加载成功status为success，否则诶fail。webpage中open方法就是用这个方法作为回调函数

var page = require('webpage').create()
page.onLoadFinished = function(status) {
	console.log('Status: ' + status)
	//Do other things here...
}


3.system模块
system模块只有属性，没有方法
args 从命令行输入的参数，是一个字符串列表
var system = require('system')';
var args = system.args;
if (args.length > 1)
	args.forEach(function(arg, i) {
		console.log(i + ':' + arg);
	})

env 系统变量，是一个键值对列表
var system = require('system')';
var env = system.env;
Object.keys(env).forEach(function(key) {
	console.log(key + '=' + env[key]);
});

os操作系统的信息
var system = require('system')';
var os = system.os;
console.log(os.architecture);
console.log(os.name);
console.log(os.version);

pid当前执行PhantonJS的进程号
var system = require('system')';
var pid = system.pid;
console.log(pid);

platform平台名称，总是PhantomJS
var system = require('system');
console.log(system.platform);//'phantomjs'

4.fs模块，全程File System主要对文件系统进行操作
touch创建一个空文件
var fs = require('fs');
var path = 'test.txt';
fs.touch(path);
phantom.exit();

exists判断文件是否存在
var fs = require('fs');
var path = 'test.txt';
if(fs.exists(path))
	console.log(exists);
else
	console.log(no exists);
phantom.exit();

read读文件
var fs = require('fs');
var content = fs.read('file.txt');
console.log(content);
phantom.exit();

write写文件
var fs = require('fs');
var path = 'output.txt'
var content = 'Hello World!';
fs.write(path, content, 'w');
phantom.exit();