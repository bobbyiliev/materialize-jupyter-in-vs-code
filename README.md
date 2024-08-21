# How to show graph in VS Code with Matplotlib, Jupyter and Materialize

This is a simple example of how to show a graph in VS Code with Matplotlib, Jupyter and Materialize.

![](https://imgur.com/pRcpVhX.gif)

## Requirements

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/)
- [Materialize](https://materialize.com/)

## Install the required extension in VS Code

- Install the [Jupyter extension in VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).
- Install the [Python extension in VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Create a virtual environment

- Create a new virtual environment:

    ```
    python -m venv .venv
    ```

- Activate the virtual environment:

    - On Windows:

        ```
        .venv\Scripts\Activate.ps1
        ```

    - On macOS and Linux:

        ```
        source .venv/bin/activate
        ```

- Install the necessary packages:

    ```
    pip install psycopg2-binary matplotlib python-dotenv
    ```

## Create a `.env` file

Copy the `.env.example` file to a new file named `.env` and fill in the necessary information.

## Create some demo data

Run the SQL statements in the `demo.sql` file to create the necessary table, view and insert some data.

## Run the demo

Open the `demo.py` file and run the code.

Right-click on the code and select "Run in interactive window" -> "Run current file in Interactive Window".

VS Code will open a new tab with the graph:

<img width="1837" alt="image" src="https://github.com/user-attachments/assets/215f008d-a4fc-488e-b6f2-b44d1fd20870">

To display your own graph, change the SQL query in the `demo.py` file to query your own data and the Matplotlib code to display the graph you want to show.
