<?php 

$command = escapeshellcmd('/home/pi/scripts/barlightoff.py');
$output = shell_exec($command);
echo $output;

?>