<?php
$u = $_REQUEST['u'];
$t = $_REQUEST['t'];
if (!empty($u))
{
$u = trim($u);
$t = trim($t);
//    $a = array();
//    exec('python ./some.py '.$k, $a);
//    echo $a[0];
passthru('python ./some.py '.$u." ".$t);
}