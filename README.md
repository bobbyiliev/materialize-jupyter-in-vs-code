# How to Show Graphs in VS Code with Matplotlib, Jupyter, Materialize, and Plotly

This is a simple example of how to show graphs in VS Code using Matplotlib, Jupyter, Materialize, and Plotly.

![](https://imgur.com/pRcpVhX.gif)

## Requirements

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/)
- [Materialize](https://materialize.com/)

## Install the Required Extensions in VS Code

- Install the [Jupyter extension in VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).
- Install the [Python extension in VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Create a Virtual Environment

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
    pip install psycopg2-binary matplotlib plotly pandas python-dotenv
    ```

## Create a `.env` File

Copy the `.env.example` file to a new file named `.env` and fill in the necessary information.

## Create Some Demo Data

Run the SQL statements in the `demo.sql` file to create the necessary table, view, and insert some data.

## Demo 1: Matplotlib Graph

This demo will show you how to create and display a graph using Matplotlib in VS Code.

### Run the Demo

1. Open the `demo_matplotlib.py` file and run the code.

2. Right-click on the code and select "Run in Interactive Window" -> "Run current file in Interactive Window".

3. VS Code will open a new tab with the graph:

   <img width="1837" alt="image" src="https://github.com/user-attachments/assets/215f008d-a4fc-488e-b6f2-b44d1fd20870">

4. To display your own graph, change the SQL query in the `demo_matplotlib.py` file to query your own data and the Matplotlib code to display the graph you want to show.

## Demo 2: Plotly with Pandas

This demo will show you how to create and display a graph using Plotly and Pandas in VS Code. Plotly provides interactive and visually appealing charts, which can be a great alternative to Matplotlib.

### Run the Demo

1. Open the `demo_plotly.py` file in VS Code.

2. Right-click on the code and select "Run in Interactive Window" -> "Run current file in Interactive Window".

3. VS Code will open a new tab or your web browser with the interactive graph.

4. To display your own graph, change the SQL query in the `demo_plotly.py` file to query your own data and the Plotly code to display the graph you want to show.
