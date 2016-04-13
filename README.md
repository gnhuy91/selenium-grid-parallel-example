# Selenium Grid parallel test example
Example parallel testing with Selenium Grid and Pytest.

## Quick start
1. Install required packages, using `virtualenv` is recommended
  ```
  pip install -r requirements.txt
  ```

2. Start Selenium Hub and (2) nodes
  ```
  docker run -d -p 4444:4444 --name selenium-hub selenium/hub:2.53.0
  docker run -d -P -p 5998:5900 --link selenium-hub:hub selenium/node-firefox-debug:2.53.0
  docker run -d -P -p 5999:5900 --link selenium-hub:hub selenium/node-firefox-debug:2.53.0
  ```
  See [here](https://github.com/SeleniumHQ/docker-selenium) for more info about Selenium docker images.

3. Execute pytest
  ```
  py.test -n 2 --html=report.html --driver Remote --host localhost --port 4444 \
      --capability browserName firefox --variables capabilities.json test_grid.py
  ```
  For more detail, see [examples on Gridlastic](https://www.gridlastic.com/python-code-example.html#pytest-plugin-pytest-selenium).

Open up [VNCViewer](https://www.realvnc.com/download/viewer/) to mapped ports (`localhost:5998` and `localhost:5999`, password: `secret`) and you should see both nodes are running different test method at once.

## Bonus
After executed above test, open the generated `report.html` (current directory) for test report.
