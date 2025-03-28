import os

# Pasta onde estão os arquivos de notas
notes_dir = "docs"
output_file = "index.html"

# Obtém a lista de arquivos .md na pasta docs/
notes = [f for f in os.listdir(notes_dir) if f.endswith(".md")]

# Gera o HTML
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minhas Notas</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; text-align: center; background-color: #f4f4f4; }
        h1 { color: #333; }
        ul { list-style: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #007bff; font-size: 18px; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>📚 Minhas Notas</h1>
    <p>Selecione uma das notas abaixo para visualizar:</p>
    <ul>
"""

for note in notes:
    html_content += f'        <li><a href="{notes_dir}/{note}">{note}</a></li>\n'

html_content += """    </ul>
</body>
</html>
"""

# Salva o arquivo index.html
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Arquivo {output_file} gerado com sucesso!")
