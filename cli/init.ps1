function DataProject {
    gcloud config set project gcp-data-davidkhala
}

function BaseProject {
    gcloud config set project gcp-base-davidkhala
}
function HK {
    gcloud config set compute/region asia-east2
}
function Desktop {
    # Interactive
    gcloud init
}

function Server {
    # Interactive
    gcloud init --no-browser
}

if ($args.Count -gt 0)
{
    Invoke-Expression ($args -join " ")
}
