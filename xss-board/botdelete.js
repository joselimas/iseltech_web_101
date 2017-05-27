// author: takeshix@adversec.com
var zombie = require("zombie");
var bot = new zombie();
bot.setCookie({name: 'PHPSESSID', domain: '95.85.49.66', value: 'mag1c_c00k1e'});
bot.visit("http://95.85.49.66:5004/delete.php", {debug: true}, function(){});
