import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Run the script and capture the output
    output = subprocess.check_output(['python', 'Backend/group_model.py'])

    # Decode the byte string to utf-8
    output_text = output.decode('utf-8')

    # Now you can use the output_text variable which contains the output of your_script.py as a UTF-8 string
    classification_report = output_text

    # Parse classification report to find the organization with maximum support
    max_support_group = None
    max_support = -1
    for line in classification_report.split('\n'):
        if line.strip():
            # Ensure line contains at least 5 values before splitting
            if len(line.split()) >= 5:
                parts = line.split()
                group_name = ' '.join(parts[:-4])  # Join first few elements as group name
                support = int(parts[-1])  # Take the last element as support value
                if support > max_support:
                    max_support = support
                    max_support_group = group_name.strip()

    # Render template with the organization with maximum support
    return render_template('index.html', max_support_group=max_support_group)

if __name__ == '__main__':
    app.run(debug=True)
