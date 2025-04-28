from PIL import Image, ImageOps, ImageFilter

def create_light_version(input_path, output_path):
    """
    Cria uma versão da logo com contorno branco para uso em fundos escuros.
    
    Args:
        input_path: Caminho para a imagem original
        output_path: Caminho para salvar a versão modificada
    """
    # Abre a imagem original
    original = Image.open(input_path).convert("RGBA")
    
    # Cria uma cópia para o efeito de brilho
    glow = original.copy()
    
    # Cria uma máscara branca apenas com as partes não transparentes
    mask = Image.new("RGBA", original.size, (0, 0, 0, 0))
    for y in range(original.height):
        for x in range(original.width):
            pixel = original.getpixel((x, y))
            if pixel[3] > 50:  # Se não for transparente
                mask.putpixel((x, y), (255, 255, 255, pixel[3]))
    
    # Aplica um desfoque na máscara para criar o efeito de brilho
    mask = mask.filter(ImageFilter.GaussianBlur(radius=3))
    
    # Combina a máscara com a imagem original
    result = Image.alpha_composite(mask, original)
    
    # Aumenta o brilho da imagem final
    enhancer = ImageOps.autocontrast(result)
    
    # Salva a imagem
    enhancer.save(output_path, "PNG")
    
    print(f"Versão da logo com brilho salva com sucesso em {output_path}")

if __name__ == "__main__":
    # Caminhos para os arquivos
    input_image = "image/Logo_PP.png"
    output_image = "image/Logo_PP_light.png"
    
    # Cria versão melhorada da logo
    create_light_version(input_image, output_image)
    
    print("Agora atualize o HTML para usar a imagem corretamente:") 