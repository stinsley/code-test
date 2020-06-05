pipeline {
    def commit_id
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Pull Down from GIT') { // Install any dependencies you need to perform testing

            git 'https://github.com/stinsley00/code-test.git'
            sh "git rev-parse --short HEAD > .git/commit-id"
            commit_id = readFile('.git/commit-id').trim()
        }
        stage('Unit Testing') { // Perform unit testing

        def testContainer = docker.image('ubuntu:18.04')
        testContainer.pull()
        //"--entrypoint='python3 app.py [1,2,3] [7,9,6]'"
        testContainer.inside() {

            script {
            sh """
            sudo apt-get update && apt-get install \
             -y --no-install-recommends python3 python3-virtualenv python3-pip
            """
            sh """
            export VIRTUAL_ENV=/opt/venv
            python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
            PATH="$VIRTUAL_ENV/bin:$PATH"
             """

              sh """
              python -m unittest discover -s tests
              """
            }
        }
    }

}