import os
import subprocess
import zipfile
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import shutil
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key')
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['COMPILED_FOLDER'] = 'compiled'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['COMPILED_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'java', 'mf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS or filename == 'MANIFEST.MF'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile_midlet():
    if 'java_file' not in request.files or 'manifest_file' not in request.files:
        return jsonify({'error': 'Both Java source and MANIFEST.MF files are required'}), 400
    
    java_file = request.files['java_file']
    manifest_file = request.files['manifest_file']
    
    if java_file.filename == '' or manifest_file.filename == '':
        return jsonify({'error': 'No files selected'}), 400
    
    if not java_file.filename.endswith('.java'):
        return jsonify({'error': 'Java file must have .java extension'}), 400
    
    timestamp = str(int(time.time()))
    work_dir = os.path.join(app.config['UPLOAD_FOLDER'], timestamp)
    os.makedirs(work_dir, exist_ok=True)
    
    try:
        java_filename = secure_filename(java_file.filename)
        java_path = os.path.join(work_dir, java_filename)
        java_file.save(java_path)
        
        manifest_path = os.path.join(work_dir, 'MANIFEST.MF')
        manifest_file.save(manifest_path)
        
        class_name = java_filename.replace('.java', '')
        
        compile_result = subprocess.run(
            ['javac', '-classpath', 'lib/cldcapi11.jar:lib/midpapi20.jar', java_path],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        logs = []
        logs.append("=== Compilation ===")
        if compile_result.stdout:
            logs.append(compile_result.stdout)
        if compile_result.stderr:
            logs.append(compile_result.stderr)
        
        if compile_result.returncode != 0:
            return jsonify({
                'error': 'Compilation failed',
                'logs': '\n'.join(logs)
            }), 400
        
        logs.append("Compilation successful!")
        
        class_file = os.path.join(work_dir, f'{class_name}.class')
        if not os.path.exists(class_file):
            return jsonify({
                'error': f'Class file not found: {class_name}.class',
                'logs': '\n'.join(logs)
            }), 400
        
        logs.append("\n=== Downgrading Bytecode to J2ME (Java 1.3) ===")
        downgraded_class = os.path.join(work_dir, f'{class_name}_j2me.class')
        downgrade_result = subprocess.run(
            ['java', '-cp', 'lib/asm-9.7.jar:.', 'BytecodeDowngrader', class_file, downgraded_class],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if downgrade_result.stdout:
            logs.append(downgrade_result.stdout)
        if downgrade_result.stderr:
            logs.append(downgrade_result.stderr)
        
        if downgrade_result.returncode != 0:
            return jsonify({
                'error': 'Bytecode downgrade failed',
                'logs': '\n'.join(logs)
            }), 400
        
        shutil.move(downgraded_class, class_file)
        
        jar_filename = f'{class_name}.jar'
        jar_path = os.path.join(app.config['COMPILED_FOLDER'], jar_filename)
        
        logs.append("\n=== Creating JAR ===")
        jar_result = subprocess.run(
            ['jar', 'cvfm', jar_path, manifest_path, '-C', work_dir, f'{class_name}.class'],
            capture_output=True,
            text=True
        )
        
        if jar_result.stdout:
            logs.append(jar_result.stdout)
        if jar_result.stderr:
            logs.append(jar_result.stderr)
        
        if jar_result.returncode != 0:
            return jsonify({
                'error': 'JAR creation failed',
                'logs': '\n'.join(logs)
            }), 400
        
        logs.append(f"\nJAR created successfully: {jar_filename}")
        logs.append(f"File size: {os.path.getsize(jar_path)} bytes")
        
        shutil.rmtree(work_dir)
        
        return jsonify({
            'success': True,
            'jar_filename': jar_filename,
            'logs': '\n'.join(logs)
        })
        
    except Exception as e:
        if os.path.exists(work_dir):
            shutil.rmtree(work_dir)
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_jar(filename):
    jar_path = os.path.join(app.config['COMPILED_FOLDER'], secure_filename(filename))
    if not os.path.exists(jar_path):
        return jsonify({'error': 'File not found'}), 404
    return send_file(jar_path, as_attachment=True, download_name=filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
