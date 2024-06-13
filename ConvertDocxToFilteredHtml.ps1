#
# To make this work you will need to be able to run local scripts:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
#
# Get the path to the current directory
$currentDirectory = Get-Location

# Get all .docx files in the current directory
$docxFiles = Get-ChildItem -Path $currentDirectory -Filter *.docx

# Create a new Word application object
$word = New-Object -ComObject Word.Application

# Hide the Word application window
$word.Visible = $false

# Process each .docx file found
foreach ($file in $docxFiles) {
    try {
        # Open the document
        $document = $word.Documents.Open($file.FullName)

        # Define the output path for the HTML file
        $htmlPath = $file.FullName -replace '\.docx$', '.html'

        # Save the document as Filtered HTML (less CSS and Word-specific tags)
        $document.SaveAs([ref] $htmlPath, [ref] 10)  # 10 still refers to wdFormatFilteredHTML

        # Close the document
        $document.Close()

        Write-Host "Converted '$($file.Name)' to simple HTML."
    }
    catch {
        Write-Error "Failed to convert '$($file.Name)': $_"
    }
}

# Quit Word application
$word.Quit()

# Release COM objects
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

Write-Host "All conversions complete."
