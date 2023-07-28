from googletrans import Translator

def split_text_into_blocks(text, block_size):
    # Teilt den Text in Blöcke von block_size Zeilen auf
    lines = text.strip().split('\n')
    blocks = [lines[i:i+block_size] for i in range(0, len(lines), block_size)]
    return blocks

def translate_text(text, src_lang='en', dest_lang='de'):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def main():
    input_file = 'HUNTB-613.vtt'
    output_file = 'HUNTB-613_de.vtt'
    block_size = 15

    with open(input_file, 'r', encoding='utf-8') as f:
        input_text = f.read()

    input_blocks = split_text_into_blocks(input_text, block_size)
    output_blocks = []

    for block in input_blocks:
        block_text = '\n'.join(block)
        translated_text = translate_text(block_text)
        output_blocks.append(translated_text)

    output_text = '\n\n'.join(output_blocks)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text)

if __name__ == "__main__":
    main()
