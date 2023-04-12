translate4CLI() {
    echo $1 | sed "s/'/\"/g" | sed '/^[[:blank:]]*--/d;s/--.*//'
}

$@
