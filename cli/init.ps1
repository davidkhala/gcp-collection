function DataProject {
    gcloud config set project gcp-data-davidkhala
}

function FreeProject {
    gcloud config set project freetier-only
}
function HK {
    gcloud config set compute/region asia-east1
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
