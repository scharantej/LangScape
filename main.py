
# main.py

# Import necessary Flask and LangGraph libraries
from flask import Flask, request, render_template, redirect, url_for
import langgraph as lg
import json

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the requirements page
@app.route('/requirements', methods=['GET', 'POST'])
def requirements():
    if request.method == 'POST':
        # Extract the user-provided requirements from the request
        data = request.form.to_dict()
        requirements = json.loads(data['requirements'])

        # Generate a LangGraph configuration file based on the requirements
        config = lg.generate_config(requirements)

        # Save the configuration file to a temporary location
        with open('config.lg', 'w') as f:
            f.write(config)

        # Redirect the user to the execute page
        return redirect(url_for('execute'))

    return render_template('requirements.html')

# Define the route for executing the simulation
@app.route('/execute', methods=['GET'])
def execute():
    # Execute the LangGraph configuration file
    results = lg.execute('config.lg')

    # Save the results to a temporary location
    with open('results.json', 'w') as f:
        json.dump(results, f)

    # Redirect the user to the results page
    return redirect(url_for('results'))

# Define the route for displaying the results
@app.route('/results', methods=['GET'])
def results():
    # Load the simulation results from the temporary location
    with open('results.json', 'r') as f:
        results = json.load(f)

    # Render the results page with the simulation results
    return render_template('results.html', results=results)

# Define the route for the documentation page
@app.route('/documentation', methods=['GET'])
def documentation():
    return render_template('documentation.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
