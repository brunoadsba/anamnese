from PIL import Image, ImageDraw, ImageOps

def add_white_backdrop(input_path, output_path, scale_factor=1.5):
    """
    Adiciona um fundo circular branco à logo para melhorar visibilidade em fundos escuros.
    
    Args:
        input_path: Caminho para a imagem original
        output_path: Caminho para salvar a versão com fundo
        scale_factor: Fator de escala para aumentar o tamanho da imagem
    """
    # Abre a imagem original
    original = Image.open(input_path).convert("RGBA")
    
    # Calcula as novas dimensões
    width, height = original.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    
    # Redimensiona a imagem original
    original_resized = original.resize((new_width, new_height), Image.LANCZOS)
    
    # Cria uma nova imagem com fundo transparente
    result = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
    
    # Cria um desenho para adicionar o círculo branco
    draw = ImageDraw.Draw(result)
    
    # Calcula o raio do círculo (um pouco maior que a imagem)
    center_x, center_y = new_width // 2, new_height // 2
    radius = max(new_width, new_height) // 2
    
    # Desenha o círculo branco com um pouco de transparência
    draw.ellipse(
        (center_x - radius, center_y - radius, center_x + radius, center_y + radius),
        fill=(255, 255, 255, 220)  # Aumenta a opacidade
    )
    
    # Combina o círculo branco com a imagem original
    result.alpha_composite(original_resized)
    
    # Salva a imagem
    result.save(output_path, "PNG")
    
    print(f"Logo com fundo branco salva com sucesso em {output_path}")

if __name__ == "__main__":
    # Caminhos para os arquivos
    input_image = "image/Logo_PP.png"
    output_image = "image/Logo_PP_with_bg.png"
    
    # Adiciona fundo branco à logo com aumento de tamanho
    add_white_backdrop(input_image, output_image, scale_factor=1.5)
    
    print("Você pode usar esta imagem para fundos escuros alterando o src no HTML para 'image/Logo_PP_with_bg.png'") 