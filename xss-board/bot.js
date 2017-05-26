// author: takeshix@adversec.com
var zombie = require("zombie");
var bot = new zombie();
bot.setCookie({name: 'PHPSESSID', domain: '192.168.40.132', value: 'mag1c_c00k1e'});
bot.visit("http://192.168.40.132:5004/index.php", {debug: true}, function(){
	bot.
		fill("user", "admin").
		fill("comment", "hilarious!").
		pressButton("Post it!", function(){})
});
