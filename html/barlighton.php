<?php 

$command = escapeshellcmd('/home/pi/scripts/barlighton.py');
$output = shell_exec($command);
echo $output;

?>