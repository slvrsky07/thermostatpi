<?php 

$command = escapeshellcmd('/home/pi/scripts/settempdown.py');
$output = shell_exec($command);
echo $output;

?>