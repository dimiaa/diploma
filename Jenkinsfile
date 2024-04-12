pipeline {
    agent any
    environment {
        PATH = "/usr/bin/python3"
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
                sh 'python3 sources/karaushev3d.py build sources/main.py build sources/LinearRegression.py build'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}