pipeline {
    agent any
    environment {
        STAGE_ADMIN_LINK = 'https://oqg-staging.test-qr.com/helpdesk'
        STAGE_ADMIN_EMAIL = 'oqg-dev@outlook.com'
        STAGE_ADMIN_PASSWORD = '12345678'
        ALLURE_RESULTS_DIR = 'allure-results'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials-id', url: 'https://github.com/Bohdan-wtl/qr-generator.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Install Playwright Browsers') {
            steps {
                sh '. venv/bin/activate && playwright install'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'sudo apt-get install -y xvfb'
                sh '. venv/bin/activate && xvfb-run -a pytest --alluredir=${ALLURE_RESULTS_DIR}'
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**', fingerprint: true
            junit 'allure-results/**/*.xml'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
