pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile sources/karaushev3d.py sources/main.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}