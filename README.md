# Hypothesis Generation Project

## Description

This project implements a Language Learning Model (LLM) that simulates a material scientist with deep knowledge of organic materials and molecular interactions. The LLM is designed to analyze functional groups, their interactions, and propose new hypotheses based on given data.

## Streamlit App Frontend

This project includes a Streamlit app as the frontend interface. Streamlit provides an easy-to-use framework for creating web applications with Python.

run the app 
```
streamlit run app.py
```

## Installation

To install this project, follow these steps:

1. Ensure you have Python 3.11 installed on your system.
2. Install Poetry if you haven't already. You can find installation instructions at [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation).
3. Clone this repository to your local machine:
   ```
   git clone [your-repository-url]
   cd [your-project-directory]
   ```
4. Install the project dependencies using Poetry:
   ```
   poetry install --no-root
   ```

This command will create a virtual environment and install all the necessary dependencies without installing the project itself as a package.

## Usage

User can upload a data file and knowledge file. The LLM will analyze the data and provide insights based on its knowledge of organic materials and molecular interactions.

## Roadmap

- [x] Implement analysis for molecular interactions as research assistant, capable of online semantic search.
- [x] Add in data intake from csv function.
- [x] Add in knowledge base prompt engineering refinement
- [ ] Implement a more agents for more complex analysis and query-retrieval based hypothesis generation (human in the loop)
- [ ] Enhance the Streamlit frontend with visualizations of molecular structures and data
- [ ] Integrate machine learning models for predictive analysis of material properties
- [ ] Integrate robotic operation sent our request to the lab for experimentation.

## Contributing

[Add guidelines for how others can contribute to your project, if applicable.]

## License

[Specify the license under which your project is released.]

## Contact

[Provide contact information or links for users to reach out with questions or feedback.]