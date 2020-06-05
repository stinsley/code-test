node {
  def commit_id
      stage('Setup') { // Install any dependencies you need to perform testing

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
              pip install -r requirements.txt
              """

              sh """
              python -m unittest discover -s tests
              """
            }
        }
    }
}