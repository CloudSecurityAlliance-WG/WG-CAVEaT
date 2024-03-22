$word_app = New-Object -ComObject Word.Application
$word_app.Visible = $False

# Define the folder where your Word documents are located
$source_folder = "C:\GitHub\WG-CAVEaT-data\CAVEaT-files\Docs"
# Define the folder where you want to save the PDFs
$target_folder = "C:\GitHub\WG-CAVEaT-data\CAVEaT-files\PDFs"

# Ensure the target directory exists
if (-not (Test-Path -Path $target_folder)) {
    New-Item -ItemType Directory -Path $target_folder
}

Get-ChildItem -Path $source_folder -Filter *.docx | ForEach-Object {
    $document = $word_app.Documents.Open($_.FullName)
    $pdf_filename = "$target_folder\" + $_.BaseName + ".pdf"
    $document.SaveAs([ref] $pdf_filename, [ref] 17) # 17 is the wdFormatPDF enum value
    $document.Close()
}

$word_app.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word_app) | Out-Null
