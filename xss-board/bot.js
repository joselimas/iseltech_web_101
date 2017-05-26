// author: takeshix@adversec.com
var zombie = require("zombie");
var bot = new zombie();
bot.setCookie('PHPSESSID','mag1c_c00k1e');
bot.visit("http://192.168.40.132:5004/index.php", {debug: true}, function(){
	bot.
		fill("user", "admin").
		fill("comment", "hilarious!3").
		pressButton("Post it!", function(){})
});
