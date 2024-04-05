
# Json Base64 Encode File Upload Project

This Django project provides a REST API that accepts JSON payloads containing Base64-encoded files, specifically designed for ease of integration with various frontend technologies. It simplifies the process of file upload by allowing clients to send files encoded as Base64 strings within a JSON object, avoiding the complexity of multipart/form-data handling.
## Features

- File upload through Base64 encoding within JSON.
- Django REST Framework for efficient API design.
- Cross-Origin Resource Sharing (CORS) enabled.

##  Requirements
- Django==4.1.7
- django-cors-headers==3.14.0
- djangorestframework==3.14.0
- drf-extra-fields==3.7.0
- pillow==10.3.0
# Setting Up
###  1. Clone Repository

```bash
git  clone https://github.com/Om-17/Json-Base64-Encode-File-Upload-Project.git
```
###  2. Environment Setup

   Ensure Python 3.8 or newer is installed. It's recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Requirements
Install the required packages using pip.
```bash 
pip install -r requirements.txt

```

### Running the Server

Run the Django development server.
```bash 
python manage.py runserver

```


## API Reference

#### To upload a file

```http
  POST /api/files
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `file`      | `base64` | **Base64 encode**   |
| `image`      | `base64` | **Base64 encode**   |



## API Request
To upload a file, send a POST request to the API endpoint with a JSON payload containing the Base64-encoded file. The expected format is as follows:

```bash 
{
  "file": "data:image/jpeg,name:demo.jpg;base64,<base64code>"
} 
```
## Badges


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

