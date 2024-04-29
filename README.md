# AirBnB Clone V2

This repository contains the second version of a simplified clone of AirBnB. It includes back-end services and scripts to manage a web static and dynamic content using Flask, a Python web framework, and MySQL for data management.

## Project Structure

Here's a brief overview of the top-level directory structure:

- `0-setup_web_static.sh`: Shell script for setting up web static.
- `1-pack_web_static.py`, `2-do_deploy_web_static.py`, `3-deploy_web_static.py`: Python scripts for packaging and deploying web static files.
- `100-clean_web_static.py`, `101-setup_web_static.pp`: Scripts for cleaning up old web static files and Puppet setup script, respectively.
- `0x1A-application_server`: Configuration files and scripts for the application server.
- `web_flask`: Flask application modules.
- `web_static`: HTML and CSS files for the web static part.
- `models`: Python classes and methods for data management.
- `tests`: Unit tests for application validation.
- `versions`: Archive of old versions of the web static files.
- `console.py`: Command line console for custom admin processes.
- `setup_mysql_dev.sql`, `setup_mysql_test.sql`: SQL scripts for setting up development and test MySQL databases.
- `test_params_create`: Scripts or configurations for testing parameters.
- `AUTHORS`: List of contributors to this project.

## Setup Instructions

To set up the project on your local environment, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/AirBnB_clone_v2.git
   cd AirBnB_clone_v2
