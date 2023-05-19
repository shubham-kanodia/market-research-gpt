# Market Research AI

## Setup and Running

* Clone the GitHub repo

* Install python dependencies, it is recommended to use a python virtual env
    ```bash
    $ pip install -r requirements.txt
    ```

* Setup env variables
  * Get Organisation-Id and API keys from openai
  * Enter the values in `env.example` file
  * Rename the file to `.env`

* If you are running on a new idea, go to `config.json` and update the `idea` key. Also delete the contents of `data/` directory
* Information regarding each step is cached in `data/` directory. To run any step again, just delete the file corresponding to that step's data
* Run the program using the following command
    ```bash
    $ python main.py
    ```
* The results are published in `data/research.md` file
