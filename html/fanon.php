<?php 

$command = escapeshellcmd('/home/pi/scripts/fanon.py');
$output = shell_exec($command);
echo $output;

?>