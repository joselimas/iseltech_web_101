var page = require('webpage').create();
var host = "95.85.49.66";
var url = "http://"+host+":5004/index.php";
var timeout = 2000;
phantom.addCookie({
    'name': 'PHPSESSID',
    'value': 'mag1c_c00k1e',
    'domain': host,
    'path': '/',
    'httponly': false
});
page.settings.loadImages=true;
page.onNavigationRequested = function(url, type, willNavigate, main) {
    console.log("[URL] URL="+url);
};
page.settings.resourceTimeout = timeout;
page.onResourceTimeout = function(e) {
    setTimeout(function(){
        console.log("[INFO] Timeout")
        phantom.exit();
    }, 1);
};

page.onLoadFinished = function() {
      console.log("page load finished");
      phantom.exit();
    };

page.open(url, function(status) {
    page.evaluate(function(){

    });
});
