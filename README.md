## Flask Application Design

### HTML Files

- **index.html:** The main page of the application, providing an interface for users to specify requirements and interact with the multi-agent system.
- **requirements.html:** Allows users to define agent behaviors, the environment, and other relevant requirements for their multi-agent system.
- **output.html:** Displays the results of the simulation, including agent interactions, environment changes, and performance metrics.
- **documentation.html:** Provides step-by-step instructions, tutorials, and reference materials to guide users through the application's functionality.

### Routes

- **`/requirements`**: Accepts POST requests with the user-provided requirements and processes them to generate a LangGraph configuration file.
- **`/execute`**: Initiates the simulation process by executing the generated LangGraph configuration file, simulating the multi-agent system, and generating results.
- **`/results`**: Retrieves the simulation results and sends them to the client, which displays them on the **output.html** page.
- **`/documentation`**: Redirects the user to the **documentation.html** page, providing access to help and guidance.