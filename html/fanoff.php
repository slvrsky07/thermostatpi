<?php 

$command = escapeshellcmd('/home/pi/scripts/fanoff.py');
$output = shell_exec($command);
echo $output;

?>