Feature: Deploy New Features to Servers
  In order to streamline the deployment process
  As a project team member
  We'll create a cmd-line deployment tool

  Scenario: Git Update
    Given uncommited code
    When I call git_update()
    Then Do "git add" to stage changed files
    Then Do "git commit" on repository
    Then Do "git pull" to merge changes
    Then Do "git push" to update code base

  Scenario: Connect to Server
    Given ssh_access
    Given server
    Given Server name
    When I call connect_to_server(testserver6)
    Then Connect to server
    And return the open ssh portal

  Scenario: Start Server
    Given server name
    When I call "fab start_server" in cmd-line

  Scenario: Deploy to Testing Environment
    Given published code
    Given a test server
    Given valid ssh credentials
    When I call "fab search_bar deploy" in cmd-line
    Then do Git Update
    Then Connect to Server
    Then deploy service to the server
    Then restart the service

  Scenario: Deploy to Testing Environment w/o server
    Given published code
    Given valid ssh credentials
    When I call "fab search_bar deploy" in cmd-line
    Then do git_update
    Then create test server

  Scenario: Deploy to Staging/Production Environment
    Given published code
    Given a production server
    Given valid ssh credentials
    When I call "fab search_bar deploy" in cmd-line
    Then do Git Update
    Then Connect to Server
    Then deploy service to the server
    Then restart the service

  Scenario: Create New Feature
    When I call "fab search_bar new_feature" in cmd-line
    Then add a new branch to both local and remote repository

  Scenario: Finish Feature
    Given branch
    When I call "fab search_bar finish_feature" in cmd-line
    Then do Git Update
    Then create a pull request for branch
    Then delete

  Scenario: Trash Feature
    Given branch
    When I call "fab search_bar trash_feature" in cmd-line
    Then delete the branch from both local and remote repository

  Scenario: Update Keys
    Given public key
    Given Environment
    When I call update_keys()
    Then put public key into list of approved users dictated by Environments

  Scenario: List Servers
    Given workflow level <level>
    When I call "fab list_server" in cmd-line
    Then list the names of all the servers available for test hosting on <level>
    And list the environment of the servers

