# Query-Engine-for-English-Language

Problem Statement: Given a data source (csv per say), build a Query Engine for English language.

## Description

This project is a query engine built to provide fast and efficient search capabilities for BigBasket's product list. 
It leverages natural language processing to understand and retrieve product information based on user queries. 
Using a pre-trained vector space model, it finds the most relevant product descriptions that match the search intent. 
This API is ideal for integrating with e-commerce platforms to enhance product discovery.

## Setup

To run this project locally, follow the instructions below:

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**:  
   Use the following command to clone the repository to your local machine. Replace `<REPOSITORY_URL>` with the actual URL of the GitHub repository.

   git clone <REPOSITORY_URL>

2. Navigate to the project directory: Change into the project directory using the command line.
   cd path_to_cloned_repository

### Running the Application
1. Install dependencies: Install the required Python packages listed in 'requirements.txt'.

2. Start the FastAPI server:
Launch the server with the following command. The --reload flag is used for development purposes and enables live reloading.

To Run: uvicorn main:app --reload

Running the Application
With the server running, visit 'http://127.0.0.1:8000/docs' in your web browser to access the interactive API documentation provided by Swagger UI.
You can also test the API directly by sending GET requests to the following endpoint:

GET /query/?query={search_query}
Note: Replace {search_query} with the keywords you wish to search for.


### Sample Queries
Try out the query engine using the following examples:
1. For a basic product search:
   Search for natural hair care products by navigating to:
   http://127.0.0.1:8000/query/?query=natural+shampoo

2. For kitchen-related products:
   Find non-stick cookware items with the query:
   http://127.0.0.1:8000/query/?query=non-stick+pan


