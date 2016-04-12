# Selenium Grid parallel test example
Example parallel testing with Selenium Grid and Pytest.

## Quick start
1. Install required packages
  ```
  pip install -r requirements.txt
  ```

2. Start Selenium Hub and (2) nodes
  ```
  docker run -d -p 4444:4444 --name selenium-hub selenium/hub:2.53.0
  docker run -d -P -p 5998:5900 --link selenium-hub:hub selenium/node-firefox-debug:2.53.0
  docker run -d -P -p 5999:5900 --link selenium-hub:hub selenium/node-firefox-debug:2.53.0
  ```

3. Execute pytest
  ```
  py.test -n 2 --driver Remote --host localhost --port 4444 \
      --capability browserName firefox --variables capabilities.json test_grid.py
  ```

Open up [VNCViewer](https://www.realvnc.com/download/viewer/) to mapped ports (`localhost:5998` and `localhost:5999`, password: `secret`) and you should see both nodes are running different test method at once.
