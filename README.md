# My ZootopiaAPI 🦊

A Python web application that fetches animal data from the API Ninjas Animals API and generates beautiful HTML pages with animal information. Users can search for animals, filter by skin type, and get detailed information displayed in an attractive card layout.

## 🌟 Features

* **Animal Search**: Search for any animal using the API Ninjas Animals API
* **Skin Type Filtering**: Filter animals by different skin types (Fur, Scales, Hair, etc.)
* **Beautiful HTML Output**: Generates responsive HTML pages with CSS styling
* **Error Handling**: User-friendly error pages for non-existent animals
* **Modular Architecture**: Separated data fetching and web generation logic
* **Environment Variables**: Secure API key management using .env files

## 📋 Prerequisites

* Python 3.7 or higher
* pip (Python package installer)
* API Ninjas account and API key ([Get one here](https://api.api-ninjas.com/))

## 🚀 Installation

1. **Clone the repository**

``` bash
git clone https://github.com/Oleguzik/My-ZootopiaAPI.git
cd My-ZootopiaAPI
```

2. **Create a virtual environment**

``` bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

3. **Install dependencies**

``` bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory and add your API key:

```
API_KEY=your_api_ninjas_key_here
```

## 🎮 Usage

Run the application:

``` bash
python animals_web_generator.py
```

Follow the interactive prompts:

1. Enter an animal name (e.g., "fox", "cat", "lion")
2. Choose a skin type from the available options
3. The application will generate `animals.html` with the results

Open `animals.html` in your web browser to view the generated animal cards.

## 📁 Project Structure

```

├── animals_web_generator.py    # Main application file
├── data_fetcher.py            # API communication module
├── animals_template.html      # HTML template for output
├── styles.less               # LESS stylesheet source
├── styles.css               # Compiled CSS (auto-generated)
├── animals.html             # Generated HTML output (auto-generated)
├── requirements.txt         # Python dependencies
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🛠️ Dependencies

### Python Dependencies
* **requests**: For making HTTP API calls
* **python-dotenv**: For loading environment variables from .env file
* **lesscpy**: Python LESS compiler for CSS preprocessing

### Node.js Dependencies (Alternative)
If you prefer using Node.js for LESS compilation:
```bash
npm install
npm run build-css
```

## 🎨 Styling

The project uses LESS for CSS preprocessing with variables and mixins. 

### Compiling LESS to CSS

**Option 1: Python LESS Compiler (lesscpy)**
```bash
lesscpy styles.less styles.css
```

**Option 2: Node.js LESS Compiler**
```bash
npm run build-css
# or for watching changes:
npm run watch-css
```

## 🔧 API Integration

This project uses the [API Ninjas Animals API](https://api.api-ninjas.com/v1/animals) to fetch animal data. You'll need to:

1. Sign up for a free account at [API Ninjas](https://api.api-ninjas.com/)
2. Get your API key from the dashboard
3. Add it to your `.env` file

## 📊 Example Output

The application generates HTML cards with animal information including:

* Animal name and type
* Diet information
* Location data
* Taxonomic classification
* Physical characteristics

## 🚨 Error Handling

The application includes user-friendly error handling for:

* Non-existent animals (displays a helpful error page)
* API connection issues
* Missing configuration files

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**

``` bash
git checkout -b feature/amazing-feature
```

3. **Make your changes**
4. **Commit your changes**

``` bash
git commit -m 'Add some amazing feature'
```

5. **Push to the branch**

``` bash
git push origin feature/amazing-feature
```

6. **Open a Pull Request**

### Development Guidelines

* Follow PEP 8 style guidelines
* Add comments for complex logic
* Test your changes before submitting
* Update documentation if needed

## 📝 License

This project is open source and available under the [MIT License](LICENSE).


## 🙏 Acknowledgments

* [API Ninjas](https://api.api-ninjas.com/) for providing the animals API
* The Python community for excellent libraries and tools

## 📞 Support

If you have any questions or run into issues, please [open an issue](https://github.com/Oleguzik/issues) on GitHub.

- - -

**Happy animal searching! 🐾**