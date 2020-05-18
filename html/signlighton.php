<?php 

$command = escapeshellcmd('/home/pi/scripts/signlighton.py');
$output = shell_exec($command);
echo $output;

?>