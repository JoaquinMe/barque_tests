marker=$1

tar -zcf "$marker/12_results.tar.gz" "$marker/barque/12_results"
tar -zcf "$marker/99_logfiles.tar.gz" "$marker/barque/99_logfiles"
rm -rf "$marker/barque"
sum_results=$(sha1sum <"$marker"/12_results.tar.gz | awk '{print $1}')
sum_logfiles=$(sha1sum <"$marker"/99_logfiles.tar.gz | awk '{print $1}')

echo "{\"results_checksum\": \"$sum_results\", \"logfiles_checksum\": \"$sum_logfiles\"}"
