typeset TMP_FILE=$( mktemp )

touch "${TMP_FILE}"
cp -p tweets.json "${TMP_FILE}"
sed -e 's/$/,/' "${TMP_FILE}" > tweets.json
