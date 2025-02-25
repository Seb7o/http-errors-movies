import os
import sys
import yaml
from jinja2 import Template

DEFAULT_SETTINGS_FILE = 'settings.yml'
DEFAULT_TEMPLATE_FILE = 'base.html'
DEFAULT_OUTPUT_DIR = 'error_pages'

def load_settings(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def load_template(template_file):
    with open(template_file, 'r') as file:
        return Template(file.read())

def generate_html_pages(settings, codes_to_generate=None):
    template = load_template(DEFAULT_TEMPLATE_FILE)
    output_dir = DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)

    codes = codes_to_generate if codes_to_generate else settings.keys()
    
    for code in codes:
        if code in settings['errors']:
            pages = settings['errors'][code]
            for idx, data in enumerate(pages):
                rendered_html = template.render(
                    title=data.get('title', f'Error {code}'),
                    background_image=data.get('background_image', ''),
                    logo=data.get('logo', settings.get('logo', '')),
                    image=data.get('image', ''),
                    image_alt=data.get('image_alt', ''),
                    quote=data.get('quote', ''),
                    description=data.get('description', ''),
                    movie_title=data.get('movie_title', ''),
                    movie_url=data.get('movie_url', ''),
                    back_button_text=settings.get('back_button_text', 'Go back')
                )
                output_file = os.path.join(output_dir, f"{code}-{idx}.html" if idx else f"{code}.html")
                with open(output_file, "w") as file:
                    file.write(rendered_html)
                print(f"Page d'erreur {code} générée : {output_file}")
        else:
            print(f"Code d'erreur {code} non trouvé dans les paramètres.")

def main():
    settings_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SETTINGS_FILE
    settings = load_settings(settings_file)
    codes_to_generate = sys.argv[2:] if len(sys.argv) > 2 else settings['errors'].keys()

    generate_html_pages(settings, codes_to_generate)

if __name__ == "__main__":
    main()
