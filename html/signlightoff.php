<?php 

$command = escapeshellcmd('/home/pi/scripts/signlightoff.py');
$output = shell_exec($command);
echo $output;

?>