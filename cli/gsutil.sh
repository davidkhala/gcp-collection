countFiles() {
  gsutil du gs://$1/* | wc -l
  
}
$@
