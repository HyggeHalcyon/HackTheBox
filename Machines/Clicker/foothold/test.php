<?php

# Trying SQLi but it's just a rabbit hole
$player = "bob";
$args["clicks"] = "1',role='Admin";
$args["level"] = 100;

$setStr = "";
foreach ($args as $key => $value) {
        $setStr .= $key . "='" . $value . "',";
}
$setStr = rtrim($setStr, ",");
$stmt = "UPDATE players SET" . $setStr . "WHERE username =" . $player . "\n";

echo $stmt;