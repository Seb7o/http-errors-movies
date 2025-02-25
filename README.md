# Funny HTTP Error Pages Generator

A lightweight Python tool to generate humorous and movie-themed HTTP error pages for reverse proxies (and similar use cases). Customize the generated pages by editing a YAML configuration file to suit your needs.

---

## Overview

![Generated HTTP 404 Error Page Example](./screenshots/404.png "Error 404")

This project uses a combination of **Jinja2** and **PyYAML** to render HTML error pages based on customizable settings. The provided template is designed with Tailwind CSS, making it visually appealing and easily adaptable for movie-related or other themed error messages.

---

## Features

- **Customizable Errors:** Define multiple error pages (e.g., 404, 500) with unique titles, quotes, descriptions, and images.
- **Movie-Themed Customization:** Out-of-the-box settings focus on movie-related content, but the setup is flexible enough to cater to any theme.
- **Simple Configuration:** Use the `settings.yml` file to configure error details, such as background images, logos, and more.
- **Easy Integration:** Generate standalone HTML files that can be used with reverse proxies or integrated into your web server setup.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Configure Your Error Settings:**

   Edit the `settings.yml` file to customize error messages. For example, you can update the title, quote, description, images, and movie title. An example configuration:

   ```yaml
   logo: https://example.com/logo.svg
   back_button_text: Back
   errors:
     404:
       - title: Erreur 404 Not Found
         quote: a funy quote
         description: a funny description
         background_image: https://example.com/errors/404/background.jpg
         image: https://example.com/errors/404/image.jpg
         image_alt: If image is unloadable or for audio description
         movie_title: Obviously the movie title
   ```

2. **Run the Generator Script:**

   By default, the script reads from `settings.yml` and uses the `base.html` template to generate error pages:

   ```bash
   python generate.py
   ```

   Generated HTML files will be placed in the `error_pages` directory. You can also specify a different settings file or specific error codes as command-line arguments:

   ```bash
   python generate.py custom_settings.yml 404 500
   ```

3. **Deploy the Generated Pages:**

   Use the generated HTML files as custom error pages on your web server or reverse proxy configuration.

---

## Customization

- **Template Customization:**  
  Modify `base.html` to change the layout or add new elements. The file uses Jinja2 templating, so you can insert or update placeholders as needed.

- **Error Settings:**  
  Update the `settings.yml` file to change error codes, add multiple variations per error code, or adjust visual elements like logos and backgrounds.

- **Styling:**  
  The project includes Tailwind CSS via CDN in the template. You can modify the inline styles or replace Tailwind with your preferred CSS framework.

---


## Screenshots

![Generated HTTP 400 Error Page Example](./screenshots/400.png "Error 400")
![Generated HTTP 401 Error Page Example](./screenshots/401.png "Error 401")
![Generated HTTP 403 Error Page Example](./screenshots/403.png "Error 403")
![Generated HTTP 404 Error Page Example](./screenshots/404.png "Error 404")
![Generated HTTP 500 Error Page Example](./screenshots/500.png "Error 500")

---

## Contributing

Feel free to fork the repository and submit pull requests for new features, bug fixes, or improvements. All contributions are welcome!

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact

For any questions or suggestions, please open an issue on the GitHub repository.

Enjoy creating your own funny and engaging error pages!