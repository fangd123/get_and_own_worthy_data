<?php

// 使用说明：
// composer install
// php index.php

require 'vendor/autoload.php';

use League\HTMLToMarkdown\HtmlConverter;

$converter = new HtmlConverter(array('strip_tags' => true));

function convert($converter, $filename)
{
    echo $filename."\n";
    $contents =file_get_contents($filename);
    $markdown = $converter->convert($contents);
    $path_parts  = pathinfo($filename);
    $new_file_name = $path_parts['dirname']."/".$path_parts['filename'].".md";
    echo $new_file_name."\n";

    file_put_contents($new_file_name,$markdown);
}

$folder = "夕小瑶的卖萌屋/html/"; // 读取的文件夹路径
if ($dir = opendir($folder)) {
    while (($file = readdir($dir)) !== false) {
        if (strstr($file,"html")) {
            convert($converter, $folder.$file);
        };
    }
    closedir($dir);
};


?>