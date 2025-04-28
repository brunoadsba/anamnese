from PIL import Image

def remove_white_background(input_path, output_path):
    """
    Remove o fundo branco de uma imagem PNG e salva com transparência.
    
    Args:
        input_path: Caminho para a imagem original
        output_path: Caminho para salvar a imagem com fundo transparente
    """
    img = Image.open(input_path)
    img = img.convert("RGBA")
    
    # Obtém os dados dos pixels
    datas = img.getdata()
    
    # Cria uma nova lista de dados
    new_data = []
    
    # Define o limiar de branco (quanto maior, mais cores serão consideradas "branco")
    white_threshold = 240
    
    # Para cada pixel, verifica se é branco (ou quase branco)
    for item in datas:
        # Se o pixel for branco (ou quase branco), torne-o transparente
        if item[0] >= white_threshold and item[1] >= white_threshold and item[2] >= white_threshold:
            new_data.append((255, 255, 255, 0))  # Transparente
        else:
            new_data.append(item)  # Mantém a cor original
    
    # Atualiza os dados da imagem
    img.putdata(new_data)
    
    # Salva a imagem com transparência
    img.save(output_path, "PNG")
    
    print(f"Imagem salva com sucesso em {output_path}")

if __name__ == "__main__":
    # Caminhos para os arquivos
    input_image = "image/Logo_PP.png"
    output_image = "image/Logo_PP_transparent.png"
    
    # Remove o fundo branco
    remove_white_background(input_image, output_image)
    
    print("Para usar a nova imagem, altere o src no arquivo form.html para 'image/Logo_PP_transparent.png'") 