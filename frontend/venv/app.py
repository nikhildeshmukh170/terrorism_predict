import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Run the script and capture the output
    output = subprocess.check_output(['python', 'frontend/venv/group_model.py'])

    # Decode the byte string to utf-8
    output_text = output.decode('utf-8')

    # Now you can use the output_text variable which contains the output of your_script.py as a UTF-8 string
    classification_report = output_text

    # Parse classification report to find the top 3 groups with maximum support
    top_groups = []
    for line in classification_report.split('\n'):
        if line.strip() and not any(word in line for word in ['accuracy', 'macro avg', 'weighted avg']):
            # Ensure line contains at least 5 values before splitting
            if len(line.split()) >= 5:
                parts = line.split()
                group_name = ' '.join(parts[:-4])  # Join first few elements as group name
                support = int(parts[-1])  # Take the last element as support value

                # Add the group to top_groups if it has higher support than any of the existing top groups
                if len(top_groups) < 3 or support > top_groups[-1][1]:
                    top_groups.append((group_name.strip(), support))
                    top_groups = sorted(top_groups, key=lambda x: x[1], reverse=True)[:3]

    # Render template with the top 3 groups
    return render_template('index.html', top_groups=top_groups)

if __name__ == '__main__':
    app.run(debug=True)
