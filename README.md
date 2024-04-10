# 🩸Moroccan Blood Donating Centers API

# **ℹ️ Project Overview**

The Moroccan Blood Donating Centers API is a Flask-based API that provides information about blood donation centers in Morocco. The API organizes the data by the 12 regions of Morocco, making it easy to access information specific to each region.

# **👨‍💻 Technologies**

- Python: The programming language used to develop the API.
    - Flask: A lightweight web framework for Python used to create the API endpoints and handle HTTP requests.
    - pymongo: A Python package that provides tools for interacting with MongoDB, a NoSQL database used to store the blood donation center data.
    - python-dotenv: A Python package used to load environment variables from a .env file, allowing secure configuration of the API.
- MongoDB: A NoSQL database used to store the blood donation center data. MongoDB's flexibility and scalability make it a suitable choice for managing the API's data.

# 🕸️ API Consumption

To consume the Moroccan Blood Donation API and retrieve the data, follow the instructions below:

- Make a **`GET`** request to the following URI to retrieve the full data:
    
    ```jsx
    https://sifeddine.pythonanywhere.com/centers
    ```
    
- To retrieve data for a specific blood donating centers of a region using its ID, append the ID to the URI mentioned above using a **`GET`** request to the modified URI. For example, to retrieve data for donationg centers of the region with ID 1, the URI would be:
    
    ```jsx
    https://sifeddine.pythonanywhere.com/centers/1
    ```
    
    Replace **`1`** with the desired region ID as following:
    
    | Region ID | Region Name | Region Name (Arabic) |
    | --- | --- | --- |
    | 1 | Tangier-Tetouan-Al Hoceïma | جهة طنجة تطوان الحسيمة |
    | 2 | Oriental Region | جهة الشرق |
    | 3 | Fez-Meknes | جهة فاس مكناس |
    | 4 | Rabat-Salé-Kenitra | جهة الرباط سلا القنيطرة |
    | 5 | Beni Mellal-Khenifra | جهة بني ملال خنيفرة |
    | 6 | Casablanca-Settat | جهة الدار البيضاء سطات |
    | 7 | Marrakech-Safi | جهة مراكش اسفي |
    | 8 | Drâa-Tafilalet | جهة درعة تافيلالت |
    | 9 | Souss-Massa | جهة سوس ماسة |
    | 10 | Guelmim-Oued Noun | جهة كلميم واد نون |
    | 11 | Laâyoune-Sakia El Hamra | جهة العيون الساقية الحمراء |
    | 12 | Dakhla-Oued Ed-Dahab | جهة الداخلة وادي الذهب |

Additionally, consider encoding and displaying Arabic text appropriately to ensure proper rendering of the data.