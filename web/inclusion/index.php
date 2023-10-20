<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inclusion de ficheros</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h2>Inclusion de Ficheros</h2>
        <div class="card">
            <div class="card-body">
                <?php
                if (isset($_GET['file'])) {
                    $filename = $_GET['file'];
                    // Evitar la inclusión de archivos fuera del directorio actual por razones de seguridad
                    if (strpos($filename, '..') === false) {
                        $content = file_get_contents($filename);
                        echo nl2br(htmlspecialchars($content));
                    } else {
                        echo "Invalid file specified.";
                    }
                } else {
                    echo "Porfavor especifique un archivo usando el parámetro 'file'.";
                }
                ?>
            </div>
        </div>
    </div>
</body>
</html>
