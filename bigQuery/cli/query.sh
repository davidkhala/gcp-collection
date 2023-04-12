set -e
translate4CLI() {
    local result=$(cat $1 | sed "s/'/\"/g" | sed '/^[[:blank:]]*--/d;s/--.*//')
    echo "'${result}'"
}

$@
