pipeline {
    agent any
    environment {
        registry = "dimiaa/app"
        registryCredential = '7fd88827-0fec-4a11-b4bc-efde01eb1d9e'
        dockerImage = ''
    }
    stages {
        stage('Git checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/dimiaa/diploma.git'
            }
        }
        stage('Build Docker Image'){
            steps {
                 script {
                    dockerImage = docker.build registry
                 }
            }
        }
        stage('Upload Image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential)
                    dockerImage.push()
                }
            }
        }
        stage('Docker stop container') {
            steps {
                sh 'docker ps -f name=app -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=app -q | xargs -r docker container rm'
            }
        }
        stage('Docker run'){
            steps {
                script {
                    dockerImage.rin("-p 6000:6000 --rm --name app")
                }
            }
        }
    }
}