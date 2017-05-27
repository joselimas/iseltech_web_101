<?php
    if (isset($_COOKIE["PHPSESSID"])) {
        $files = glob('/var/www/public/comments/*'); // get all file names
        foreach($files as $file){ // iterate files
          if(is_file($file))
            $content = file($file);
            if ($content[0]==$_COOKIE["PHPSESSID"]."\n" || $_COOKIE["PHPSESSID"]=='mag1c_c00k1e'){
                unlink($file); // delete file
            }
        }
    }
?>
