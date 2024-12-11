pipeline {
    agent any   // This tells Jenkins to use any available agent (machine) to run the pipeline

    stages {
        stage('Checkout') {  // Stage 1: Checkout the repository
            steps {
                checkout scm  // Fetch the source code from your GitHub repository
            }
        }

        stage('Build') {  // Stage 2: Build the project
            steps {
                echo 'Building the project...'  // Print a message to the console
                sh 'npm install'  // Example build command (for a Node.js project)
            }
        }

        stage('Test') {  // Stage 3: Run Tests
            steps {
                echo 'Running tests...'
                sh 'npm test'  // Replace with your testing command
            }
        }

        stage('Deploy') {  // Stage 4: Deploy the application
            steps {
                echo 'Deploying the application...'
                sh './deploy.sh'  // Replace with your deploy command or script
            }
        }
    }

    post {  // Optional: Actions to perform after the pipeline finishes
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
