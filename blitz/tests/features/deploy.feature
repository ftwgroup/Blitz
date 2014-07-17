Feature: Deploy New Features to Servers
  In order to streamline the deployment process
  As a project team member
  We'll create a cmd-line deployment tool

  Scenario: Git Update
    Given uncommited code
    When I do a "git_update()"
    Then Do "git add" to stage changed files
    Then Do "git commit" on repository
    Then Do "git pull" to merge changes
    Then Do "git push" to update code base

  Scenario: Connect to Server
    Given ssh_access
    Given server
    Given Server name
    When I do a "connect_to_server(testserver6)
    Then Connect to server
    And return the open ssh portal

  Scenario: Start Server
    Given server name
    When I call "fab start_server

  Scenario: Deploy to Testing Environment
    Given published code
    Given a test server
    Given ssh credentials
    When I call "fab search_bar deploy" in cmd-line
    Then do Git Update
    Then Connect to Server
    Then deploy service to the server
    Then restart the service

  Scenario: Deploy to Testing Environment w/o server
    Given published code
    Given ssh credentials
    When I call "fab search_bar deploy" in cmd-line
    Then do git_update
    Then create test server

  Scenario: Deploy to Staging/Production Environment
    Given published code
    Given a production server
    Given ssh credentials
    When I call "fab search_bar deploy" in cmd-line
    Then do Git Update
    Then Connect to Server
    Then deploy service to the server
    Then restart the service

  Scenario: Create New Feature
    When I call "fab search_bar new_feature" in cmd-line
    Then add a new branch in git

  Scenario: Finish Feature
    Given finished branch
    When I call "fab search_bar finish_feature" in cmd-line
    Then do Git Update
    Then create a pull request

  Scenario: Trash Feature
    Given branch
    When I call "fab search_bar trash_feature" in cmd-line
    Then delete the branch

  Scenario: Update Keys
    Given public key
    When I call update_keys()
    Then put public key into list of approved users

  Scenario: List Servers
    Given workflow level (test or production)
    When I call "fab list_server"
    Then list the names of all the servers available for test hosting

  Scenario:
