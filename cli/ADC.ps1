# Application Default Credentials (ADC) used in calling Google APIs.
# - used for local dev environment
$ErrorActionPreference = "Stop"
function Path
{
    echo $env:APPDATA\gcloud\application_default_credentials.json
}
function Setup{
    # Interactive
    gcloud auth application-default login

    $project = gcloud config get-value project

    if ([string]::IsNullOrWhiteSpace($project)) {
        Set-Project $args[0]
    }
}

function Set-Project {
    param (
        [string]$projectId
    )

    gcloud auth application-default set-quota-project $projectId
    gcloud config set project $projectId
}

if ($args.Count -gt 0) {
    Invoke-Expression ($args -join " ")
}