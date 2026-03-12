# BrowserStack Integration with Robot Framework Selenium (Python) and Percy on Automate

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780) 

A minimal example repo showing how to run Robot Framework Selenium tests on **BrowserStack Automate**, with optional visual testing using **Percy (Percy on Automate)**.

It includes sample Robot tests, a BrowserStack config file (`browserstack.yml`), and the commands needed to run tests via `browserstack-sdk` and `percy exec`.

## Prerequisite
```
python3 should be installed
```

## Setup
* Clone the repo 
  ```
  git clone -b sdk https://github.com/browserstack/robot-browserstack.git
  ```
* It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate # on Mac
  env\Scripts\activate # on Windows
  ```
* Install dependencies 
  ```
  pip install -r requirements.txt
  ```  

## Set BrowserStack Credentials
* Add your BrowserStack username and access key in the `browserstack.yml` config fle.
* You can also export them as environment variables, `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY`:

  #### For Linux/MacOS
    ```
    export BROWSERSTACK_USERNAME=<browserstack-username>
    export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```
  #### For Windows
    ```
    set BROWSERSTACK_USERNAME=<browserstack-username>
    set BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    
    setx BROWSERSTACK_USERNAME=<browserstack-username>
    setx BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```

## Running tests

* To run sample tests:
  - To run the sample tests in parallel across the platforms defined in the `browserstack.yml` file, run:
    ```
    browserstack-sdk robot ./tests/test-1.robot
    ```

## Percy visual testing (BrowserStack + Percy on Automate)

The repository can be run through Percy to capture visual snapshots in your BrowserStack Automate runs.

1. Install Percy CLI (recommended global install):
    ```
    npm install -g @percy/cli
    ```

2. Install Percy SDK for Selenium (required for Percy snapshots):
    ```
    pip install percy-selenium
    ```

3. Export your Percy token (from your Percy project settings):
    ```
    export PERCY_TOKEN="<your token here>"
    ```

4. Run your Robot Framework tests through Percy:
    ```
    npx percy exec --verbose -- browserstack-sdk robot ./tests/test-1.robot
    ```

> **Note:** Percy snapshots are captured using `percy_screenshot` from `percy_selenium`. For Python-based Selenium tests, you can add `from percy import percy_screenshot` and call `percy_screenshot(driver, name="...")` in your test script. For Robot Framework tests, add a corresponding keyword in your test library that calls into the Percy SDK.

Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Additional Resources
* [Documentation for writing Automate test scripts in Python](https://www.browserstack.com/automate/python)
* [Customizing your tests on BrowserStack](https://www.browserstack.com/automate/capabilities)
* [Browsers & mobile devices for selenium testing on BrowserStack](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate)
* [Using REST API to access information about your tests via the command-line interface](https://www.browserstack.com/automate/rest-api)
* [Percy + BrowserStack Automate guide](https://www.browserstack.com/docs/percy/selenium/getting-started/python/integrate-your-tests?fw-lang=python#Percy_with_Automate)
