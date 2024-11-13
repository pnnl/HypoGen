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

## License

Copyright Battelle Memorial Institute

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

This material was prepared as an account of work sponsored by an agency of the
United States Government.  Neither the United States Government nor the United
States Department of Energy, nor Battelle, nor any of their employees, nor any
jurisdiction or organization that has cooperated in the development of these
materials, makes any warranty, express or implied, or assumes any legal
liability or responsibility for the accuracy, completeness, or usefulness or
any information, apparatus, product, software, or process disclosed, or
represents that its use would not infringe privately owned rights.

Reference herein to any specific commercial product, process, or service by
trade name, trademark, manufacturer, or otherwise does not necessarily
constitute or imply its endorsement, recommendation, or favoring by the United
States Government or any agency thereof, or Battelle Memorial Institute. The
views and opinions of authors expressed herein do not necessarily state or
reflect those of the United States Government or any agency thereof.

                 PACIFIC NORTHWEST NATIONAL LABORATORY
                              operated by
                                BATTELLE
                                for the
                   UNITED STATES DEPARTMENT OF ENERGY
                    under Contract DE-AC05-76RL01830
