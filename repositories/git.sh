set-git-cookie(){
  local email=$1
  local token=$2
  eval 'set +o history' 2>/dev/null || setopt HIST_IGNORE_SPACE 2>/dev/null
  touch ~/.gitcookies
  chmod 0600 ~/.gitcookies
  git config --global http.cookiefile ~/.gitcookies
  tr , \\t <<\__END__ >>~/.gitcookies
source.developers.google.com,FALSE,/,TRUE,2147483647,o,git-${email}=1//0${token}
__END__
  eval 'set -o history' 2>/dev/null || unsetopt HIST_IGNORE_SPACE 2>/dev/null

}
$@
