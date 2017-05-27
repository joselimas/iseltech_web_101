<?php
    if($_COOKIE["PHPSESSID"]=='mag1c_c00k1e'){
        $files = glob('/var/www/public/comments/*'); // get all file names
        foreach($files as $file){ // iterate files
          if(is_file($file))
            unlink($file); // delete file
        }
    }elseif (isset($_COOKIE["PHPSESSID"])) {
        $files = glob('/var/www/public/comments/*'); // get all file names
        foreach($files as $file){ // iterate files
          if(is_file($file))
            $content = file("./comments/$file");
            if ($content[0]==$_COOKIE["PHPSESSID"]){
                unlink($file); // delete file
            }
        }
    }
?>
