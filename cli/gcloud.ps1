function Install {
    param(
        [ValidateSet("User", "Machine")]
        [string]$Scope = "User"
    )

    $installer = "$env:Temp\GoogleCloudSDKInstaller.exe"
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", $installer)

    $scopeArg = if ($Scope -eq "Machine") { "/allusers" } else { "/currentuser" }
    Start-Process $installer -ArgumentList "/S /noreporting $scopeArg" -Wait

    Remove-Item $installer -Force
}

function Uninstall {
    param(
        [ValidateSet("User", "Machine")]
        [string]$Scope = "User"
    )

    $uninstallDir = if ($Scope -eq "Machine") {
        "${env:ProgramFiles(x86)}\Google\Cloud SDK"
    } else {
        "$env:LOCALAPPDATA\Google\Cloud SDK"
    }
    $uninstaller = "$uninstallDir\uninstaller.exe"

    if (-not (Test-Path $uninstaller)) {
        Write-Error "Uninstaller not found: $uninstaller"
        return
    }
    Start-Process $uninstaller -ArgumentList "/S" -Wait
}

if ($args.Count -gt 0)
{
    Invoke-Expression ($args -join " ")
}