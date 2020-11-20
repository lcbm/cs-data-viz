#!/usr/bin/env bash


remove_special_characters() {
    local DATA_DIR=$1

    echo -e "Removing special characters from data in ${DATA_DIR}..."
    cd "${DATA_DIR}" &&

    echo -e "Removing accents and other non ascii characters..."
    find . -type f -name '*' -exec iconv -f utf8 -t ascii//TRANSLIT {} -o {}_new \; &&

    echo -e "Replacing single quotes by spaces..."
    find . -name '*.csv_new' -exec sed -i "s/'/ /g" {} + &&

    return 0
}


main() {
    remove_special_characters "${1}" &&
    exit 0
}


main "${1}"
