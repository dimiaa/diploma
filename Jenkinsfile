pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/dimiaa/diploma.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'python sources/karaushev3d.py build sources/main.py build sources/LinearRegression.py build'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}