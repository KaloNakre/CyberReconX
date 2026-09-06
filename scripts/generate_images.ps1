param(
  [string]$Prompt,
  [string]$Out = "out.png"
)

if (-not $Prompt) {
  Write-Host "Usage: .\generate_images.ps1 -Prompt 'your prompt' -Out out.png"
  exit 1
}

$body = @{ prompt = $Prompt; steps = 28; width = 1024; height = 576 } | ConvertTo-Json
$resp = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:7860/sdapi/v1/txt2img -ContentType 'application/json' -Body $body

if ($resp.images -and $resp.images.Count -gt 0) {
  $b64 = $resp.images[0]
  [System.IO.File]::WriteAllBytes($Out, [System.Convert]::FromBase64String($b64))
  Write-Host "Saved $Out"
} else {
  Write-Host "No image returned. Response saved to resp.json"
  $resp | ConvertTo-Json | Out-File resp.json
}
