set -e

extract() {

    if [[ -z "${dataset}" ]]; then
        echo "Missing \$dataset"
        exit 128
    fi
    if [[ -z "${bucket}" ]]; then
        echo "Missing \$bucket"
        exit 128
    fi

    if [[ -z "${source_table}" ]]; then

        if [[ -z "${table}" ]]; then

            for word in $(bq ls --format=json $dataset | jq -r ".[].id"); do
                export source_table=$word
                extract
            done

            exit
        fi
        if [[ -n "${project_id}" ]]; then
            source_table=$project_id:$dataset.$table
        else
            source_table=$dataset.$table
        fi
    fi

    bq extract $source_table gs://$bucket/$source_table.csv

}

$@
