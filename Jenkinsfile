pipeline {
    agent any
    environment {
        PATH = "/usr/bin/python3:$PATH"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/dimiaa/diploma.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 --version'
                sh 'pip install -r requirements.txt'
                sh 'pyinstaller --onefile sources/karaushev3d.py sources/main.py sources/LinearRegression.py'
            }
        }
    }
}