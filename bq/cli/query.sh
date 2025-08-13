set -e
translate4CLI() {
    local result=$(cat $1 | sed "s/'/\"/g" | sed '/^[[:blank:]]*--/d;s/--.*//')
    echo "'${result}'"
}
schema-of(){
    bq show --format=prettyjson $1 | jq '.schema.fields'
}

$@
