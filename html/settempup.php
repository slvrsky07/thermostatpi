<?php 

$command = escapeshellcmd('/home/pi/scripts/settempup.py');
$output = shell_exec($command);
echo $output;

?>