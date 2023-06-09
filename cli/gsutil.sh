countFiles() {
  gsutil du gs://$1/* | wc -l
  
}
binaryInstall(){
  # Download gsutil
  curl https://storage.googleapis.com/pub/gsutil.tar.gz > gsutil.tar.gz
  tar xfz gsutil.tar.gz -C $HOME 
  # Add gsutil to PATH environment variable
  echo 'export PATH="$HOME/gsutil: ${PATH}"' >> $HOME/.bashrc
  # Run below command to test if gsutil is available
  if ! ./gsutil --version; then
      rm -rf ./gsutil.tar.gz
      exit 1
  fi
}

$@
