from flask import Flask, jsonify, request, render_template, send_file
from resume_checker import evaluate_resume, plot_pie_chart
import os

app = Flask(__name__)

# Ensure the 'uploads' and 'static' directories exist
os.makedirs('uploads', exist_ok=True)
os.makedirs('static', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    resume_type = request.form.get('resume_type', 'Default')

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        try:
            score, missing_keywords, resources = evaluate_resume(file_path, resume_type)
            chart_img = plot_pie_chart(score, resume_type)

            # Save the pie chart image to a static file
            chart_path = 'static/pie_chart.png'
            with open(chart_path, 'wb') as f:
                f.write(chart_img.getvalue())

            return render_template('result.html', score=score, missing_keywords=missing_keywords, resources=resources, chart_url=chart_path)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True,port=5016)
